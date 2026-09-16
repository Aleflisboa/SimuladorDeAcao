num_1 = int (input(("Digite um numero")))
num_2 = int (input(("Digite um numero")))

soma = num_1 + num_2

print( f'A soma de {num_1} + {num_2} é: {soma}' )

#---------------------------------------------------------------questão 2--------------------------------------------------------------

numero = int(input("Digite um número: "))

def verificar_par_ou_impar(numero):
    if numero % 2 == 0:
        return "Par"
    else:
        return "Ímpar"
    
resultado = verificar_par_ou_impar(numero)
print(f"O número {numero} é {resultado}.")

#----------------------------------------------------------questão 3-----------------------------------------------------

numero = int(input("Digite um número para calcular a fatorial: "))

def calcular_fatorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * calcular_fatorial(n - 1)

if numero < 0:
    print("Fatorial é indefinida para números negativos.")
else:
    resultado = calcular_fatorial(numero)
    print(f"A fatorial de {numero} é {resultado}.")

#----------------------------------------------------------questão 4-----------------------------------------------------

frase = input("Digite uma frase: ")

def contar_vogais(frase):
    vogais = "aeiouAEIOU"
    contador = 0
    for char in frase:
        if char in vogais:
            contador += 1
    return contador

resultado = contar_vogais(frase)
print(f"A frase '{frase}' contém {resultado} vogais.")

#----------------------------------------------------------questão 5-----------------------------------------------------

ano = int(input("Digite um ano para verificar se é bissexto: "))

def eh_bissexto(ano):
    
    return ano % 4 == 0 and (ano % 100 != 0 or ano % 400 == 0)

if eh_bissexto(ano):
    print(f"{ano} é um ano bissexto.")
else:
    print(f"{ano} não é um ano bissexto.")

#----------------------------------------------------------questão 6-----------------------------------------------------

    
numero = int(input("Digite o número de termos da sequência de Fibonacci desejados: "))  
    
def calcular_fibonacci(n):
    fibonacci_sequence = [0, 1]

    for _ in range(2, n):
        next_term = fibonacci_sequence[-1] + fibonacci_sequence[-2]
        fibonacci_sequence.append (next_term)

    return fibonacci_sequence


if numero < 0:
    print("Por favor, insira um número não-negativo.")
else:
    resultado = calcular_fibonacci(numero)
    print(f"Sequência de Fibonacci com {numero} termos: {resultado}")

#----------------------------------------------------------questão 7-----------------------------------------------------

import math

area_a_pintar = float(input("Digite o tamanho da área a ser pintada em metros quadrados: "))

preco_por_lata = 80.00

def calcular_quantidade_latas(area):
    cobertura_por_lata = 18 * 3 
    quantidade_latas = math.ceil(area / cobertura_por_lata)
    return quantidade_latas

def calcular_preco_total(quantidade_latas, preco_por_lata):
    return quantidade_latas * preco_por_lata

quantidade_latas_necessarias = calcular_quantidade_latas(area_a_pintar)

preco_total = calcular_preco_total(quantidade_latas_necessarias, preco_por_lata)


print(f"Quantidade de latas necessárias: {quantidade_latas_necessarias}")
print(f"Preço total: R${preco_total:.2f}")

#----------------------------------------------------------questão 8-----------------------------------------------------

import math
area_a_pintar = float(input("Digite o tamanho da área a ser pintada em metros quadrados: "))

def calcular_latas_18litros(area):
    cobertura_por_lata = 18 * 6  
    quantidade_latas = math.ceil(area / cobertura_por_lata)
    preco_total = quantidade_latas * 80.00
    return quantidade_latas, preco_total


def calcular_galoes_36litros(area):
    cobertura_por_galao = 3.6 * 6  
    quantidade_galoes = math.ceil(area / cobertura_por_galao)
    preco_total = quantidade_galoes * 25.00
    return quantidade_galoes, preco_total

def calcular_combinacao_menor_desperdicio(area):
    cobertura_por_lata = 18 * 6
    cobertura_por_galao = 3.6 * 6
    quantidade_latas = math.ceil(area / cobertura_por_lata)
    
    menor_preco = float('inf')
    melhor_combinacao = None
    
    for num_latas in range(quantidade_latas + 1):
        restante_area = area - num_latas * cobertura_por_lata
        num_galoes = math.ceil(restante_area / cobertura_por_galao)
        
        preco_total = num_latas * 80.00 + num_galoes * 25.00
        if preco_total < menor_preco:
            menor_preco = preco_total
            melhor_combinacao = (num_latas, num_galoes)
    
    return melhor_combinacao, menor_preco


latas_18litros = calcular_latas_18litros(area_a_pintar)
print(f"Situação 1: Comprar apenas latas de 18 litros - Quantidade: {latas_18litros[0]}, Preço: R${latas_18litros[1]:.2f}")

galoes_36litros = calcular_galoes_36litros(area_a_pintar)
print(f"Situação 2: Comprar apenas galões de 3,6 litros - Quantidade: {galoes_36litros[0]}, Preço: R${galoes_36litros[1]:.2f}")

combinacao_menor_desperdicio = calcular_combinacao_menor_desperdicio(area_a_pintar)
print(f"Situação 3: Misturar latas e galões - Quantidade de latas: {combinacao_menor_desperdicio[0][0]}, Quantidade de galões: {combinacao_menor_desperdicio[0][1]}, Preço: R${combinacao_menor_desperdicio[1]:.2f}")

#----------------------------------------------------------questão 9-----------------------------------------------------
numero_binario = input("Digite um número binário: ")

def binario_para_decimal(numero_binario):
    numero_decimal = 0
    expoente = 0

    
    for digito in reversed(numero_binario):
        
        numero_decimal += int(digito) * (2 ** expoente)
        expoente += 1

    return numero_decimal

if set(numero_binario) <= {'0', '1'}:
    resultado_decimal = binario_para_decimal(numero_binario)
    print(f"O número binário {numero_binario} em decimal é {resultado_decimal}.")
else:
    print("Por favor, insira um número binário válido contendo apenas 0s e 1s.")
