class Vehiculos():             #Clase padre o superclase
    
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self.enmarcha = False
        self.acelera = False
        self.frena = False
    
    def arrancar(self):
        self.enmarcha = True
    def acelerar(self):
        self.acelera = True
    def frenar(self):
        self.frena = True
    def estado(self):
        print("Marca: " ,self.marca, "\nModelo: ", self.modelo, "\nMarcha: ", self.enmarcha)

class Moto(Vehiculos):                         #Clase moto que utiliza de la classe vehiculos


    hcaballito=""                                    #   pass                                       #Pass para que funcione aunque no le pongas nada especifico a la clase
    
    def caballito(self):
        self.hcaballito="Voy haciendo el caballito"
    def estado(self):
        print("Marca: " ,self.marca, "\nModelo: ", self.modelo, "\nMarcha: ", self.enmarcha, "\n", self.hcaballito)

class Furgoneta(Vehiculos):
    
    def carga(self, cargar):
        
        self.cargado = cargar
        
        if(self.cargado == True):                            #Igual que no poner el ==True
            return "La furgoneta esta cargada"
        else:
            return "La furgo no esta cargada"

class VElectricos():                                      #Clase Independiente xk no hereda de nada
    def __init__(self):
        self.autonomia = 100
    def cargarEnergia(self):
        self.cargando = True

class BicicletaElectrica(Vehiculos, VElectricos):         #Hereda de dos clases, todos los metodos y propiedades de las dos. Hereda constructor Vehiculos xk entre () es el primero q se pone
    #pass                                                       #Cuando hay herencia multiple que constructor hereda? I metodos tambien
        
    def __init__(self, cadena):
        self.estadoCadena = cadena
        super().__init__("BMX", "XA")         #Esta instruccion permite que se pueda usar EL INIT de la clase padre (Vehiculos)

    def arrancar(self):
        super().arrancar()                       #Hace el metodo arrancar de la classe padre 
        self.cargado=-1                              #Ademas de lo que le hemos dicho ahora, sin super() solo ejecutaria el cargado-1 si llamamos a arrancar para BiciElectrica

MiMoto=Moto("Honda", "CBR")
MiMoto.estado()

MiMoto.caballito()
MiMoto.estado()                                 #Que nos informe tambien si hace el caballito heredando lo de antes


MiFurgoneta = Furgoneta("Renault", "Kangoo")
print(MiFurgoneta.carga(True))

MiFurgoneta.arrancar()
MiFurgoneta.estado()


####
miBici=BicicletaElectrica(12)                  #Hereda el constructor de la primera classe que pongas entre()
miBici.estado()
print(isinstance(miBici, Vehiculos))           #isinstance para saber que tipo de classe es un objeto (si tiene herencia de otros, los q preguntes)

### "Polimorfismo"
def arrancamiento(cosa):
    cosa.arrancar()

Micosa=Vehiculos("sin marca", "sin modelo")        #Puedes assignar este comportamineto a que haga una función de un objeto
print(arrancamiento(Micosa))
