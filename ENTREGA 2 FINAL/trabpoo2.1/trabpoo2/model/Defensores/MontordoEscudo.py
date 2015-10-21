from model.Guerreiro import Guerreiro
from model.Defensores.Defensor import Defensor

class MontordoEscudo(Defensor):

    def __init__ (self, nome, idade, peso):
        Guerreiro.__init__(self,nome,idade,peso,'China')
        self.tipo = 'MontordoEscudo'
        self.setEnergia(150)

    def defender(self, guerreiro, defensores, ofensores, ofensoresAdversarios):
        guerreiro.setEnergia(0)