from classes import CarrinhoDeCompras, Produto

carrinho = CarrinhoDeCompras()

p1 = Produto('Pão', 5)
p2 = Produto('Queijo', 15)
p3 = Produto('Carne', 70)

carrinho.inserir_produto(p1)
carrinho.inserir_produto(p2)
carrinho.inserir_produto(p3)

carrinho.listar_produtos()

print(carrinho.soma_total())
