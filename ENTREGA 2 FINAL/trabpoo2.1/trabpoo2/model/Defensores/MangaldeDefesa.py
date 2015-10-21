from model.Guerreiro import Guerreiro
from model.Defensores.Defensor import Defensor

class MangaldeDefesa(Defensor):

    def __init__ (self, nome, idade, peso):
        Guerreiro.__init__(self,nome,idade,peso,'China')
        self.tipo = 'MangaldeDefesa'

    def defender(self, guerreiro, defensores, ofensores, ofensoresAdversarios):
        guerreiro.setEnergia(guerreiro.getEnergia()-2)



