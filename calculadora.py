from tkinter import Tk, Frame, Label, LabelFrame, Entry, Text, Scrollbar, Button, StringVar

raiz=Tk()
miFrame=Frame(raiz)
miFrame.pack()

#---------------OPERACIÓN--------------#

operacion=""                                        #cadena vacia hasta que se clique alguna operacion

resultado=0


#---------------PANTALLA---------------#

numeroPantalla = StringVar()                                                    #numeroPantalla es una variable string que saldra en el Entry, esta variable la definiremos en una funcion

pantalla = Entry(miFrame, textvariable=numeroPantalla)                       #La pantalla donde saldran los nnumeros
pantalla.grid(row=1, column=1, padx=10, pady=10, columnspan=4)    #En que sitio quiero que salga #IMPORTANTE: columnspan=4 hace que la pantalla ya sepa que se divide en 4 y asi los proximos botones se podran posicionar bien
pantalla.config(background="black", fg="white", justify="right")    #Como se vera el texto y el fondo del entry

#---------------Pulsar Teclado----------#

def numeroPulsado(num):                                                   #No podemos enviar los numeros directamente a la entrada de la función porque luego en el command=numeroPulsado("4") que seria lo que se pondria, se ejecutaria sin llamarlo, xk python todo lo que tenga entre parentesis lo ejecuta.
    #numeroPantalla.set("4")                                        #En el numero 4 agregames command=numeropulsado, PERO esto solo permite poner un 4 y ya, te elimina los numeros que habian antes
    # ESTO SE PONE EN EL ELSE :  numeroPantalla.set(numeroPantalla.get() + num)              #El get coge lo que ya habia y le mete el 4 adicional que estas pulsando, posteriormente he puesto num para q funcione con todo

    global operacion    #ERROR
    if operacion!="":                                       #Si operacion distinto a cadena vacia es que se ha pulsado suma o x y hay que eliminar los numeros que habia antes        
        numeroPantalla.set(num)                                 #Escribe el nuevo numero pero sin el get.
        operacion=""                                            #Para que vuelva a estar sin nada
    else:
        numeroPantalla.set(numeroPantalla.get() + num)                                          ###AQUI ESTA EL ERROR

#---------------Pulsar Teclado OPERACIONES----------#


def suma(num):
    global operacion                                                        #Global xk ha de tener en cuenta que operacion es una variable global #(num) xk almacena el numero q hay en pantalla ya.

    global resultado
    resultado+=int(num)
    operacion="suma"

    numeroPantalla.set(resultado)

#---------------funcion resultado----------#

def el_resultado():
    global resultado
    numeroPantalla.set(resultado + int(numeroPantalla.get()))           
    resultado=0

#--------------Fila 1-------------------#

boton7 = Button(miFrame, text="7", width=3, command=lambda:numeroPulsado("7"))
boton7.grid(row=2, column=1)

boton8 = Button(miFrame, text="8", width=3, command=lambda:numeroPulsado("8"))
boton8.grid(row=2, column=2)

boton9 = Button(miFrame, text="9", width=3, command=lambda:numeroPulsado("9"))
boton9.grid(row=2, column=3)

botonDiv = Button(miFrame, text="/", width=3)
botonDiv.grid(row=2, column=4)

#--------------Fila 2-------------------#

boton4 = Button(miFrame, text="4", width=3, command=lambda:numeroPulsado("4"))                          #Command funcionalidad del boton, usara la funcion numero pulsado pasandole como parametro num "4"
boton4.grid(row=3, column=1)

boton5 = Button(miFrame, text="5", width=3, command=lambda:numeroPulsado("5"))                          #lambda es una función que hace que no se ejecute una función con (), sino que quede a la espera. Sino pasaria lo que esta explicado en el #def de la funcion.     
boton5.grid(row=3, column=2)

boton6 = Button(miFrame, text="6", width=3, command=lambda:numeroPulsado("6"))
boton6.grid(row=3, column=3)

botonMult = Button(miFrame, text="x", width=3)
botonMult.grid(row=3, column=4)

#--------------Fila 3-------------------#

boton1 = Button(miFrame, text="1", width=3, command=lambda:numeroPulsado("1"))
boton1.grid(row=4, column=1)

boton2 = Button(miFrame, text="2", width=3, command=lambda:numeroPulsado("2"))
boton2.grid(row=4, column=2)

boton3 = Button(miFrame, text="3", width=3, command=lambda:numeroPulsado("3"))
boton3.grid(row=4, column=3)

botonRest = Button(miFrame, text="-", width=3)
botonRest.grid(row=4, column=4)

#--------------Fila 3-------------------#

boton0 = Button(miFrame, text="0", width=3, command=lambda:numeroPulsado("0"))
boton0.grid(row=5, column=1)

botonComa = Button(miFrame, text=",", width=3, command=lambda:numeroPulsado("."))
botonComa.grid(row=5, column=2)

botonIgual = Button(miFrame, text="=", width=3, command=lambda:el_resultado())
botonIgual.grid(row=5, column=3)

botonSum = Button(miFrame, text="+", width=3, command=lambda:suma(numeroPantalla.get()))                    #Command, si pulsas el boton, llamas a la función suma y lambda para que no se active instantaneo #el get piensa
botonSum.grid(row=5, column=4)


raiz.mainloop()

