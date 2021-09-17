class BaseDeDados:
    def __init__(self):
        self.__dados = {}

    @property
    def dados(self):
        return self.__dados

    def inserir_cliente(self, id, nome):
        if 'clientes' not in self.__dados:
            self.__dados['clientes'] = {id: nome}
        else:
            self.__dados['clientes'].update({id: nome})

    def listar_clientes(self):
        for id, nome in self.__dados['clientes'].items():
            print(id, nome)

    def apagar_clientes(self, id):
        del self.__dados['clientes'][id]


base = BaseDeDados()

base.inserir_cliente(1, 'Maria')
base.inserir_cliente(2, 'Julia')
base.inserir_cliente(3, 'John')

base.listar_clientes()
base.apagar_clientes(2)

print('-------------')
base.listar_clientes()
