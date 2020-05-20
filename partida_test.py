from unittest import TestCase
from ahorcado import Partida

class TestComenzarPartida(TestCase):
    def test_partida_solitario(self):
        partida = Partida()
        partida.inicializar()
        palabra = partida.get_palabra()
        self.assertTrue(palabra.isalpha() and len(palabra) > 0)

    def test_arriesgar_letra_correcta(self):
        partida = Partida()
        partida.inicializar()
        palabra = partida.get_palabra()
        resultado = partida.arriesgar(palabra[0])
        self.assertTrue(resultado)
    
    def test_validar_terminado(self):
        partida = Partida()
        partida.inicializar()
        palabra = partida.get_palabra()
        for letra in palabra:
            partida.arriesgar(letra)
        
        terminado = partida.validar_terminado()
        self.assertTrue(terminado)