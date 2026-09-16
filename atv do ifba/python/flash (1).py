#composição, a variavel "senha" tem dependecia da classe cofre

class cofre:
    senha = ""
     

    def __init__(self ,senha):
      self.senha = senha

    def verificar_senha(nova_senha):
        if len(nova_senha)> 6:
            return True
        else:
            return False


senha = input("digite a senha: ")

if cofre.verificar_senha(senha):
    alefCofre = cofre(senha)
    print('senha criada')
else:
    print('senha inválida')

print(alefCofre.senha)

