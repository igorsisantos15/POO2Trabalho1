from model.Guerreiro import Guerreiro
from model.Ofensores.Ninja import Ninja
from model.Defensores.Defensor import Defensor

class TanTan(Defensor):

    def __init__ (self, nome, idade, peso):
        Guerreiro.__init__(self,nome,idade,peso,'Japao')
        self.tipo = 'Tantan'

    def defender(self, guerreiro, defensores, ofensores, ofensoresAdversarios):
        energia = self.getEnergia()

        if energia <=0:
            ninja = Ninja(self.nome,self.idade,self.peso)
            ofensores.append(ninja)


