class Coche():

    def __init__(self):      #Constructor = define un estado inicial
        self.pesoInicial = 1000            #Como va sin __ se puede modificar luego
        self.__altura = 2        #self.__ sirve para encapsular y no poder cambiar este parametro luego

    largoChasis = 250       #propiedades
    anchoChasis = 120
    ruedas = 4                #Las propiedades tambien se pueden definir como estado inicial
    enmarcha = False

    def arrancar(self, arrancamos):     #Funcionamiento (metodo), self=this en otros lenguajes
        self.enmarcha = arrancamos          ##Self enmarcha es igual a arrancamos (False/True) que le hemos pasado a la función
        if(self.enmarcha):              #Es igual que poner if(self.enmarcha=true)
                return "El coche esta en marcha"
        else:
            return "Esta parado"
        self.enmarcha = True
    def estado(self):
        print("El coche tiene", self.ruedas, "ruedas, ", self.largoChasis,"cm de largo")



miCoche=Coche()             #Instancia de clase, crear objeto. No cal new

print("El largo del coche es :",miCoche.largoChasis)

print(miCoche.arrancar(True))          #Hara lo que esta definido en arrancar
miCoche.estado()

print("\n")
#Segundo objeto

miCoche2 = Coche()

print(miCoche2.arrancar(False))
print("El coche tiene :",miCoche2.ruedas, "ruedas")     #Sintaxis frase printf("tiene %i ruedas", ruedas)

miCoche2.pesoInicial=0                     #Cambiando una propiedad inicial del constructor
#                                          #Esta propiedad no deberia poder cambiarse i para eso usamos ENCAPSULACIÓN
miCoche2.estado()
