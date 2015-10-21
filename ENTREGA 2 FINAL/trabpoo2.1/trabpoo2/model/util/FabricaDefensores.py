from model.util.FabricaDefensorChina import FabricaDefensorChina
from model.util.FabricaDefensorIndia import FabricaDefensorIndia
from model.util.FabricaDefensorJapao import FabricaDefensorJapao

class FabricaDefensores():

    def criarDefensores(self, nomeNacao, tipo, nome, idade, peso):

        fabrica = None;

        if(nomeNacao == 'China\n'):
            fabrica = FabricaDefensorChina()
        elif(nomeNacao == 'India\n'):
            fabrica = FabricaDefensorIndia()
        elif(nomeNacao == 'Japao\n'):
            fabrica = FabricaDefensorJapao()

        return fabrica.criarGuerreiro(tipo, nome, idade, peso)
