from tkinter import Tk
from tkinter import Frame
from tkinter import Label
from tkinter import LabelFrame
from tkinter import Entry
from tkinter import Text
from tkinter import Scrollbar
from tkinter import Button
from tkinter import StringVar


raiz = Tk()                 #Raiz es como el fondo donde iran los frames a raiz se le suele llamar root 

raiz.title("Interfaz grafica 1")

#raiz.iconbitmap("NombreArchivo.ico")            #archivo .ico para que salga

#raiz.resizable(0,0)           weight heith false     #Para que no se pueda redimensionar

raiz.geometry("1000x500")


raiz.config(bg="blue")          #Muchas de las config que hay en frame se puede poner en raiz


##CREANDO FRAME##   
MiFrame = Frame()                                            #En pack (fill="y") se va redimensiondo si vas haciendo mas grande la ventana. "x" redimensiona el ancho, ("y", expand="True") para el vertical. Both para todo 
MiFrame.pack(side = "right", anchor="n", fill="both")                   #En que sitio quieres que este el frame especificamente Anchor=n(north), s(sud).. side=left,top...

MiFrame.config(bg="red", width="650", height="350")                #Eso si a un frame hay que darle tamaño, 


MiFrame.config(bd="5", relief="sunken")        #bd para decir que haya borde

MiFrame.config(cursor="hand2")                  #Para que el cursor cambie de forma cuando te pones encima del frame



#SI cambias la extension py del archivo x pyw ya no abrira la consola de py al abrir el archivo https://docs.python.org/3/library/tk.html

## LABEL (PARA EL TEXTO) ##

miLabel = Label(MiFrame, text="Hola Waybiles", fg="white", bg="red")           #  (contenedor, opciones) Tipos de opciones= text, anchor, bg, bitmap, bd, font, fg, widtg, height, image, justify

miLabel.pack()                              #Empaquetamos pero adapta el frame al label, asi q con place lo arreglamos

miLabel.place(x=100, y=100)                 #x i y son la distancia a la que estaran del borde 


#Para poner imagen--> miImagen=PhotoImage(file="foto.png") label(image=miImagen)


raiz.mainloop() #Este bucle siempre al final

####################################################################################################
####################################################################################################

###  ENTRY (para poner texto) ###



miFrame=Frame(raiz, width=1200, height=600)
miFrame.pack()


miNombre = StringVar()                   #Textvariable=miNombre para que este asignado, stringvar . Al crear esta variable, si ponemos en entry(textvariable=) Imprimira lo que tenemos selecionado en miNombre, en este caso minombre.set=Dani asi que imprimira eso

###


cuadroTexto = Entry(miFrame, textvariable=miNombre)                     #La entri este en mi frame
#cuadroTexto.place(x=100 , y=100)                 #En que parte del frame colocar el cuadro
cuadroTexto.grid(row=0, column=1)                          #Para hacer una cantidad de casillas es el frame i asi colocar las cosas en cada sitio, empieza a contar desde 0
    #En grid ya no respeta el tamaño del frame igual q con pack. pero si lo hacemos mas grande si que se va colocando (3x3 creo q es grid )

nombreLabel = Label(miFrame, text="Nombre:")                      #Un label dentro de frame que tenga ese text
#nombreLabel.place(x=100, y=100)                 #Si los pones en el mismo sitio uno se pone delante de otro, es mejor usar pack()
nombreLabel.grid(row=0, column=0)


cuadroTexto2 = Entry(miFrame)
cuadroTexto2.grid(row=1, column=1)

email = Label(miFrame, text="E-mail:") 
email.grid(row=1, column=0)

cuadroTexto3 = Entry(miFrame)
cuadroTexto3.grid(row=2, column=1)
cuadroTexto3.config(fg="red", justify="right") #Configurar como se vera el texto en el cuadro introducible



Direccion = Label(miFrame, text="Dirección:") 
Direccion.grid(row=2, column=0, sticky="e", pady=0, padx=20)             #En sticky se puede poner n s w e en funcion de la posicion que quieras, tambien ne o sw ...
    #Sticky = El texto label esta como centrado, pero quizas quiero ponerlo todo a la izquierda o derecha, sticky=""
    #Pady = La distancia a los 4 lados de el label de texto. Pady = padding vertical. Padx = padding horitzontal
        
cuadroTexto4 = Entry(miFrame)
cuadroTexto4.grid(row=3, column=1)
cuadroTexto4.config(show="*")           #Para que parezca que una contraseña, todo lo que se ponga sera una contraseña

password = Label(miFrame, text="Contraseña:") 
password.grid(row=3, column=0)


###  TEXT(para texto largo) Y BUTTON ###

comment1 = Label(miFrame, text="Comentario:") 
comment1.grid(row=4, column=0)


comment = Text(miFrame, width=12, height=6)                 #Jode la interfaz porque text es enorme. Hace scrolling pero hay que agregarla manualmente la barra si quieres subir o bajar
comment.grid(row=4, column=1)


scrollVert = Scrollbar(miFrame, command="comment.yview")
scrollVert.grid(row=4, column=2, sticky="nsew")                            #Colocar al lado del sitio donde quieres que salga, sino no saldra. Con sticky nsew La barra se ajusta al grid
comment.config(yscrollcommand=scrollVert.set)                              #Para que la barra se vaya haciendo mas pequeña y grande y se mueva en funcion de la posicion en el texto




def codigoBoton():

    miNombre.set("Dani")

botonEnvio = Button(raiz, text="Enviar", command=codigoBoton)
botonEnvio.pack()

#Recursos adicionales: Columnspan, .get(), 
# lambda:


raiz.mainloop()

