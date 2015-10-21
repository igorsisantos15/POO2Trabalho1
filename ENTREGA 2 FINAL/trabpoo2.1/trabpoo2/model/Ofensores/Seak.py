from model.Guerreiro import Guerreiro

from model.Ofensores.Ofensor import Ofensor


class Seak(Ofensor):

    def __init__ (self, nome, idade, peso):
        Guerreiro.__init__(self,nome,idade,peso,'India')
        self.tipo = 'Seak'

    def atacar(self, guerreiro, ofensores, defensores, defensoresAdversarios):
        guerreiro.setEnergia(guerreiro.getEnergia()-25)

