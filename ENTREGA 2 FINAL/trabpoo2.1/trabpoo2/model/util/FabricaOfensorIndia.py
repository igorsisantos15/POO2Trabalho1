from model.Ofensores.Seak import Seak
from model.util.SuperFabrica import SuperFabrica

class FabricaOfensorIndia(SuperFabrica):

    def criarGuerreiro(self, tipo, nome, idade, peso):

        ofensor = None

        if(tipo == 1):
            ofensor = Seak(nome,idade,peso)

        return ofensor