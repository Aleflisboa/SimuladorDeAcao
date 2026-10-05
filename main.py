import yfinance as yf
import time
from datetime import datetime
from db import get_conexao


# ============================================================
# CONFIGURAÇÕES
# ============================================================

INTERVALO_ATUALIZACAO = 60  # segundos

LIMITE_ACIMA = 0.05
LIMITE_ABAIXO = -0.05


# ============================================================
# CLASSE DO BOT
# ============================================================

class BotAnalista:

    def __init__(self, nome, bot_id, ativo):
        self.nome = nome
        self.bot_id = bot_id
        self.ativo = ativo

        self.humor = "ESPERANDO"
        self.status_acao = "MEDIA (Boa)"

        self.historico_precos = []

    # --------------------------------------------------------
    # ANALISAR MERCADO
    # --------------------------------------------------------

    def analisar_mercado(self, preco_atual):

        self.historico_precos.append(preco_atual)

        # Mantém somente os últimos 3 preços
        if len(self.historico_precos) > 3:
            self.historico_precos.pop(0)

        # Ainda não temos preços suficientes
        if len(self.historico_precos) < 3:
            self.humor = "ESPERANDO"
            self.status_acao = "MEDIA (Boa)"
            return

        media = sum(self.historico_precos) / len(self.historico_precos)

        if media == 0:
            return

        variacao = (preco_atual - media) / media

        # Subiu mais de 5%
        if variacao > LIMITE_ACIMA:

            self.status_acao = "ACIMA (Agradavel)"
            self.humor = "FELIZ"

        # Caiu mais de 5%
        elif variacao < LIMITE_ABAIXO:

            self.status_acao = "BAIXO (Desagradavel)"
            self.humor = "COM_RAIVA"

        # Normal
        else:

            self.status_acao = "MEDIA (Boa)"
            self.humor = "ESPERANDO"

    # --------------------------------------------------------
    # SALVAR NO MYSQL
    # --------------------------------------------------------

    def salvar_analise(self, preco):

        conn = None
        cur = None

        try:

            conn = get_conexao()
            cur = conn.cursor()

            # Atualiza o bot atual
            cur.execute(
                """
                UPDATE bots
                SET preco = %s,
                    humor = %s,
                    status_acao = %s
                WHERE id = %s
                """,
                (
                    float(preco),
                    self.humor,
                    self.status_acao,
                    self.bot_id
                )
            )

            # Salva histórico, caso a tabela exista
            try:

                cur.execute(
                    """
                    INSERT INTO historico_analises
                    (bot_id, preco, humor, status_acao)
                    VALUES (%s, %s, %s, %s)
                    """,
                    (
                        self.bot_id,
                        float(preco),
                        self.humor,
                        self.status_acao
                    )
                )

            except Exception as erro_historico:

                print(
                    f"⚠️ Não foi possível salvar histórico "
                    f"do {self.nome}: {erro_historico}"
                )

            conn.commit()

            print(
                f"💾 {self.nome} atualizado no MySQL | "
                f"R$ {float(preco):.2f}"
            )

        except Exception as erro:

            print(
                f"❌ Erro ao salvar {self.nome}: {erro}"
            )

            if conn:
                conn.rollback()

        finally:

            if cur:
                cur.close()

            if conn:
                conn.close()

    # --------------------------------------------------------
    # MOSTRAR NO TERMINAL
    # --------------------------------------------------------

    def mostrar_comportamento(self, agora, preco):

        print(
            f"[{self.nome:<15}] "
            f"{self.ativo:<12} | "
            f"R$ {float(preco):>8.2f} | "
            f"Status: {self.status_acao:<22} | "
            f"Humor: {self.humor:<12} | "
            f"Atualização: {agora.strftime('%H:%M:%S')}"
        )


# ============================================================
# BUSCAR PREÇO
# ============================================================

def buscar_preco_atual(ticker):

    print(f"📡 Buscando preço de {ticker}...")

    try:

        ativo = yf.Ticker(ticker)

        # ----------------------------------------------------
        # PRIMEIRA TENTATIVA
        # ----------------------------------------------------

        try:

            preco = ativo.fast_info.get("last_price")

            if preco is not None:

                preco = float(preco)

                print(
                    f"💰 {ticker}: R$ {preco:.2f}"
                )

                return preco

        except Exception as erro:

            print(
                f"⚠️ fast_info falhou para {ticker}: {erro}"
            )

        # ----------------------------------------------------
        # SEGUNDA TENTATIVA
        # ----------------------------------------------------

        dados = ativo.history(
            period="1d",
            interval="1m"
        )

        if dados.empty:

            print(
                f"❌ Nenhum dado encontrado para {ticker}"
            )

            return None

        dados = dados.dropna(
            subset=["Close"]
        )

        if dados.empty:

            print(
                f"❌ Não foi possível obter o preço de {ticker}"
            )

            return None

        preco = float(
            dados["Close"].iloc[-1]
        )

        print(
            f"💰 {ticker}: R$ {preco:.2f}"
        )

        return preco

    except Exception as erro:

        print(
            f"❌ Erro ao buscar {ticker}: {erro}"
        )

        return None


# ============================================================
# CARREGAR BOTS DO MYSQL
# ============================================================

def carregar_bots():

    conn = None
    cur = None

    try:

        conn = get_conexao()

        cur = conn.cursor()

        cur.execute(
            """
            SELECT id, nome, ativo
            FROM bots
            """
        )

        registros = cur.fetchall()

        bots = []

        for bot_id, nome, ativo in registros:

            bot = BotAnalista(
                nome,
                bot_id,
                ativo
            )

            bots.append(bot)

        return bots

    except Exception as erro:

        print(
            f"❌ Erro ao carregar bots: {erro}"
        )

        return []

    finally:

        if cur:
            cur.close()

        if conn:
            conn.close()


# ============================================================
# SIMULAÇÃO / ATUALIZAÇÃO
# ============================================================

def simular_mercado():

    print("=" * 100)
    print(" STOCKBOTS - MONITORAMENTO DE ATIVOS ")
    print("=" * 100)

    bots = carregar_bots()

    if not bots:

        print(
            "❌ Nenhum bot encontrado no banco de dados."
        )

        return

    print(
        f"🤖 {len(bots)} bot(s) carregado(s)."
    )

    print(
        f"⏱️ Atualização a cada "
        f"{INTERVALO_ATUALIZACAO} segundos."
    )

    print("=" * 100)

    while True:

        agora = datetime.now()

        print()
        print(
            f"🔄 ATUALIZAÇÃO "
            f"{agora.strftime('%d/%m/%Y %H:%M:%S')}"
        )

        print("-" * 100)

        for bot in bots:

            preco = buscar_preco_atual(
                bot.ativo
            )

            # Se não conseguiu preço,
            # não altera o banco
            if preco is None:

                print(
                    f"⚠️ {bot.nome}: "
                    f"preço não encontrado."
                )

                continue

            # Analisa o preço
            bot.analisar_mercado(
                preco
            )

            # Mostra no terminal
            bot.mostrar_comportamento(
                agora,
                preco
            )

            # SALVA NO MYSQL
            bot.salvar_analise(
                preco
            )

        print("-" * 100)

        print(
            f"⏳ Próxima atualização em "
            f"{INTERVALO_ATUALIZACAO} segundos..."
        )

        time.sleep(
            INTERVALO_ATUALIZACAO
        )


# ============================================================
# INICIAR PROGRAMA
# ============================================================

if __name__ == "__main__":

    simular_mercado()