from model.Guerreiro import Guerreiro
from model.Defensores import MangaldeDefesa
from model.Ofensores.Ofensor import Ofensor


class Noktu(Ofensor):

    def __init__ (self, nome, idade, peso):
        Guerreiro.__init__(self,nome,idade,peso,'China')
        self.tipo = 'Noktu'

    def atacar(self, guerreiro, ofensores, defensores, defensoresAdversarios):
        guerreiro.setEnergia(guerreiro.getEnergia()-5)
        nome = "MangalGerado" + self.__sobrenome
        self.__parteNome = self.__parteNome + 1
        self.__sobrenome = self.__parteNome
        self.__nome = self.__nome + self.__sobrenome
        __idade = 30
        __peso = 90
        mangaldeDefesa = MangaldeDefesa(nome,self.__idade,self.__peso)
        defensores.add(mangaldeDefesa)



