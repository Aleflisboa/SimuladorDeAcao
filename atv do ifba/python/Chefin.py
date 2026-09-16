class ProdutoAlimenticio:
    def __init__(self, nome, data_validade):
        self.__nome = nome
        self.__data_validade = data_validade

    def calcular_validade(self):

        hoje = self.obter_data_atual()
        dias_restantes = (self.__data_validade - hoje).days
        return dias_restantes

    def esta_estragado(self):
        hoje = self.obter_data_atual()
        return self.__data_validade < hoje

    def obter_data_atual(self):

        return "2023-12-14" 

class Fruta(ProdutoAlimenticio):
    def __init__(self, nome, data_validade, tipo):
        super().__init__(nome, data_validade)
        self.__tipo = tipo

class Carne(ProdutoAlimenticio):
    def __init__(self, nome, data_validade, tipo_corte):
        super().__init__(nome, data_validade)
        self.__tipo_corte = tipo_corte

if __name__ == "__main__":

    banana = Fruta("Banana", "2023-12-31")
    carne_bovina = Carne("Carne Bovina", "2023-12-15", "Filé Mignon")

    print(f"A validade da banana é em {banana.calcular_validade()} dias.")
    print(f"A banana está estragada? {'Sim' if banana.esta_estragado() else 'Não'}")

    print(f"A validade da carne bovina é em {carne_bovina.calcular_validade()} dias.")
    print(f"A carne bovina está estragada? {'Sim' if carne_bovina.esta_estragado() else 'Não'}")

#Second Quest/ Questão 2

class Jogo:
    def __init__(self, nome, dificuldade):
        self.__nome = nome
        self.__dificuldade = dificuldade
        self.__venceu = False

    def jogar(self):
        pass

    def verificar_vitoria(self):
        return self.__venceu

    def __str__(self):
        return f"{self.__nome} - Dificuldade: {self.__dificuldade}"


class JogoAventura(Jogo):
    def __init__(self, nome, dificuldade, missao):
        super().__init__(nome, dificuldade)
        self.__missao = missao

    def jogar(self):
       
       
        print(f"Jogando {self.__nome} - Aventura... Missão: {self.__missao}")
       
        self.__venceu = True


class JogoEstrategia(Jogo):
    def __init__(self, nome, dificuldade, objetivos):
        super().__init__(nome, dificuldade)
        self.__objetivos = objetivos

    def jogar(self):
       
       
        print(f"Jogando {self.__nome} - Estratégia... Objetivos: {self.__objetivos}")
        
        self.__venceu = True



if __name__ == "__main__":
    Hora_de_Aventura = JogoAventura("Aventura Fantástica", "Fácil", "Salvar a princesa")
    Chess = JogoEstrategia("Guerra Tática", "Média", "Conquistar territórios")

    
    Hora_de_Aventura.jogar()
    print(f"{Hora_de_Aventura} - Venceu? {'Sim' if Hora_de_Aventura.verificar_vitoria() else 'Não'}")

    Chess.jogar()
    print(f"{Chess} - Venceu? {'Sim' if Chess.verificar_vitoria() else 'Não'}")


#Third Quest / Questão 3

class Planta:
    def __init__(self, nome, altura, necessidade_agua):
        self.__nome = nome
        self.__altura = altura
        self.__necessidade_agua = necessidade_agua

    def calcular_altura(self):
        return self.__altura

    def precisa_de_agua(self):
        return self.__necessidade_agua

    def regar(self):
 
        pass

    def __str__(self):
        return f"{self.__nome} - Altura: {self.__altura} cm"


class Flor(Planta):
    def __init__(self, nome, altura, necessidade_agua, cor_petala):
        super().__init__(nome, altura, necessidade_agua)
        self.__cor_petala = cor_petala

    def regar(self):
        print(f"Regando a flor {self.__nome} de cor {self.__cor_petala}")
       
        self._Planta__necessidade_agua = False


class Arvore(Planta):
    def __init__(self, nome, altura, necessidade_agua, tipo_folhas):
        super().__init__(nome, altura, necessidade_agua)
        self.__tipo_folhas = tipo_folhas

    def regar(self):
      
        print(f"Regando a árvore {self._Planta__nome} com folhas do tipo {self.__tipo_folhas}")
     
        self._Planta__necessidade_agua = False



if __name__ == "__main__":
    flor_rosa = Flor("Rosa", 30, True, "Vermelha")
    arvore_mangueira = Arvore("Mangueira", 200, True, "Caducas")

    print(f"{flor_rosa} - Precisa de água? {'Sim' if flor_rosa.precisa_de_agua() else 'Não'}")
    print(f"{arvore_mangueira} - Precisa de água? {'Sim' if arvore_mangueira.precisa_de_agua() else 'Não'}")

    flor_rosa.regar()
    arvore_mangueira.regar()

    
    print(f"{flor_rosa} - Precisa de água? {'Sim' if flor_rosa.precisa_de_agua() else 'Não'}")
    print(f"{arvore_mangueira} - Precisa de água? {'Sim' if arvore_mangueira.precisa_de_agua() else 'Não'}")

#Fourth Quest / Questão 4

class Documento:
    def __init__(self, nome, conteudo=""):
        self.__nome = nome
        self.__conteudo = conteudo

    def ler(self):
        return self.__conteudo

    def escrever(self, novo_conteudo):
    
        self.__conteudo = novo_conteudo

    def __str__(self):
        return f"Documento: {self.__nome}"


class DocumentoTexto(Documento):
    def __init__(self, nome, conteudo=""):
        super().__init__(nome, conteudo)

    def escrever(self, novo_conteudo):
    
        print(f"Escrevendo no documento de texto {self._Documento__nome}")
        super().escrever(novo_conteudo)


class DocumentoPlanilha(Documento):
    def __init__(self, nome, conteudo=""):
        super().__init__(nome, conteudo)

    def escrever(self, novo_conteudo):
    
        print(f"Preenchendo a planilha {self._Documento__nome}")
        super().escrever(novo_conteudo)



if __name__ == "__main__":
    doc_texto = DocumentoTexto("DocumentoTexto1", "Conteúdo inicial do documento de texto.")
    doc_planilha = DocumentoPlanilha("Planilha1", "Dados iniciais da planilha.")

    
    print(f"{doc_texto} - Conteúdo: {doc_texto.ler()}")
    print(f"{doc_planilha} - Conteúdo: {doc_planilha.ler()}")

    
    doc_texto.escrever("Novo conteúdo para o documento de texto.")
    doc_planilha.escrever("Atualizando dados na planilha.")

    
    print(f"{doc_texto} - Conteúdo: {doc_texto.ler()}")
    print(f"{doc_planilha} - Conteúdo: {doc_planilha.ler()}")
