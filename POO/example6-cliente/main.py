from classes import Cliente, Endereco

cliente1 = Cliente('João', 32)
cliente1.inserir_endereco('Belo Horizonte', 'MG')
print(f'Cliente: {cliente1.nome}')
cliente1.listar_endereco()
print('------')

cliente2 = Cliente('Maria', 55)
cliente2.inserir_endereco('Salvador', 'BA')
cliente2.inserir_endereco('Rio de Janeiro', 'RJ')
print(f'Cliente: {cliente2.nome}')
cliente2.listar_endereco()
del cliente2
print('------')
cliente3 = Cliente('Luiz', 41)
cliente3.inserir_endereco('São Paulo', 'SP')
print(f'Cliente: {cliente3.nome}')
cliente3.listar_endereco()
print('###########')
