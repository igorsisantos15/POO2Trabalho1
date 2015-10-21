from model.Ofensores.Chunku import Chunku
from model.Ofensores.Gunte import Gunte
from model.Ofensores.Noktu import Noktu
from model.util.SuperFabrica import SuperFabrica

class FabricaOfensorChina(SuperFabrica):

    def criarGuerreiro(self, tipo, nome, idade, peso):

        ofensor = None

        if(tipo == 1):
            ofensor = Chunku(nome,idade,peso)
        if(tipo == 2):
            ofensor = Gunte(nome,idade,peso)
        if(tipo == 3):
            ofensor = Noktu(nome,idade,peso)

        return ofensor