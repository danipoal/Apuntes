#LISTAS Y TUPLAS

tupla1=("Juan", 12, 1, 1999)
print(tupla1[1])
lista1=list(tupla1)
tupla2="Dani", 12, 2, 1999
tuplaUnitaria=("Jose",)


    # Listas .append .insert .extend .index .remove .pop 



print(tupla1.count("Juan"))
print(len(tupla1))

nombre, dia, mes, agno=tupla2
print(nombre) #Dani

#DICCIONARIOS

miDiccionario={"Alemania":"Berlín", "Francia":"París", "Reino Unido":"Londres", "España":"Madrid"}
print(miDiccionario["Alemania"]) #Berlín
miDiccionario["Italia"]="Lisboa" #Añadir al diccionario [clave]=valor
miDiccionario["Itaria"]="Roma"   #Modificar (Se sobrescribe)
del miDiccionario["Reino Unido"] #Eliminar

PaisesTupla=["España", "Francia"]
miDiccionario={PaisesTupla[0]:"Madrid", PaisesTupla[1]:"París"} #Usar tupla para asignar claves

JordanDiccio={23:"Jordan", "Nombre":"Michael", "anillos":[1991,1992,1993,1996]} #Tupla dentro de un valor . Tambien se puede diccionario dentro de diccionario

print(miDiccionario.keys)         #Las claves
print(miDiccionario.values)       #Los valores

#CONDICIONALES : IF

print("Programa de evaluación de notas de alumno")
nota_alumno=input("Introduce la nota:")        #Es un scanf que se guarda en nota_alumnos

def evaluacion(nota):
    valoración="aprovado"          #Valoración solo se ha definido en la función asi que solo se puede modificar ahi
    if nota<5:
        valoración="suspenso"
    return valoración

print(evaluacion(int(nota_alumno))) #Input siempre considera en TEXTO asi que con int lo convertimos

edad_usuario=int(input("Introduce la edad"))
if edad_usuario<18:
    print("No puede pasar")
else:                               #Estructura else  else if= elif
    print("Puedes pasar")

print("Edad es" + str(edad_usuario)) #como edad usuario es int, para imprimir junto a un string hay que hacer str()

#BUCLES

for i in "juan":                     #El end es para q no haga \n
    print("Hola", end="")            #hace el bucle tantas veces caracteres encuentre, si es array pues tantos vectores haya

email=False
for e in "juan@pildoras.es":        #in viene siendo como que "es", osea i es "juan@.." y acaba siendo el último caracter, pero hay un momento que ha sido @
    if(i=="@"):
        email=True
    break                           #Cuando encuentre el @, el break detiene el bucle

for a in range(5):                  #array de 5
    print(f"Valor de la variable {a}")   # printf("Valor de la variable %i", a);

import math          #include <math.h> como si fuera

solucion=0
a=5
if a==5:
    solucion=math.sqrt(a)   #retorna la raiz quadrada
    print(solucion)         #continue= sirve para ignorar lo q haya debajo en un bucle i volver al bucle

while True:
    pass                    #Estar en el bucle hasta q se haga ctrl+c pass= ignorar

#GENERADORES

def generaPares(limite):
    num=1
    while num<limite:
        yield num*2        #En vez de return yield que es un objeto iterativo
        num+=1

devuelvePares=generaPares(10)
for i in devuelvePares:
    print(i)

def devuelve_ciudades1(*ciudades):      #* significa no sabemos cuantos y en tupla
    for elemento in ciudades:
        yield elemento
ciudades_devueltas=devuelve_ciudades("Madrid", "Barcelona", "Bilbao")
print(next(ciudades_devueltas))          #Next para que el generador vaya pasando
print(next(ciudades_devueltas)) #imprime Barcelona

def devuelve_ciudades(*ciudades):      
    for elemento in ciudades:
        for subElemento in elemento:
            yield subElemento        # Esto serian dos for anidados que es = a yield from

def devuelve_ciudades2(*ciudades):      
    for elemento in ciudades:
        yield from elemento         #Asi se haria
    
#EXCEPCIONES

def divide(num1,num2):
    try:                           #Que intente hacer y si no lo consigue ejecuta el except
        return num1/num2
    except ZeroDivisionError:
        print("error")
        return "Error"

while True:                       #Bucle infinito hasta q se ejecute bien i salga x el break
    try:                          #Try siempre tiene que tener except o finally
        a=0
        op=input()
        break
    except ValueError:
        a=1
    except ZeroDivisionError:        #Mas de una excepción pa tener encuenta mas errores
        a=1
    finally:                         #Para que se ejecute siempre si o si tanto si hay except como si try sale bien
        print("xd")

edad=0
if edad<0:                            #Puedes lanzar tu propio error no predefinido pero hay q definirlo
    raise TypeError("No se permiten edades negativas") #hacer saltar un error aposta
