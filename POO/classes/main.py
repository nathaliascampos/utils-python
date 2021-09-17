from classes import Escritor, Caneta, MaquinaDeEscrever

caneta = Caneta('Bic')
maquina = MaquinaDeEscrever()
escritor = Escritor('Izzie')

escritor.ferramenta = maquina
escritor.ferramenta.escrever()
