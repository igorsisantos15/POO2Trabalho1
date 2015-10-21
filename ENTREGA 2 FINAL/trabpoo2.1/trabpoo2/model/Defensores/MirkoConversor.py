from model.Guerreiro import Guerreiro
from model.Defensores.Defensor import Defensor
from model.Ofensores import Gunte

class MirkoConversor(Defensor):

    def __init__ (self, nome, idade, peso):
        Guerreiro.__init__(self,nome,idade,peso,'China')
        self.tipo = 'MirkoConversor'

    def defender(self, guerreiro, defensores, ofensores, ofensoresAdversarios):

        if guerreiro.getTipo() == "Samurai":
            gunte = Gunte(guerreiro.getNome(), guerreiro.getIdade(), guerreiro.getPeso());
            ofensores.append(gunte)
            ofensoresAdversarios.remove(guerreiro)