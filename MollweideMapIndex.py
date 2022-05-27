from tkinter import *
from PIL import ImageTk, Image
import modules as md

## Detalles de ventana ##
colors = ['gray','black','white']
ventanaPrincipal = Tk(className='Mapa de objetos astronómicos')
ventanaPrincipal.resizable(0,0)
segLabelPrin = Label(ventanaPrincipal, text = 'CARRERA')
segLabelPrin.pack()
boton = Button(ventanaPrincipal,text='descarga Juegos sin viruz')
boton.pack()
## Frame del mapa ##
principalFrame = Frame()
principalFrame.pack()
principalFrame.config(width=2050, height=1040)
principalFrame.config(bg=colors[1])



##########  Grafica Mollweide con Botones ##########
def PosBotones():
    pos = md.getCordinates()
    center = [3000/2-25, 1570/2-20]
    # for i in range(len(pos[0])):


def on_click():
    print('click')

 

canvas = Canvas(principalFrame, width=2050, height=1040)
canvas.pack()
canvas.bind('<Button-1>', on_click())

background = PhotoImage(file='media/plotBackground.png').zoom(3)
background_id = canvas.create_image((0, 0), image=background, anchor='nw')

button_img = PhotoImage(file='media/circle.png').subsample(20)
button_id = canvas.create_image((2050/2, 1040/2), image=button_img, anchor='center')






#Tamaño predefinido
ventanaPrincipal.geometry('3000x1570')
#Color de fondo
ventanaPrincipal.config(bg='gray')
#Loop para mantener ejecutando la ventana
ventanaPrincipal.mainloop()