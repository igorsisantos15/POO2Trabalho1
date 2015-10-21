__author__ = 'Italo'



class Nacao(object):
    __nome = None
    __ofensores = []
    __defensores = []


    def setOfensores(self, ofensores):
        self.__ofensores = ofensores

    def setDefensores(self, defensores):
        self.__defensores = defensores

    def setNome(self, nome):
        self.__nome = nome

    def getNome(self):
        return self.__nome

    def getOfensores(self):
        return self.__ofensores

    def getDefensores(self):
        return self.__defensores

    def getLutador(self):
        lutador = self.__ofensores[0]
        self.__ofensores.remove(lutador)
        return lutador

    def getDefensor(self):
        defensor = self.__defensores[0]
        self.__defensores.remove(defensor)
        return defensor

    def retornarLutador(self, lutador):
        self.__ofensores.append(lutador)

    def retornarDefensor(self,defensor):
        self.__defensores(defensor)

    def sizeOfensor(self):
        return len(self.__ofensores)

    def sizeDefensores(self):
        return len(self.__defensores)

    def adcionarOfensor(self, ofensor):
        self.__ofensores.append(ofensor)

    def adcionarDefensor(self, defensor):
        self.__defensores.append(defensor)

