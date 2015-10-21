from model.Guerreiro import Guerreiro
from model.Defensores.Defensor import Defensor

class MongeBarrier(Defensor):
    __sobrenome = None
    __parteNome = None
    __meiaEnergia = None
    def __init__ (self, nome, idade, peso):
        Guerreiro.__init__(self,nome,idade,peso,'India')
        self.tipo = 'MongeBarrier'
        self.__parteNome = None
        self.__nivelEnergetico = 100

    def getParteNome(self):
        return self.__parteNome

    def setParteNome(self,parteNome):
        self.__parteNome = parteNome

    def getNivelEnergetico(self):
        return self.__nivelEnergetico

    def setNivelEnergetico(self,nivelEnergetico):
        self.__nivelEnergetico = nivelEnergetico

    def defender(self, guerreiro, defensores, ofensores, ofensoresAdversarios):

        if (self.getEnergia() <= 0) and (self.getNivelEnergetico() != 1):
            self.__meiaEnergia = self.__nivelEnergetico /2
            for i in range(2):
                nome = "MongeBarrierGerado" + self.__sobrenome
                self.__parteNome = self.__parteNome + 1
                self.__sobrenome = self.__parteNome
                self.__nome = self.__nome + self.__sobrenome
                mongeBarrier = MongeBarrier(nome,self.idade, self.peso)
                mongeBarrier.setNivelEnergetico(self.__meiaEnergia)
                defensores.append(mongeBarrier)

