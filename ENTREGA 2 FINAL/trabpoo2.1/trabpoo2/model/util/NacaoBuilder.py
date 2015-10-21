__author__ = 'Italo'

class NacaoBuilder(object):


    def criarNacao(self, nome):
        raise NotImplementedError("Criar Nacao")

    def fazerDefensores(self, listDefensores):
        raise NotImplementedError("Criar Guerreiros")

    def fazerOfensores(self, listOfensores):
        raise NotImplementedError("Criar Guerreiros")

    def getNacao(self):
        raise NotImplementedError("Interface")
