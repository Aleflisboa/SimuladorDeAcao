import math

class FiguraGeometrica:
    def __init__(self):
        self._area = 0
        self._perimetro = 0

    def calcular_area(self):
        pass

    def calcular_perimetro(self):
        pass

    def get_area(self):
        return self._area

    def get_perimetro(self):
        return self._perimetro

class Circulo(FiguraGeometrica):
    def __init__(self, raio):
        super().__init__()
        self._raio = raio
        self.calcular_area()
        self.calcular_perimetro()

    def calcular_area(self):
        self._area = math.pi * self._raio**2

    def calcular_perimetro(self):
        self._perimetro = 2 * math.pi * self._raio

class Quadrado(FiguraGeometrica):
    def __init__(self, lado):
        super().__init__()
        self._lado = lado
        self.calcular_area()
        self.calcular_perimetro()

    def calcular_area(self):
        self._area = self._lado**2

    def calcular_perimetro(self):
        self._perimetro = 4 * self._lado

if __name__ == "__main__":
    # Exemplo de uso
    raio_circulo = 5
    circulo = Circulo(raio_circulo)
    print(f"Círculo - Área: {circulo.get_area()}, Perímetro: {circulo.get_perimetro()}")

    lado_quadrado = 4
    quadrado = Quadrado(lado_quadrado)
    print(f"Quadrado - Área: {quadrado.get_area()}, Perímetro: {quadrado.get_perimetro()}")

#Second Quest

class Empregado:
    def __init__(self, nome, salario_base):
        self._nome = nome
        self._salario_base = salario_base

    def calcular_salario(self):
        return self._salario_base

    def calcular_beneficios(self):
        return "Benefícios básicos: Plano de saúde, seguro de vida."

    def get_nome(self):
        return self._nome

class Gerente(Empregado):
    def __init__(self, nome, salario_base, bonus):
        super().__init__(nome, salario_base)
        self._bonus = bonus

    def calcular_salario(self):
        return self._salario_base + self._bonus

    def calcular_beneficios(self):
        beneficios_empregado = super().calcular_beneficios()
        return f"{beneficios_empregado} Benefícios adicionais para gerentes: Bônus de performance."

class Analista(Empregado):
    def __init__(self, nome, salario_base, vale_refeicao):
        super().__init__(nome, salario_base)
        self._vale_refeicao = vale_refeicao

    def calcular_salario(self):
        return self._salario_base

    def calcular_beneficios(self):
        beneficios_empregado = super().calcular_beneficios()
        return f"{beneficios_empregado} Benefícios adicionais para analistas: Vale refeição."

if __name__ == "__main__":

    gerente = Gerente("Alef", 5000, 1000)
    analista = Analista("Maria", 3000, 400)

    print(f"{gerente.get_nome()} - Salário: {gerente.calcular_salario()}, Benefícios: {gerente.calcular_beneficios()}")
    print(f"{analista.get_nome()} - Salário: {analista.calcular_salario()}, Benefícios: {analista.calcular_beneficios()}")

#Third Quest 

class Produto:
    def __init__(self, nome, preco_unitario, quantidade_estoque):
        self._nome = nome
        self._preco_unitario = preco_unitario
        self._quantidade_estoque = quantidade_estoque

    def calcular_preco_com_desconto(self, desconto_percentual):
        preco_com_desconto = self._preco_unitario * (1 - desconto_percentual / 100)
        return preco_com_desconto

    def calcular_valor_total_em_estoque(self):
        valor_total = self._preco_unitario * self._quantidade_estoque
        return valor_total

    def get_nome(self):
        return self._nome

    def get_preco_unitario(self):
        return self._preco_unitario

    def get_quantidade_estoque(self):
        return self._quantidade_estoque

class ProdutoEletronico(Produto):
    def __init__(self, nome, preco_unitario, quantidade_estoque, garantia_meses):
        super().__init__(nome, preco_unitario, quantidade_estoque)
        self._garantia_meses = garantia_meses

    def calcular_valor_total_em_estoque(self):
        valor_total = super().calcular_valor_total_em_estoque()
        return valor_total + valor_total * 0.1

class ProdutoAlimenticio(Produto):
    def __init__(self, nome, preco_unitario, quantidade_estoque, data_validade):
        super().__init__(nome, preco_unitario, quantidade_estoque)
        self._data_validade = data_validade

    def calcular_preco_com_desconto(self, desconto_percentual):
      
        return super().calcular_preco_com_desconto(0)

if __name__ == "__main__":
   
    produto_generico = Produto("Alexa", 50, 100)
    produto_eletronico = ProdutoEletronico("TV", 1500, 5, 12)
    produto_alimenticio = ProdutoAlimenticio("Chocolate", 5, 200, "01/01/2024")

    print(f"{produto_generico.get_nome()} - Valor total em estoque: {produto_generico.calcular_valor_total_em_estoque()}")
    print(f"{produto_eletronico.get_nome()} - Valor total em estoque: {produto_eletronico.calcular_valor_total_em_estoque()}")
    print(f"{produto_alimenticio.get_nome()} - Preço com desconto: {produto_alimenticio.calcular_preco_com_desconto(10)}")


#Fourth Quest

class ContaCorrente:
    def __init__(self, saldo_inicial=0):
        self._saldo = saldo_inicial

    def depositar(self, quantia):
        if quantia > 0:
            self._saldo += quantia
            print(f"Depósito de {quantia} realizado. Novo saldo: {self._saldo}")
        else:
            print("Erro: Quantia de depósito inválida.")

    def sacar(self, quantia):
        if quantia > 0 and quantia <= self._saldo:
            self._saldo -= quantia
            print(f"Saque de {quantia} realizado. Novo saldo: {self._saldo}")
        else:
            print("Erro: Quantia de saque inválida.")

    def verificar_saldo(self):
        return self._saldo

class ContaEmpresarial(ContaCorrente):
    def __init__(self, saldo_inicial=0, limite_empresarial=0):
        super().__init__(saldo_inicial)
        self._limite_empresarial = limite_empresarial

    def sacar(self, quantia):
        limite_total = self._saldo + self._limite_empresarial
        if quantia > 0 and quantia <= limite_total:
            self._saldo -= quantia
            print(f"Saque de {quantia} realizado. Novo saldo: {self._saldo}")
        else:
            print("Erro: Quantia de saque inválida para conta empresarial.")

class ContaPessoal(ContaCorrente):
    def sacar(self, quantia):
        if quantia > 0 and quantia <= self._saldo:
            self._saldo -= quantia
            print(f"Saque de {quantia} realizado. Novo saldo: {self._saldo}")
        else:
            print("Erro: Quantia de saque inválida para conta pessoal.")

if __name__ == "__main__":

    conta_empresarial = ContaEmpresarial(saldo_inicial=1000, limite_empresarial=500)
    conta_pessoal = ContaPessoal(saldo_inicial=500)

    conta_empresarial.depositar(200)
    conta_empresarial.sacar(800)
    print(f"Saldo conta empresarial: {conta_empresarial.verificar_saldo()}")

    conta_pessoal.depositar(300)
    conta_pessoal.sacar(100)
    print(f"Saldo conta pessoal: {conta_pessoal.verificar_saldo()}")