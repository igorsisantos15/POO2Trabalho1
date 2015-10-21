from model.util.AbstractNacaoBuilder import AbstractNacaoBuilder
from model.util.FabricaDefensorIndia import FabricaDefensorIndia
from model.util.FabricaOfensorIndia import FabricaOfensorIndia

class BuilderIndia (AbstractNacaoBuilder):

    def __init__(self):

        self.fabricaDefensores = FabricaDefensorIndia()
        self.fabricaOfensores = FabricaOfensorIndia()