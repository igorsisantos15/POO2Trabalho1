from model.Defensores.MongeBarrier import MongeBarrier
from model.Defensores.MongeBomb import MongeBomb
from model.Defensores.MongeLeaf import MongeLeaf
from model.util.SuperFabrica import SuperFabrica

class FabricaDefensorIndia(SuperFabrica):

    def criarGuerreiro(self, tipo, nome, idade, peso):

        defensor = None

        if(tipo == 1):
            defensor = MongeLeaf(nome,idade,peso)
        if(tipo == 2):
            defensor = MongeBomb(nome,idade,peso)
        if(tipo == 3):
            defensor = MongeBarrier(nome,idade,peso)

        return defensor
