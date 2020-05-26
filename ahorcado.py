import random

class Partida():
    def __init__(self):
        pass
    
    def inicializar(self, palabra=None):
        if palabra == None:
            self.palabra = self.get_seleccionar_palabra()
        else:
            self.palabra = palabra
        self.resultado = None
        self.intentos_restantes = 7
        self.letras_acertadas = []
        #self.letras_rechazadas = []

    def get_palabra(self):
        palabra = self.palabra
        return palabra

    def get_longitud_palabra(self):
        longitud = len(self.get_palabra())
        return longitud 

    def get_seleccionar_palabra(self):
        lista_palabras = ['mate', 'pelota', 'vaso', 'computadora', 'remera', 'teclado', 'libro']
        palabra_seleccionada = random.choice(lista_palabras)
        return palabra_seleccionada

    def get_intentos_restantes(self):
        return self.intentos_restantes

    def arriesgar(self, letra):
        acierto = False
        if letra in self.get_palabra():
            if not letra in self.letras_acertadas:
                self.letras_acertadas.append(letra)
            acierto = True
        else:
            self.intentos_restantes = self.intentos_restantes - 1
            #self.letras_acertadas.append(letra)
        return acierto

    def comenzar_partida(self):
        while self.resultado == None and self.intentos_restantes != 0:
            letra = self.solicitar_letra()
            if self.arriesgar(letra):
                print "Muy bien!"
            else:
                print "Fallaste!"
            self.validar_terminado()

        if self.resultado:
            print "Ganaste! la palabra era " + self.get_palabra()
        else: 
            print "Perdiste.. la palabra era " + self.get_palabra()

    def solicitar_letra(self):
        print "Ingrese una letra: "
        return str(input())

    def validar_terminado(self):
        for letra in self.get_palabra():
            if letra not in self.letras_acertadas:
                self.resultado = False
                return self.resultado
        self.resultado = True
        return self.resultado

