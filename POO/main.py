from pessoa import Pessoa

# p1 = Pessoa('Luiz', 29)

# p1.comer('maça')
# p1.falar('POO')
# p1.comer('maça')
# p1.parar_de_comer()
# p1.parar_de_comer()
# p1.parar_de_falar()
# p1.falar('POO')
# p1.comer('pera')
# p1.parar_de_falar()
# p1.comer('pera')


p1 = Pessoa.por_ano_nascimento("Maria", 1987)
print(p1.nome, p1.idade)
print(p1.get_ano_nascimento())

print(p1.gera_id())
