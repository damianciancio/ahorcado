import random

class Partida():

    def get_dict(self):
        dictionary = {
            "palabra": self.palabra,
            "resultado": self.resultado,
            "intentos_restantes": self.intentos_restantes,
            "letras_acertadas": self.letras_acertadas,
            "letras_rechazadas": self.letras_rechazadas,
            "progreso_palabra": self.get_progreso_palabra()
        }
        return dictionary

    def create_from_dictionary(self, dictionary):
        self.palabra = dictionary['palabra']
        self.resultado = dictionary['resultado']
        self.intentos_restantes = dictionary['intentos_restantes']
        self.letras_acertadas = dictionary['letras_acertadas']
        self.letras_rechazadas = dictionary['letras_rechazadas']
        self.progreso_palabra = dictionary['progreso_palabra']
    
    def inicializar(self, palabra=None):
        if palabra == None:
            self.palabra = self.get_seleccionar_palabra()
        else:
            self.palabra = palabra
        self.resultado = None
        self.intentos_restantes = 7
        self.letras_acertadas = []
        self.letras_rechazadas = []
        self.progreso_palabra = ''

    def get_progreso_palabra(self):
        progreso = []
        self.progreso_palabra = ''
        for i in range(int(self.get_longitud_palabra())):
            if (self.palabra[i] in self.letras_acertadas):
                progreso.append(self.palabra[i])
            else: 
                progreso.append('_')
            progreso.append(' ')
        for p in progreso:
            self.progreso_palabra += p
        return self.progreso_palabra

    def get_letras_rechazadas_html(self):
        lista_letras = []
        for letra in self.letras_rechazadas:
            lista_letras.append(letra + ' - ')
        return ''.join([str(letra) for letra in lista_letras]) 

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

        if len(letra) > 1:
            acierto = self.arriesgar_palabra(letra)
        else:
            acierto = self.arriesgar_letra(letra)
        if acierto==False:
            self.intentos_restantes = self.intentos_restantes - 1 
            self.letras_rechazadas.append(letra)
        else:
            self.letras_acertadas.append(letra)
        return acierto

    def arriesgar_letra(self, letra):
        acierto = False
        if (letra in self.get_palabra()) and (letra not in self.letras_acertadas):
                acierto = True
        return acierto

    def comenzar_partida(self):
        print("La longitud de la palabra es: " + str(self.get_longitud_palabra()))
        while not self.validar_terminado():
            print("Te quedan " + str(self.get_intentos_restantes()) + " intentos restantes")
            letra = self.solicitar_letra()
            if self.arriesgar(letra):
                print("Muy bien!")
            else:
                print("Fallaste!")

        if self.validar_si_gano():
            print("Ganaste! la palabra era " + self.get_palabra())
        else: 
            print("Perdiste.. la palabra era " + self.get_palabra())

    def solicitar_letra(self):
        print("Ingrese una o arriesgue una palabra: ")
        return str(input())

    def validar_si_gano(self):
        for acertada in self.letras_acertadas:
            if acertada == self.get_palabra():
                return True
        for letra in self.get_palabra():
            if letra not in self.letras_acertadas:
                return False
        if (len(self.letras_acertadas) == 0):
            return False
        return True

    def validar_terminado(self):
        if self.validar_si_gano():
            return 'gano'
        if self.intentos_restantes == 0:
            return 'perdio'
        return False

    def arriesgar_palabra(self, palabra):
        if self.get_palabra() == palabra:
            return True
        else:
            return False
