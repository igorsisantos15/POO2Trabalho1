from model.util.AbstractNacaoBuilder import AbstractNacaoBuilder
from model.util.FabricaDefensorJapao import FabricaDefensorJapao
from model.util.FabricaOfensorJapao import FabricaOfensorJapao

class BuilderJapao (AbstractNacaoBuilder):

    def __init__(self):

        self.fabricaDefensores = FabricaDefensorJapao()
        self.fabricaOfensores = FabricaOfensorJapao()