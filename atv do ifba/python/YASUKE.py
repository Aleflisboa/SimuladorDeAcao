class carrinho_de_compras: #Aqui vemos um class carrinho. A class carrinho pode exister sem a classe produto
    def __init__(self):
        self.produtos = [] #Na agregação as informação da class produto, compoem na class carrinho
    
    def inserir_produto(self, produto):
        self.produtos.append(produto)
    
    def lista_produto(self):
        for produto in self.produtos:
            print(produto.nome, produto.valor)
            
    def soma_total(self):
        total = 0
        for produto in self.produtos:
            total += produto.valor
        return total

class produto: #classe Produto
    def __init__(self, nome, valor):
        self.nome = nome
        self.valor = valor