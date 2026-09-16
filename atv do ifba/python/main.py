#explica se quiser man, vai na fé(carinha feliz com sinal de legal)

from YASUKE import carrinho_de_compras, produto

carrinho = carrinho_de_compras()

p1 = produto("Play Station 5", 9000)
p2 = produto("iphone", 5900)
p3 = produto("Corrente LV", 100000)

carrinho.inserir_produto(p1)
carrinho.inserir_produto(p2)
carrinho.inserir_produto(p3)
carrinho.inserir_produto(p1)

carrinho.lista_produto()
print("O valor estimado da sua compra é de: ", carrinho.soma_total())