from tkinter import Tk, Frame, Label, LabelFrame, Entry, Text, Scrollbar, Button, StringVar, Radiobutton, IntVar, Checkbutton, PhotoImage, Menu
from tkinter import messagebox, filedialog
#---------------Botones de Radio--------------#                                                     #Solo puedes elegir uno


root=Tk()

varOpcion=IntVar()                                                                   #Para poder definir variables en los botones y asi luego poder seleccionar, desselecionar. 

def imprimir():                                                             #La función que se hara una vez se elija un radiobutton
    
    if varOpcion.get() == 1:
        etiqueta.config(text="Elegiste masculino")
    else:
        etiqueta.config(text="Elegiste femenino")


Label(root, text="Género").pack()

Radiobutton(root, text="Masculino", variable=varOpcion, value=1, command=imprimir).pack()                                  #Empaqueta el .pack justo despues, el text="" la t en minuscula

Radiobutton(root, text="Femenino", variable=varOpcion, value=2, command=imprimir).pack()                  #Con el variable= y value= funcionan correctamente. Solo se puede pulsar uno. Me sorprende q la funcion en el command va sin ()

etiqueta=Label(root)
etiqueta.pack()


root.mainloop()

#---------------Botones de Radio--------------#                                              #CheckButton, botones de seleccion multiple       
root=Tk()
root.title("Ejemplo")

playa=IntVar()
montaña=IntVar()
rural=IntVar()

def opcionesViaje():
    opcionEscojida=""

    if(playa.get()==1):
        opcionEscojida+="playa "
    if(montaña.get()==1):
        opcionEscojida+="montaña "
    if(rural.get()==1):
        opcionEscojida+="rural "

    textoFinal.config(text=opcionEscojida)
#foto=PhotoImage(file="DSC_2147.jpg")
#Label(root, image=foto).pack()

frame=Frame(root)
frame.pack()

Label(frame, text="De que eres mas?", width=50).pack()


Checkbutton(frame, text="Playa", variable=playa, onvalue=1, offvalue=0, command= opcionesViaje).pack()                      #onvalue se refiere a lo que equivale la variable playa
Checkbutton(frame, text="Montaña", variable=montaña, onvalue=1, offvalue=0, command= opcionesViaje).pack()                     #offvalue el valor que tendra playa cuando desseleccionas 
Checkbutton(frame, text="Rural", variable=rural, onvalue=1, offvalue=0, command= opcionesViaje).pack()


textoFinal=Label(frame)
textoFinal.pack()





root.mainloop()

#---------------Menu, submenu y Ventanas emergentes--------------#


root=Tk()

#-- Ventanas emergentes --#                                                                     #tkinter messagebox

def infoAdicional():
    messagebox.showinfo("Acerca de", "Actualmente la version corre en 1.0.0")                   #La primera sera lo que aparezca en la cabezera y el segundo texto lo que salga abajo       

def AvisoPeligro():
    messagebox.showwarning("Peligro", "No se puede realizar este comando")                                  #En la ventana emergente en vez de I de info saldra una cosa amarilla de peligro

def salirAplicacion():
    valor = messagebox.askquestion("Salir", "Seguro que deseas salir?")                                     #Emergente que tiene dos botones de respuesta, SI y NO
    #valor = messagebox.askokcancel("Salir", "Seguro que deseas salir?")                                    #Este devuelve True o False sin ser string
    #valor = messagebox.askretrycancel("Error", "No es posible realizar esto")                                 #True false 
    if valor =="yes":                                                                                        #askquestion devuelve dos valores en string "yes y "no" para eso ponemos q si es yes pues root.destroy para cerrar
        root.destroy()                                                                                        #Cerrar programa     

def abreFichero():
    fichero=filedialog.askopenfilename(title="Abrir", initialdir="D:", filetypes=(("Ficheros de Excel","*.xlsx"), ("Ficheros de texto", "*.txt"), ("Todos los ficheros", "*.*")))                          #Esto nos devuelve algo, por defecto empieza la busqueda en C:/documents 
    print(fichero)                                                                                             #La pequeña funcion que hara, print en consola la ubicación del archivo. 
    # title= nombre en el header de la emergente. initialdir=directorio donde se abrira primero el abrir. filetypes= Los tipos de archivos que quieres que se puedan ver/abrir (en tupla)

#-- Menu principal --#

barraMenu=Menu(root)
root.config(menu=barraMenu, width=300, height=300)                                                     #configurar el menu


archivoMenu=Menu(barraMenu, tearoff=0)                                          #Tearoff es para quitar la barra que viene por defecto, fijarse en los otros menus
#-- Agregando submenu a Archivo --#
archivoMenu.add_command(label="Nuevo")
archivoMenu.add_command(label="Ventana nueva")
archivoMenu.add_command(label="Abrir", command=abreFichero)
archivoMenu.add_separator()                                                             #Añadir pequeña barrita separadora, ademas te situa la barra de submenu al desplegar mas estetica.
archivoMenu.add_command(label="Guardar")
archivoMenu.add_command(label="Salir", command=salirAplicacion)





archivoEdicion=Menu(barraMenu)
archivoEdicion.add_command(label="Undo")
archivoEdicion.add_command(label="Redo")


archivoHerramientas=Menu(barraMenu)
archivoAyuda=Menu(barraMenu, tearoff=0)
archivoAyuda.add_command(label="Acerca de", command=infoAdicional)                              #Comando a la ventana emergente


barraMenu.add_cascade(label="Archivo", menu=archivoMenu)                            #Para especificar el texto de ese menu
barraMenu.add_cascade(label="Herramientas", menu=archivoHerramientas)                       #el orden en el que esten los cass_cades sera como esten luego ordenados en el menu
barraMenu.add_cascade(label="Edición", menu=archivoEdicion)
barraMenu.add_cascade(label="Ayuda", menu=archivoAyuda)


root.mainloop()