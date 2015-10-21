from model.Batalha import Batalha

class CtrlBatalha(object):

    def iniciarBatalha(self):

        batalha = Batalha()
        batalha.carregar()
        batalha.lutar()
        batalha.gerarResultados()