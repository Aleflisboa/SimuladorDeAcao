import yfinance as yf
import pandas as pd
import time
from datetime import datetime

TICKER = "VALE3.SA"
PERIODO = "3mo"
INTERVALO = "1d"
LIMITE_ACIMA = 0.05
LIMITE_ABAIXO = -0.05

class BotAnalista:
    def __init__(self, nome):
        self.nome = nome
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

    def mostrar_comportamento(self, data):

        if self.humor == "FELIZ":
            acao_visual = "Comemorando"
        elif self.humor == "COM_RAIVA":
            acao_visual = "batendo na mesa"
        else:
            acao_visual = "Analisando"

        print(f"[{self.nome}] {data.strftime('%D/%M/%Y')} | {self.status_acao<22} | {self.humor:12} | {acao_visual}")

    def buscar_dados_yahoo(ticker, periodo, intervalo):
        print (f"buscando dados de {ticker} no yahoo finance...")
        acao = yf.Ticker(ticker)
        dados = acao.history(period=periodo, interval=intervalo)

        if dados.empty:
            print("nenhum dado encontrado")
            return None
        
        print(f"{len(dados)} dias de dados carregados com sucesso\n")
        return dados

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
    print(f" SIMULADOR DE ANÁLISE DE MERCADO - {TICKER} (Dados Reais do Yahoo Finance) ")
    print("="*100)

    dados = buscar_dados_yahoo(TICKER, PERIODO, INTERVALO)
    if dados is None:
        return

    # Cria 3 bots com personalidades (mesma lógica, nomes diferentes)
    bots = [
        BotAnalista("Bot_Alfa"),
        BotAnalista("Bot_Beta"),
        BotAnalista("Bot_Gama")
    ]

    # Itera sobre cada dia do histórico real
    for data, linha in dados.iterrows():
        preco_fechamento = linha['Close']
        
        print(f"\n--- {data.strftime('%d/%m/%Y')} | VALE3 Fechou em: R$ {preco_fechamento:.2f} ---")
        
        for bot in bots:
            bot.analisar_mercado(preco_fechamento)
            bot.mostrar_comportamento(data)

        time.sleep(0.5)  # Pausa para leitura

    print("\n" + "="*100)
    print(" FIM DA SIMULAÇÃO ")


if __name__ == "__main__":
    simular_mercado()