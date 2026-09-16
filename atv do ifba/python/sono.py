class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def calcular_desconto(self):
 
        return 0

class ProdutoEletronico(Produto):
    def __init__(self, nome, preco, garantia_meses):
        super().__init__(nome, preco)
        self.garantia_meses = garantia_meses

    def calcular_desconto(self):

        return self.preco * 0.1

class ProdutoAlimenticio(Produto):
    def __init__(self, nome, preco, data_validade):
        super().__init__(nome, preco)
        self.data_validade = data_validade

    def calcular_desconto(self):

        return self.preco * 0.05

# Exemplo de uso
produto1 = Produto(nome="Livro", preco=50)
produto2 = ProdutoEletronico(nome="Smartphone", preco=1000, garantia_meses=12)
produto3 = ProdutoAlimenticio(nome="Chocolate", preco=5, data_validade="2024-01-01")

print(f"Desconto para o produto {produto1.nome}: R${produto1.calcular_desconto()}")
print(f"Desconto para o produto {produto2.nome}: R${produto2.calcular_desconto()}")
print(f"Desconto para o produto {produto3.nome}: R${produto3.calcular_desconto()}")

#-------------------------Questão 2

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def apresentar(self):
        print(f"Olá, meu nome é {self.nome} e tenho {self.idade} anos.")

class Estudante(Pessoa):
    def __init__(self, nome, idade, curso):
        super().__init__(nome, idade)
        self.curso = curso

    def apresentar(self):
        print(f"Oi, meu nome é {self.nome}, tenho {self.idade} anos e estou cursando {self.curso}.")

class Professor(Pessoa):
    def __init__(self, nome, idade, disciplina):
        super().__init__(nome, idade)
        self.disciplina = disciplina

    def apresentar(self):
        print(f"Olá, sou o professor {self.nome}, tenho {self.idade} anos e leciono a disciplina de {self.disciplina}.")


pessoa1 = Pessoa(nome="Metro Boomin", idade=25)
estudante1 = Estudante(nome="Maria", idade=20, curso="Engenharia")
professor1 = Professor(nome="Carlos", idade=35, disciplina="Matemática")

pessoa1.apresentar()
estudante1.apresentar()
professor1.apresentar()

#-------------------------Questão 3
class Figura:
    def desenhar(self):
        print("Desenhando uma figura genérica.")

class Circulo(Figura):
    def __init__(self, raio):
        self.raio = raio

    def desenhar(self):
        print(f"Desenhando um círculo com raio {self.raio}.")

class Quadrado(Figura):
    def __init__(self, lado):
        self.lado = lado

    def desenhar(self):
        print(f"Desenhando um quadrado com lado {self.lado}.")

figura_generica = Figura()
circulo = Circulo(raio=5)
quadrado = Quadrado(lado=4)

figura_generica.desenhar()
circulo.desenhar()
quadrado.desenhar()
#--------------Questão 4

class Escola:
    def __init__(self, nome, endereco):
        self.nome = nome
        self.endereco = endereco
        self.alunos_matriculados = []

    def matricular_aluno(self, aluno):
        self.alunos_matriculados.append(aluno)
        print(f"Aluno {aluno.nome} matriculado na escola {self.nome}.")

class EscolaEnsinoFundamental(Escola):
    def __init__(self, nome, endereco, anos_ciclo):
        super().__init__(nome, endereco)
        self.anos_ciclo = anos_ciclo

    def realizar_prova_final(self):
        print("Realizando prova final para os alunos do Ensino Fundamental.")

class EscolaEnsinoMedio(Escola):
    def __init__(self, nome, endereco, serie):
        super().__init__(nome, endereco)
        self.serie = serie

    def realizar_vestibular(self):
        print("Realizando vestibular para os alunos do Ensino Médio.")


escola1 = Escola(nome="Escola A", endereco="Rua 123, Cidade X")
escola_fundamental = EscolaEnsinoFundamental(nome="Escola B", endereco="Rua 456, Cidade Y", anos_ciclo=9)
escola_medio = EscolaEnsinoMedio(nome="Escola C", endereco="Rua 789, Cidade Z", serie="3º Ano")


aluno1 = {"nome": "João", "idade": 14}
aluno2 = {"nome": "Maria", "idade": 16}


escola1.matricular_aluno(aluno1)
escola_fundamental.matricular_aluno(aluno1)
escola_medio.matricular_aluno(aluno2)


escola_fundamental.realizar_prova_final()
escola_medio.realizar_vestibular()
#=----------32498523234243141Questão 5
class Jogo:
    def __init__(self, titulo, genero):
        self.titulo = titulo
        self.genero = genero

    def jogar(self):
        print(f"Jogando o jogo {self.titulo} do gênero {self.genero}.")

class JogoAventura(Jogo):
    def __init__(self, titulo, genero, tema_aventura):
        super().__init__(titulo, genero)
        self.tema_aventura = tema_aventura

    def explorar_mundo(self):
        print(f"Explorando o mundo do jogo de aventura '{self.titulo}'.")

class JogoEstrategia(Jogo):
    def __init__(self, titulo, genero, modo_estrategia):
        super().__init__(titulo, genero)
        self.modo_estrategia = modo_estrategia

    def planejar_estrategia(self):
        print(f"Planejando estratégias no jogo de estratégia '{self.titulo}'.")


jogo_generico = Jogo(titulo="Jogo Genérico", genero="Indefinido")
jogo_aventura = JogoAventura(titulo="Aventura Fantástica", genero="Aventura", tema_aventura="Fantasia")
jogo_estrategia = JogoEstrategia(titulo="Estratégia Militar", genero="Estratégia", modo_estrategia="Combate tático")


jogo_generico.jogar()
jogo_aventura.jogar()
jogo_estrategia.jogar()


jogo_aventura.explorar_mundo()
jogo_estrategia.planejar_estrategia()

