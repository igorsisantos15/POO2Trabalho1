from model.util.AbstractNacaoBuilder import AbstractNacaoBuilder
from model.util.FabricaDefensorChina import FabricaDefensorChina
from model.util.FabricaOfensorChina import FabricaOfensorChina

class BuilderChina (AbstractNacaoBuilder):

    def __init__(self):

        self.fabricaOfensores = FabricaOfensorChina()
        self.fabricaDefensores = FabricaDefensorChina()