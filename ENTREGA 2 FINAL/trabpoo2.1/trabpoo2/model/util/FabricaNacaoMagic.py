from model.cgd.DAONacao import DAONacao
from model.util.BuilderChina import BuilderChina
from model.util.BuilderIndia import BuilderIndia
from model.util.BuilderJapao import BuilderJapao
from model.util.Deus import Deus

class FabricaNacaoMagic(object):

    builders = {}
    __instance = None

    def __init__(self):

        self.builders = dict ([('China\n',BuilderChina()),('Japao\n',BuilderJapao()),('India\n',BuilderIndia())])

    def produzirNacao(self, arquivo):

        daoNacao = DAONacao()
        listOfensores = daoNacao.leituraAtacantes(arquivo)
        listDefensores = daoNacao.leituraDefensores(arquivo)
        nome = daoNacao.leituraNome(arquivo)
        deus = Deus()
        builder = self.builders[nome]
        nacao = deus.criarNacao(builder,nome,listDefensores,listOfensores)

        return nacao

    @staticmethod
    def getInstance():
        if not FabricaNacaoMagic.__instance:
            FabricaNacaoMagic.__instance = FabricaNacaoMagic()
        return FabricaNacaoMagic.__instance



