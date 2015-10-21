from model.Guerreiro import Guerreiro
from model.Defensores.Defensor import Defensor

class MongeBomb(Defensor):

    def __init__ (self, nome, idade, peso):
        Guerreiro.__init__(self,nome,idade,peso,'India')
        self.tipo = 'MongeBomb'

    def defender(self, guerreiro, defensores, ofensores, ofensoresAdversarios):
        guerreiro.setEnergia(1)

