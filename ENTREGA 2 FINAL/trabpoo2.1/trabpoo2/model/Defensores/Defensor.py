from model.Guerreiro import Guerreiro

class Defensor (Guerreiro):

    def defender(self, guerreiro, defensores, ofensores, ofensoresAdversarios):
        raise NotImplementedError("Defensores devem implementar Defender")
