#Funciones STRING

# upper() Pone en mayus las letras d un string
# lower() Igual pero minus
# capitalize() Pone mayus la primera letra de un string 
# count() Contar cuantas veces aparece una letra o string en una frase
# find() Indice(posicion) de un string
# isdigit() Dice si el valor es digito o no
# isalum()  Si es alphanumerico
# isalpha() si es alpha comprueba si son solo letras
# split()  separa por palabras utilizando espacios
# strip() borrar espacios sobrantes al principio y final
# replace() cambia una palabra x otra
# rfind() igual q find pero contando desde atras
## http://pyspanishdoc.sourceforge.net/







####### EJEMPLOS #######

nombre = input()
print("El nombre es:", nombre.upper())      #asi se ponen todas estas funciones

####### MODULOS #######


import Herencia

from Apuntes import evaluacion #una funcion en especifico

from Clases import * #SI usas * importas todo

#Si no esta en la misma carpeta, busca en syspath

####### PAQUETES #######

# CREAR PAQUETE-> crear carpeta con un archivo que se diga: __init__.py

#     puedes usar los modulos que quieras desde esa carpete donde este init
#para usar:
from nombreCarpeta.nombreModulo import nombreFunción

#Como enviar paquetes online?    instalar (llamar al paquete independientemente de donde este)

## 1r Crear paquete --> Archivo: setup.py y poner:
from setuptools import setup
setup(
    name="nombrePaquete",
    version="1.0",
    description="Sivrve para ...",
    author="Yo",
    author_email="x@es.es",
    url="x.es",
    packages=["nombreCarpeta", "nombreCarpeta.nombreArchivo]                           #Importante, RUTA donde este el 

)
#           cmd, ir a la carpeta, escribir: python setup.py sdist
#           se crean dos carpetas: dist y paqueteNombre.egg-info
#           en dist hay un zip para enviar a la gente. 
## 2n instalar paquete --> Una vez tienes el zip
#            cmd ir carpeta dist 
#            install nombrePaquete.zip
#           unistall--> pip3 unistall nombrePaquete   (en cmd i no hace falta estar en ninguna carpeta)

