class Partida():
    def __init__(self):
        pass
    
    def inicializar(self):
        self.palabra = "hola"
        self.resultado = None
        self.intentos_restantes = 7
        self.letras_acertadas = []
        #self.letras_rechazadas = []

    def get_palabra(self):
        return self.palabra

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
        if len(self.get_palabra()) == len(self.letras_acertadas):
            self.resultado = True
        return self.resultado
        
partida = Partida()
partida.inicializar()
partida.comenzar_partida()

    