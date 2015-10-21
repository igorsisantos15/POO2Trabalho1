# coding=utf-8
from model.Batalha import Batalha
from model.Defensores.MangaldeDefesa import MangaldeDefesa
from model.Defensores.TanTan import TanTan
from model.Nacao import Nacao
from model.Ofensores.Chunku import Chunku
from model.Ofensores.Samurai import Samurai
from model.cgd.DAONacao import DAONacao
from model.util.FabricaDefensorChina import FabricaDefensorChina
from model.util.FabricaNacaoMagic import FabricaNacaoMagic




class Testes(object):

    def verificar_objeto(self):

        fabrica = FabricaDefensorChina()
        defensor = fabrica.criarGuerreiro(1, 'paulo', 50, 50)
        resultado = type(MangaldeDefesa('paulo', 50, 50))

        if type(defensor) == resultado:
            print 'True'



    def verificar_builder(self):
        arquivoleitura = 'nacao1.txt'

        resultado = 'Japao\n'
        fabrica = FabricaNacaoMagic()
        nacao = fabrica.produzirNacao(arquivoleitura)
        if nacao.getNome() == resultado:
            print 'True'


    def verificar_leitura_correta(self):

        arquivoleitura = 'nacao1.txt'
        resultadoOfensores = 4
        resultadoDefensores = 2

        daoNacao = DAONacao()
        ofensores = daoNacao.leituraAtacantes(arquivoleitura)
        defensores = daoNacao.leituraDefensores(arquivoleitura)

        if(len(ofensores) == resultadoOfensores and len(defensores) == resultadoDefensores):
            print 'True'


    def verificar_nacao_atacante(self):
        nacaoAtacante = Nacao()
        nacaoDefensora = Nacao()

        resultado = 'paulo'

        nacaoAtacante.setNome('China\n')
        nacaoDefensora.setNome('Japao\n')
        ofensorAtaque = [(Chunku('paulo',24,66)), (Chunku('alberto',30,20))]
        OfensorDefesa = [(MangaldeDefesa('Matheus',24,66)), (MangaldeDefesa('Viadins',30,20))]
        nacaoAtacante.setOfensores(ofensorAtaque)
        nacaoAtacante.setDefensores(OfensorDefesa)

        defensorAtaque = [(Samurai('Gustavao',24,66)), (Samurai('Otario',30,20))]
        defensorDefesa = [(TanTan('paulo',24,66)), (TanTan('alberto',30,20))]

        nacaoDefensora.setOfensores(defensorAtaque)
        nacaoDefensora.setDefensores(defensorDefesa)

        batalha = Batalha()
        batalha.setParamentros(nacaoAtacante,nacaoDefensora)

        if batalha.ofensor.getNome() == resultado:
            print 'True'


    def verificarLutar(self):

        nacaoAtacante = Nacao()
        nacaoDefensora = Nacao()

        resultado = 0

        nacaoAtacante.setNome('China\n')
        nacaoDefensora.setNome('Japao\n')
        ofensorAtaque = [(Chunku('paulo',24,66))]
        OfensorDefesa = [(MangaldeDefesa('Matheus',24,66))]
        nacaoAtacante.setOfensores(ofensorAtaque)
        nacaoAtacante.setDefensores(OfensorDefesa)

        defensorAtaque = [(Samurai('Gustavao',24,66))]
        defensorDefesa = [(TanTan('paulo',24,66))]

        nacaoDefensora.setOfensores(defensorAtaque)
        nacaoDefensora.setDefensores(defensorDefesa)

        batalha = Batalha()
        batalha.setParamentros(nacaoAtacante,nacaoDefensora)
        batalha.lutar()

        if nacaoAtacante.sizeDefensores() == resultado or nacaoDefensora.sizeDefensores() == resultado:
            print 'True'





