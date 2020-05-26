class Partida():
    def __init__(self):
        pass
    
    def inicializar(self, palabra=None):
        if palabra == None:
            self.palabra = "hola"
        else:
            self.palabra = palabra
        self.resultado = None
        self.intentos_restantes = 7
        self.letras_acertadas = []
        #self.letras_rechazadas = []

    def get_palabra(self):
        palabra = self.palabra
        return palabra

    def arriesgar(self, letra):
        if len(letra) > 1:
            acierto = self.arriesgar_palabra(letra)
        else:
            acierto = self.arriesgar_letra(letra)
        if not acierto:
            self.intentos_restantes = self.intentos_restantes - 1
            #self.letras_acertadas.append(letra)
        else:
            self.letras_acertadas.append(letra)
        return acierto

    def arriesgar_letra(self, letra):
        acierto = False
        if letra in self.get_palabra():
            if not letra in self.letras_acertadas:
                acierto = True
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
        print "Ingrese una o arriesgue una palabra: "
        return str(input())

    def validar_terminado(self):
        for acertada in self.letras_acertadas:
            if acertada == self.get_palabra():
                self.resultado = True
                return True
        for letra in self.get_palabra():
            if letra not in self.letras_acertadas:
                self.resultado = False
                return self.resultado
        self.resultado = True
        return self.resultado

    def arriesgar_palabra(self, palabra):
        if self.get_palabra() == palabra:
            return True
        else:
            return False