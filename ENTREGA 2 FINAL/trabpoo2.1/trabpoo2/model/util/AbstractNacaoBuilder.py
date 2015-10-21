from model.Nacao import Nacao
from model.util.NacaoBuilder import NacaoBuilder

class AbstractNacaoBuilder(NacaoBuilder):

    nacao = None
    fabricaOfensores = None
    fabricaDefensores = None

    def criarNacao(self, nome):

        self.nacao = Nacao()
        self.nacao.setNome(nome)

    def fazerDefensores(self, listDefensores):

        num = len(listDefensores)
        cont = 0
        dados = []
        listDefensoresProntos = []

        while cont < num:

            dados = listDefensores[cont]

            defensor = self.fabricaDefensores.criarGuerreiro(dados[0], dados[1], dados[2], dados[3])
            listDefensoresProntos.append(defensor)
            cont+=1

        self.nacao.setDefensores(listDefensoresProntos)

    def fazerOfensores(self, listOfensores):

        num = len(listOfensores)
        cont = 0
        dados = []
        listOfensoresProntos = []

        while cont < num:

            dados = listOfensores[cont]
            ofensor = self.fabricaOfensores.criarGuerreiro(dados[0], dados[1], dados[2], dados[3])
            listOfensoresProntos.append(ofensor)
            cont+=1

        self.nacao.setOfensores(listOfensoresProntos)


    def getNacao(self):
        return self.nacao








