####### ARCHIVOS EXTERNOS #######
# https://docs.python.org/es/3/library/io.html
from io import open      #para poder abrir un archivo externo

archivo_texto = open("nombreArchivo.txt", "w")      #mode lectura, escritura, append .. w de write

frase="Estupendo dia para hacer algo\nHoy es lunes"

archivo_texto.write(frase)                          #Para añadir esste texto
archivo_texto.close()                               #para cerrar el archivo despues de manipular

#podemos hacer ahora:                       No funciona xk esta todo en un archivo

archivo_texto2 = open("nombreArchivo.txt", "r")    #r de read

texto = archivo_texto2.read()
linea_especifica = archivo_texto2.readline()               #readline la que digas y readlines te hace array dividida por los \n
archivo_texto2.close()
print(texto)                                  #El \n lo trata como texto tmbn

print(linea_especifica[0])

#Añadir solo una linia

archivo_texto3 = open("nombreArchivo.txt", "a")     #"a" de append, "r+"=tanto lectura y escritura

archivo_texto3.write("\nSiempre es buen dia")
archivo_texto3.close()


#El cursor siempre estara en el principio del primer caracter del txt, para cambiar el puntero a otro caracter:
archivo_texto3.seek(11) #Colocate en caracter 11 (no se hace xk esta close)
archivo_texto3.read(11)   #Esto significa que haga lectura solo HASTA el caracter 11

archivo_texto3.seek(len(archivo_texto3.read())/2) #un poco chorrada

####### SERIALIZACIÓN #######
import pickle                               #Para codificar en binario importamos esta lubreria

lista_nombres=["Pedro", "Ana", "Maria", "Isabel"]
fichero_binario=open("Nombre_ficheroExterno", "wb")         #wb= write binary

pickle.dump(lista_nombres, fichero_binario)                 #Se pone el archivo en binario

fichero_binario.close()

#Para leerlo
import pickle
fichero=open("Nombre_ficheroExterno", "rb")                 #rb read binary

lista=pickle.load(fichero)                                  #decodificar y acceder info
print(lista)

## serializar OBJETOS
import pickle

class Coche():
    xd=0

#       pickle.dump(array, NombreFichero)             

####### GUARDADO PERMANENTE #######

import pickle

class persona:
    def __init__(self, nombre, genero, edad):
        self.nombre=nombre
        self.genero=genero
        self.edad=edad
        print("Se ha creado una persona nueva con el nombre de ", self.nombre)
    
    def __str__(self):                          #Convertir en string un objeto
        return"{}{}{}".format(self.nombre, self.genero, self.edad)
    
class ListaPersonas:
    personas=[]

    def __init__(self):
        listaDePersonas=open("FicheroExterno", "ab+")     #ab+ agregar info binaria
        listaDePersonas.seek(0)

        try: #Xk es la primera vez en ejecutar i dara error
            self.personas=pickle.load(listaDePersonas)
            print("Se cargaron {} personas del fichero".format(len(self.personas)))
        except:
            print("Error")
        finally:
            listaDePersonas.close()
            del(listaDePersonas)

    def agregarPersonas(self, p):
        self.personas.append(p)

    def mostrarPersonas(self):
        for p in self.personas:
            print(p)
    
    def guardarPersonasEnFicheroExterno(self):
        ListaPersonas=open("ficheroExterno", "wb")
        pickle.dump(self.personas, ListaPersonas)
        ListaPersonas.close()
        del(ListaPersonas)

    def mostrarInfoFichero(self):
        print("La info es la siguiente:")
        for p in self.personas
            print(p)



miLista=ListaPersonas()
p=persona("Sandra", "Femenino", 21)
miLista.agregarPersonas(p)

p=persona("Juan", "Masculino", 11)
miLista.agregarPersonas(p)

p=persona("Fabia", "Femenino", 31)
miLista.agregarPersonas(p)

miLista.mostrarPersonas()