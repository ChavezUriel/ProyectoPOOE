from tkinter import *
from PIL import ImageTk, Image
import modules as md
import generarPuntos as gen

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
principalFrame.config(width=1100, height=505)
principalFrame.config(bg=colors[1])



##########  Grafica Mollweide con Botones ##########
def PosBotones(n):
    xpos, ypos = gen.positions(n)
    xpos = xpos*10
    ypos = ypos*10
    center = [1500/2-60, 820/2-55]
    botones = {}
    button_img = PhotoImage(file='media/circle.png').subsample(20)
    for i in range(n):
        canvas.bind('<Button-'+str(i+1)+'>', on_click(xpos[i],ypos[i]))
        button_id = canvas.create_image((center[0]+xpos[i], center[0]+ypos[i]), image=button_img, anchor='center')


def on_click(x,y):
    print('x',x,'y',y)

 

canvas = Canvas(principalFrame, width=1366, height=690)
canvas.pack()
canvas.bind('<Button-1>', on_click(0, 0))
PosBotones(10)
background = PhotoImage(file='media/plotBackground.png').zoom(2)
background_id = canvas.create_image((0, 0), image=background, anchor='nw')

button_img = PhotoImage(file='media/circle.png').subsample(20)
button_id = canvas.create_image((1500/2-60, 820/2-55), image=button_img, anchor='center')
button_img = PhotoImage(file='media/circle.png').subsample(20)
button_id = canvas.create_image((1400/2-60, 820/2-55), image=button_img, anchor='center')






#Tamaño predefinido
ventanaPrincipal.geometry('1500x820')
#Color de fondo
ventanaPrincipal.config(bg='gray')
#Loop para mantener ejecutando la ventana
ventanaPrincipal.mainloop()