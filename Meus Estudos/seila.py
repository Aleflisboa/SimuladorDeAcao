import msvcrt
import os


menu = ["Cadastrar", "Listar", "Sair"]
posicao_atual = 0
pessoa = {}

def mostrar_menu():
    os.system("cls")
    print("===============Menu===============\n")
    for i, item in enumerate(menu):
        if i == posicao_atual:
            print(f"> {item}")
        else:
            print(f"  {item}")   
                                   

while True:
    mostrar_menu()
    
    tecla = msvcrt.getch()
    
    if tecla == b'\xe0':
        tecla = msvcrt.getch()
        
        if tecla == b'H':
            posicao_atual -= 1
        elif tecla == b'P':
            posicao_atual += 1
    
    if tecla == b'\r':
        print(f"\n voce escolheu: {menu[posicao_atual]}")
            
    if menu[posicao_atual] == "Sair":
            print(f"Encerrado ")
            break
    
nome = (input("digite seu nome:"))
pessoa["nome"] = nome
print("bem-vindo {}".format(nome)) #".format" faz que a variavel "nome" caber dentro dos "{}"        
posicao_atual %= len(menu)
        
        
            
"""O método keys() é usado para obter as chaves de um dicionário. 
No entanto, spam é uma lista, não um dicionário, então isso resultará em um erro.
Se spam fosse um dicionário, keys() retornaria uma view object que exibe as chaves do dicionário. 
Para obter uma lista das chaves, você pode usar a função"""

"""
nome = (input("digite seu nome:"))
nomelist = [nome]

nomelist = [nome.upper()] #upper é um método que converte uma string para maiúscula. O getattr é usado para chamar o método upper da variável nome.
print(nomelist)
------------------------------------------
pessoa = {}
nome = (input("digite seu nome:"))
pessoa["nome"] = nome
print(pessoa)
"""

"""for i in range(5):
    print(i)"""