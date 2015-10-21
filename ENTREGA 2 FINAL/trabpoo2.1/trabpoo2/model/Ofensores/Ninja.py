from model.Guerreiro import Guerreiro
from model.Ofensores.Ofensor import Ofensor

class Ninja(Ofensor):

    def __init__ (self, nome, idade, peso):
        Guerreiro.__init__(self,nome,idade,peso,'Japao')
        self.tipo = 'Ninja'

    def atacar(self, guerreiro, ofensores, defensores, defensoresAdversarios):
        guerreiro.setEnergia(guerreiro.getEnergia()-20)
