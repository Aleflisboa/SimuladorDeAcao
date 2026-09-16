
n1 = float(input("Digite um numero: "))
n2 = float(input("Digite um numero: "))

m = (n1 + n2) / 2

print(m)

#-------------------tabuada-----------------
n1 = int(input(""))

print("{} e {:2}".format(1, (n1 * 2)))

#-----------------ps---------------------
import os
fruta = ["maça","banana","uva"]

ps = input("oque deseja procura?: ")

while True:
    if (ps not in fruta):
        os.system("cls")
        print("não encontrado")
    elif(ps in fruta):
        print("encontrado")

#---------------------------converção de temper
c = float(input("temperatura atual: "))

conv = (c * 1.8 + 32)
convF = (c - 32) / 1.8
print(conv, convF)

#---------------------------carros
dias = float(input(""))
km = float(input(""))

p = 60 * dias
p2 = km * 0.15

print(p , p2)