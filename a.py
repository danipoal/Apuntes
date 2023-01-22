from tkinter import Tk, Frame, Label, LabelFrame, Entry, Text, Scrollbar, Button, StringVar, Radiobutton, IntVar, Checkbutton, PhotoImage, Menu
from tkinter import messagebox, filedialog

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