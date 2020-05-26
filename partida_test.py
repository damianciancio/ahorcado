from unittest import TestCase
from ahorcado import Partida

class TestComenzarPartida(TestCase):
    def test_partida_solitario(self):
        partida = Partida()
        palabra = "hola"
        partida.inicializar(palabra)
        self.assertEqual(palabra, partida.get_palabra())


    def test_arriesgar_letra_correcta(self):
        partida = Partida()
        palabra = "hola"
        partida.inicializar(palabra)
        resultado = partida.arriesgar("o")
        self.assertTrue(resultado)

    def test_arriesgar_letra_incorrecta(self):
        partida = Partida()
        palabra = "hola"
        partida.inicializar(palabra)
        resultado = partida.arriesgar("p")
        self.assertFalse(resultado)
    
    def test_validar_terminado(self):
        partida = Partida()
        palabra = "hola"
        partida.inicializar(palabra)
        for letra in palabra:
            self.assertFalse(partida.validar_terminado())
            partida.arriesgar(letra)
        
        terminado = partida.validar_terminado()
        self.assertTrue(terminado)

    def test_longitud_palabra(self):
        partida = Partida()
        partida.inicializar('hola')
        resultado = partida.get_longitud_palabra()
        self.assertEquals(resultado, 4)

    def test_seleccionar_palabra(self):
        partida = Partida()
        partida.inicializar()
        resultado = partida.get_seleccionar_palabra()
        self.assertIsNotNone(resultado)

    def test_intentos_restantes(self):
        partida = Partida()
        partida.inicializar('pelota')
        partida.arriesgar('h')
        resultado = partida.get_intentos_restantes()
        self.assertEquals(resultado, 6)