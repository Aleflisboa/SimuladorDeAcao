print("Olá, Bem-vindo ão banco Metro Boomin.")

          

class EscolherConta:
    def escolher_e_confirmar(self, saldo_inicial, limite_inferior=None):
        escolha = input("Escolha sua conta (corrente, poupança): ").lower()
        
        if escolha == "corrente":
            return ContaCorrente(saldo_inicial)
        elif escolha == "poupança":
            return ContaPoupanca(saldo_inicial, limite_inferior)
        else:
            print("Erro na sua escolha")
            return None

class Banco:
    def __init__(self, saldo_inicial):
        self._saldo = saldo_inicial

    def realizar_saque(self, quantia):
        if quantia > 0 and quantia <= self._saldo:
            self._saldo -= quantia
            return True
        else:
            print("Erro: Quantia de saque inválida")
            return False

    def ver_saldo(self):
        return self._saldo

class ContaCorrente(Banco): #Aqui a conta corrente herda as informação da classe "Banco"
    def realizar_saque(self, quantia):
        __tarifa = 5 #A variavel tarixa é privada utilizando dois "_". dessa forma a variavel tarifa não deve (mas pode) ser alterada
        if super().realizar_saque(quantia + __tarifa): #"realizar saque" e "tarifa" permite o polimorfismo usar o mesmo nome só que com metados diferentes. 
            print("Saque realizado com uma taxa de", __tarifa, "reais")
            return True
        else:
            return False

class ContaPoupanca(Banco): #Aqui a conta Poupança herda as informação da classe "Banco"
    def __init__(self, saldo_inicial, limite_inferior):
        super().__init__(saldo_inicial)
        self.limite_inferior = limite_inferior

    def realizar_saque(self, quantia):
        if quantia > 0 and (self._saldo - quantia) >= self.limite_inferior:
            self._saldo -= quantia
            return True
        else:
            print("Erro: Quantia de saque inválida para conta poupança")
            return False


if __name__ == "__main__":
    escolher_conta = EscolherConta()

    conta_escolhida = escolher_conta.escolher_e_confirmar(1000, 100)

    if conta_escolhida:
        if conta_escolhida.realizar_saque(500):
            print("Saque bem-sucedido. Saldo restante:", conta_escolhida.ver_saldo())
        else:
            print("Saque falhou. Saldo atual:", conta_escolhida.ver_saldo())

        print("Saldo atual:", conta_escolhida.ver_saldo())

