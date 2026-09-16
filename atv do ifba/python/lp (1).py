class Pessoa:
    def _init_(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def cumprimentar(self):
        print(f"Olá, meu nome é {self.nome} e tenho {self.idade} anos.")

class Cachorro:
    def _init_(self, nome, raca):
        self.nome = nome
        self.raca = raca

    def latir(self):
        print("Au au!")

    def apresentar(self):
        print(f"Oi, eu sou {self.nome}, da raça {self.raca}.")


if  __name__ == "_main_":
    
    pessoa1 = Pessoa("Alef", 19)
    cachorro1 = Cachorro("Dante", "Pitbull", "Cachorro de forças inimigas, o mal")


    pessoa1.cumprimentar()
    cachorro1.latir()
    cachorro1.apresentar()