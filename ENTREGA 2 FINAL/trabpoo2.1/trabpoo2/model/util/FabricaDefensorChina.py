from model.Defensores.MangaldeDefesa import MangaldeDefesa
from model.Defensores.MirkoConversor import MirkoConversor
from model.Defensores.MontordoEscudo import MontordoEscudo
from model.util.SuperFabrica import SuperFabrica

class FabricaDefensorChina(SuperFabrica):

    def criarGuerreiro(self, tipo, nome, idade, peso):

        defensor = None

        if(tipo == 1):
            defensor = MangaldeDefesa(nome,idade,peso)
        if(tipo == 2):
            defensor = MontordoEscudo(nome,idade,peso)
        if(tipo == 3):
            defensor = MirkoConversor(nome,idade,peso)

        return defensor