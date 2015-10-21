from model.Defensores.TanTan import TanTan
from model.util.SuperFabrica import SuperFabrica


class FabricaDefensorJapao(SuperFabrica):

    def criarGuerreiro(self, tipo, nome, idade, peso):

        defensor = None

        if(tipo == 1):
            defensor = TanTan(nome,idade,peso)

        return defensor