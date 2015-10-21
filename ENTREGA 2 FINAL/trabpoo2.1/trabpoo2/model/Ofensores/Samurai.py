from model.Guerreiro import Guerreiro

from model.Ofensores.Ofensor import Ofensor


class Samurai(Ofensor):

    def __init__ (self, nome, idade, peso):
        Guerreiro.__init__(self,nome,idade,peso,'Japao')
        self.tipo = 'Samurai'

    def atacar(self, guerreiro, ofensores, defensores, defensoresAdversarios):

        if not guerreiro.getTipo() == "MirkOConversor":
            guerreiro.setEnergia(guerreiro.getEnergia()-50)