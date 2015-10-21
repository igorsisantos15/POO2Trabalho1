__author__ = 'Italo'


class Guerreiro (object):
    __nome = None
    __idade = None
    __peso = None
    __energia = 100
    __tipo = None
    __nacao = None

    def __init__(self, nome, idade, peso, nacao):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.__nacao = nacao

    def getNome(self):
        return self.nome

    def setNome(self, nome):
         self.nome = nome

    def getIdade(self):
        return self.idade

    def setIdade(self, idade):
         self.idade = idade

    def getPeso(self):
        return self.peso

    def setPeso(self, peso):
         self.peso = peso

    def getEnergia(self):
        return self.__energia

    def setEnergia(self, energia):
         self.__energia = energia

    def getTipo(self):
        return self.tipo

    def setTipo(self, tipo):
         self.tipo = tipo

    def getNomeNacao(self):
        return self.__nacao







