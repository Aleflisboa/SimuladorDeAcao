import yfinance as yf
import pandas as pd
import time
from datetime import datetime
from db import get_conexao


PERIODO = "1d"
INTERVALO = "5m"
LIMITE_ACIMA = 0.05
LIMITE_ABAIXO = -0.05


class BotAnalista:
    def __init__(self, nome, bot_id, acao):
        self.nome = nome
        self.bot_id = bot_id
        self.acao = acao
        self.humor = "ESPERANDO"
        self.status_acao = "MEDIA"
        self.historico_precos = []
        
    def analisar_mercado(self, preco_atual):
        self.historico_precos.append(preco_atual)
        
        if len(self.historico_precos) < 3:
            self.humor = "ESPERANDO"
            self.status_acao = "MEDIA"
            return

        media = sum(self.historico_precos[-3:]) / 3
        variacao = (preco_atual - media) / media

        if variacao > LIMITE_ACIMA:
            self.status_acao = "ACIMA (Agradavel)"
            self.humor = "FELIZ"
        elif variacao < LIMITE_ABAIXO:
            self.status_acao = "BAIXO (Desagradavel)"
            self.humor = "COM_RAIVA"
        else:
            self.status_acao = "MEDIA (Boa)"
            self.humor = "ESPERANDO"
    
    def salvar_analise(self, preco):
        
     try:
        conn = get_conexao()
        cur = conn.cursor()

        # Salva no histórico
        cur.execute(
            """INSERT INTO historico_analises
               (bot_id, preco, humor, status_acao)
               VALUES (%s, %s, %s, %s)""",
            (
                self.bot_id,
                float(preco),
                self.humor,
                self.status_acao
            )
        )

        # Atualiza o estado atual do bot
        cur.execute(
            """UPDATE bots
               SET preco = %s,
                   humor = %s,
                   status_acao = %s
               WHERE id = %s""",
            (
                float(preco),
                self.humor,
                self.status_acao,
                self.bot_id
            )
        )

        conn.commit()

        cur.close()
        conn.close()

     except Exception as e:
        print(f"⚠️ Erro ao salvar análise do {self.nome}: {e}")

    def mostrar_comportamento(self, agora):
      acao_visual = "📈"  # exemplo

      print(
        f"[{self.nome:<15}] "
        f"print ultima Atulização: {agora.strftime('%H/%M/%S')}' | "
        f"Ação: {self.status_acao:<22} | "
        f"Humor: {self.humor:<12} | "
        f"{acao_visual}"
    )


def buscar_dados_yahoo(ticker, periodo, intervalo):
    print(f"📡 Buscando dados de {ticker} no Yahoo Finance...")
    acao = yf.Ticker(ticker)
    dados = acao.history(period=periodo, interval=intervalo)
    
    if dados.empty:
        print("❌ Nenhum dado encontrado. Verifique o ticker ou a conexão.")
        return None
    
    print(f"✅ {len(dados)} dias de dados carregados com sucesso!\n")
    return dados

def simular_mercado():
    print("="*100)
    print(f" SIMULADOR DE ANÁLISE DE MERCADO - (Dados Reais do Yahoo Finance) ")
    print("="*100)

  # 🔹 Busca (ou cria) os 3 bots no banco
conn = get_conexao()
cur = conn.cursor()

cur.execute("""
    SELECT id, nome, acao
    FROM bots
""")

registros = cur.fetchall()

bots = []

for bot_id, nome, acao in registros:
    bots.append(BotAnalista(nome, bot_id, acao))

    cur.close()
    conn.close()


for bot in bots:

    dados = buscar_dados_yahoo(
        bot.acao,
        PERIODO,
        INTERVALO
    )
    if dados is not None:
     print(f"Quantidade de dados: {len(dados)}")
     print(dados.tail())
    
    print(f"Ticker do bot: {bot.acao}")

    if dados is None:
        continue

    for agora, linha in dados.iterrows():

        preco = linha["Close"]

        bot.analisar_mercado(preco)
        bot.mostrar_comportamento(agora)
        bot.salvar_analise(preco)

        time.sleep(2)
        
    # Itera sobre cada dia do histórico real
    agora = datetime.now()
    for agora, linha in dados.iterrows():
        preco = linha['Close']
        
        print(f"\n--- {agora.strftime('%H%M/%S')} | VALE3 Fechou em: R$ {preco:.2f} ---")

    print("\n" + "="*100)
    print(" FIM DA SIMULAÇÃO ")


if __name__ == "__main__":
    simular_mercado()