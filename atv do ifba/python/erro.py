Aluno = input("Digite seu Nome: ")
Nome = Aluno
N1 = float(input("Digite sua nota do S1: "))#Primeiro simestre
N2 = float(input("Digite sua nota do S2: "))
N3 = float(input("Digite sua nota do S3: "))
N4 = float(input("Digite sua nota do S4: "))

Media = (N1 + N2 + N3 + N4)

Resultado = Media

if Resultado >= 7:
    print("O Aluno", Nome,", Esta com a media de:", Resultado, "portanto está Aprovado!!")
else:
    print("O Aluno", Nome,",Esta com a media de: ", Resultado, "portanto está Reprovado :(" )

#-------=--------------------------------------questão 2-----------------------------------------------------
def classificar_triangulo():
    print("Digite os comprimentos dos lados do triângulo:")
ld1 = float(input("Lado 1: "))
ld2 = float(input("Lado 2: "))
ld3 = float(input("Lado 3: "))

if ld1 == ld2 == ld3:
        print("O triângulo é equilátero.")
elif ld1 == ld2 or ld1 == ld3 or ld2 == ld3:
        print("O triângulo é isósceles.")
else:
        print("O triângulo é escaleno.")


classificar_triangulo()

#-----------------------------------------------Questão3----------------------------------------------------

class Calendario:
    def _init_(self, dia, mes, ano):
        self.dia = dia
        self.mes = mes
        self.ano = ano

    def avancar_um_dia(self):
        dias_no_mes = self.dias_no_mes()
        if self.dia < dias_no_mes:
            self.dia += 1
        else:
            self.dia = 1
            if self.mes < 12:
                self.mes += 1
            else:
                self.mes = 1
                self.ano += 1

    def retroceder_um_dia(self):
        if self.dia > 1:
            self.dia -= 1
        else:
            if self.mes > 1:
                self.mes -= 1
                self.dia = self.dias_no_mes()
            else:
                self.mes = 12
                self.ano -= 1
                self.dia = self.dias_no_mes()

    def dias_no_mes(self):
        meses_com_31_dias = {1, 3, 5, 7, 8, 10, 12}
        meses_com_30_dias = {4, 6, 9, 11}

        if self.mes == 2:
            if self.ano % 4 == 0 and (self.ano % 100 != 0 or self.ano % 400 == 0):
                return 29 
            else:
                return 28  
        elif self.mes in meses_com_31_dias:
            return 31
        elif self.mes in meses_com_30_dias:
            return 30


data = Calendario(31, 12, 2022)

print(f"Data atual: {data.dia}/{data.mes}/{data.ano}")
data.avancar_um_dia()
print(f"Data avançada um dia: {data.dia}/{data.mes}/{data.ano}")
data.retroceder_um_dia()
print(f"Data retrocedida um dia: {data.dia}/{data.mes}/{data.ano}")

#-----------------------------------------------Questão4----------------------------------------------------
class Livro:
    def _init_(self, titulo, autor, ano_publicacao):
        self.titulo = titulo
        self.autor = autor
        self.ano_publicacao = ano_publicacao

    def formatar_info(self):
        return f"{self.titulo}, {self.autor} ({self.ano_publicacao})"

# Exemplo de uso:
livro1 = Livro("Dom Quixote", "Miguel de Cervantes", 1605)
print(livro1.formatar_info())

livro2 = Livro("Cem Anos de Solidão", "Gabriel García Márquez", 1967)
print(livro2.formatar_info())