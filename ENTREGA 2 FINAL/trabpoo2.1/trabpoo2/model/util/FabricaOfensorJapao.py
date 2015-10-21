from model.Ofensores.Ninja import Ninja
from model.Ofensores.Samurai import Samurai
from model.util.SuperFabrica import SuperFabrica

__author__ = 'Italo'


class FabricaOfensorJapao(SuperFabrica):

    def criarGuerreiro(self, tipo, nome, idade, peso):

        ofensor = None

        if(tipo == 1):
            ofensor = Samurai(nome,idade,peso)
        if(tipo == 2):
            ofensor = Ninja(nome,idade,peso)

        return ofensor