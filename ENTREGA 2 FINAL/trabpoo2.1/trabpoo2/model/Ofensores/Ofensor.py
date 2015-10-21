
from model.Guerreiro import Guerreiro

__author__ = 'Italo'


class  Ofensor (Guerreiro):


    def atacar(self, guerreiro, ofensores, defensores, defensoresAdversarios ):
        raise NotImplementedError("Ofensores devem implementar Atacar")
