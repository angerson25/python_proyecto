#Importarla libreria tkinter y todas sus funciones
from tkinter import *
from tkinter import Tk, Label, Button, Entry, Spinbox, OptionMenu, StringVar

#-----------------
#Ventana principal
#-----------------

#funciones
#funcion piernas
def piernas():
    ventanapiernas=Tk()
    ventanapiernas.title("Ejercicios Piernas")
    imagen=PhotoImage(file="foto/piernas.png")
    fondo=Label(ventanapiernas, image=imagen)
    fondo.place(x=0,y=0)
    ventanapiernas.mainloop()

def brazos():
    ventanapiernas=Tk()
    ventanapiernas.title("Ejercicios Piernas")
    imagen=PhotoImage(file="foto/brazos.png")
    fondo=Label(ventanapiernas, image=imagen)
    fondo.place(x=0,y=0)
    ventanapiernas.mainloop()

def abdomen():
    ventanapiernas=Tk()
    ventanapiernas.title("Ejercicios Piernas")
    imagen=PhotoImage(file="foto/abdomen.png")
    fondo=Label(ventanapiernas, image=imagen)
    fondo.place(x=0,y=0)
    ventanapiernas.mainloop()

#Se declara una variable llamada ventana_principal y que adquiere las caracteristicas tk
ventana_principal = Tk()

#titulo de la ventana
ventana_principal.title("Proyecto")

#dimensiones de la ventana(ancho,alto)
ventana_principal.geometry("500x350")

#permite deshabilitar boton de maximizar
ventana_principal.resizable(0,0)

#color de fondo
ventana_principal.config(bg="white")

#frame
frame_entrada = Frame(ventana_principal)
frame_entrada.config(bg="white", width=480, height=230)
frame_entrada.place(x=10, y=10)

#etiqueta para el titulo de la app
titulo = Label(frame_entrada, text="HEALTH TRAINING")
titulo.config(bg="white", fg="black", font=("Bahnschrift SemiBold", 20))
titulo.place(x=10, y=10)

#texto1
texto1= Label(frame_entrada, text="¿Qué parte del cuerpo deseas entrenar?")
texto1.config(bg="white", fg="black", font=("Bahnschrift SemiBold", 16))
texto1.place(x=10, y=130)

#boton
bt_pie = Button(frame_entrada, text=("Piernas") , command=piernas)
bt_pie.place(x=10, y=170, width=100, height=30)

#boton
bt_bra = Button(frame_entrada, text=("Brazos") , command=brazos)
bt_bra.place(x=150, y=170, width=100, height=30)

#boton
bt_ab = Button(frame_entrada, text=("Abdomen") , command=abdomen)
bt_ab.place(x=290, y=170, width=100, height=30)






ventana_principal.mainloop()