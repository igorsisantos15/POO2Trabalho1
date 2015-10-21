from model.Guerreiro import Guerreiro
from model.Defensores.Defensor import Defensor

class MongeLeaf(Defensor):

    def __init__ (self, nome, idade, peso):
        Guerreiro.__init__(self,nome,idade,peso,'India')
        self.tipo = 'MongeLeaf'

    def defender(self, guerreiro, defensores, ofensores, ofensoresAdversarios):
        if guerreiro.getTipo() == "Ninja":
            self.setEnergia(self.getEnergia()+ 20)
            guerreiro.setEnergia(guerreiro.getEnergia()-1)
        if guerreiro.getTipo() == "Chunku":
            self.setEnergia(self.getEnergia()+ 5)
            guerreiro.setEnergia(guerreiro.getEnergia()-1)

