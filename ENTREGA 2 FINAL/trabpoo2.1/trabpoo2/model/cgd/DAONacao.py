class DAONacao(object):
    __arquivo1 = 'nacao1.txt'
    __arquivo2 = 'nacao2.txt'

    def getArquivo1(self):
        return self.__arquivo1

    def getArquivo2(self):
        return self.__arquivo2

    def leituraAtacantes(self,arquivo):

        listOfensores = []

        ARQ = open(arquivo, 'r')
        nacao = ARQ.readline()
        linha = ARQ.readline()
        linha = ARQ.readline()
        while (linha != 'Defensores\n'):

                dados = linha.split(' ')
                dados[0] = int(dados[0])
                dados[2] = int(dados[2])
                dados[3] = int(dados[3])
                listOfensores.append(dados)

                linha = ARQ.readline()
        return listOfensores

    def leituraDefensores(self, arquivo):

        listDefensores = []

        ARQ = open(arquivo, 'r')
        nacao = ARQ.readline()
        linha = ARQ.readline()
        linha = ARQ.readline()
        while (linha != 'Defensores\n'):
            linha = ARQ.readline()

        linha = ARQ.readline()
        while linha!= '\n' and linha!= '':

            dados = linha.split(' ')

            dados[0] = int(dados[0])
            dados[2] = int(dados[2])
            dados[3] = int(dados[3])
            listDefensores.append(dados)

            linha = ARQ.readline()

        return listDefensores

    def leituraNome(self, arquivo):

        ARQ = open(arquivo, 'r')
        nacao = ARQ.readline()
        ARQ.close()
        return nacao