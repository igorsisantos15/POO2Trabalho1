from random import randint
from model.cgd.DAONacao import DAONacao
from model.Nacao import Nacao
from model.util.FabricaNacaoMagic import FabricaNacaoMagic
from view.Telabatalha import TelaBatalha

class Batalha(object):

    __nacao1 = Nacao()
    __nacao2 = Nacao()
    nacaoAtaque = None
    ofensor = None
    ofensoresAtacantes = None
    defensoresAtacantes = None
    ofesoresDefesa = None
    defensoresDefesa = None
    defensor = None

    def carregar(self):

        daoNacao = DAONacao()

        arq1 = daoNacao.getArquivo1()
        arq2 = daoNacao.getArquivo2()

        fabrica = FabricaNacaoMagic.getInstance()
        self.__nacao1 = fabrica.produzirNacao(arq1)
        self.__nacao2 = fabrica.produzirNacao(arq2)

    def setParamentros(self,nacaoAtaque, nacaoDefesa):

        self.nacaoAtaque = nacaoAtaque
        self.ofensor = nacaoAtaque.getLutador()
        self.ofensoresAtacantes = nacaoAtaque.getOfensores()
        self.defensoresAtacantes = nacaoAtaque.getDefensores()
        self.ofesoresDefesa = nacaoDefesa.getOfensores()
        self.defensoresDefesa = nacaoDefesa.getDefensores()
        self.defensor = nacaoDefesa.getDefensor()

    def lutar(self):

        vezAtaque = randint(1,2)

        while self.__nacao1.sizeOfensor()!= 0 and self.__nacao1.sizeDefensores()!=0 and self.__nacao2.sizeOfensor()!=0 and self.__nacao2.sizeDefensores()!=0:

            if vezAtaque == 1:

                self.setParamentros(self.__nacao1,self.__nacao2)
                proxAtaque = 2

            else:

                self.setParamentros(self.__nacao2,self.__nacao1)
                proxAtaque = 1

            while self.defensor.getEnergia() > 0 and len(self.ofensoresAtacantes) > 0:
                self.ofensor.atacar(self.defensor,self.ofensoresAtacantes,self.defensoresAtacantes,self.defensoresDefesa)
                self.defensor.defender(self.ofensor,self.defensoresDefesa,self.ofesoresDefesa,self.ofensoresAtacantes)

                if self.ofensor.getEnergia() > 0:
                    self.nacaoAtaque.adcionarOfensor(self.ofensor)

                self.ofensor = self.nacaoAtaque.getLutador()

            vezAtaque = proxAtaque

    def gerarResultados(self):

        tela = TelaBatalha()
        empate = 0


        if self.__nacao1.sizeOfensor() == 0 and self.__nacao2.sizeDefensores() == 0 or self.__nacao2.sizeOfensor() == 0 and self.__nacao1.sizeDefensores() == 0:
            tela.menssagem("EMPATE - A PAZ REINOU")

            empate = 1


        if self.__nacao1.sizeOfensor() == 0 and empate == 0:

            tela.menssagem("A nacao vencedora foi: %s" %self.__nacao2.getNome())
            tela.menssagem("A nacao perdedora foi %s" %self.__nacao1.getNome())
            tela.menssagem("Acabaram os guerreiros ofensores da nacao 1")

        if self.__nacao1.sizeDefensores() == 0 and empate == 0:
            tela.menssagem("A nacao vencedora foi: %s" %self.__nacao2.getNome())
            tela.menssagem("A nacao perdedora foi: %s"%self.__nacao1.getNome())
            tela.menssagem("Acabaram os guerreiros defensores da nacao 1")

        if self.__nacao2.sizeOfensor == 0 and empate == 0:
            tela.menssagem("A nacao vencedora foi: %s" %self.__nacao1.getNome())
            tela.menssagem("A nacao perdedora foi: %s"  %self.__nacao2.getNome())
            tela.menssagem("Acabaram os guerreiros ofensores da nacao 2")

        if self.__nacao2.sizeDefensores() == 0 and empate == 0:
            tela.menssagem("A nacao vencedora foi: %s" %self.__nacao1.getNome())
            tela.menssagem("A nacao perdedora foi: %s"  %self.__nacao2.getNome())
            tela.menssagem("Acabaram os guerreiros defensores da nacao2")