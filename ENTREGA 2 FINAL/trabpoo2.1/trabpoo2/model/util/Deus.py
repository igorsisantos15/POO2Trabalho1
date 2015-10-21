from model.util.Director import Director

class Deus(Director):

    def criarNacao(self, ajudante, nome, listDefensores, listOfensores):

        ajudante.criarNacao(nome)
        ajudante.fazerDefensores(listDefensores)
        ajudante.fazerOfensores(listOfensores)

        return ajudante.getNacao()