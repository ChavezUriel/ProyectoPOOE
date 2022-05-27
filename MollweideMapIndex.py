from tkinter import *
from PIL import ImageTk, Image
import modules as md
import generarPuntos as gen
from functools import partial



#####   NUMERO DE PUNTOS  #######
n = 100

## Detalles de ventana ##
# Dimensiones de la ventana
dimVentana = [1500,820]

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
principalFrame.config(bg='black',borderwidth=1)



##########  Grafica Mollweide con Botones ##########



def on_click(x,y):
    print('x', x)

 
DimMap = [1366,690]
canvas = Canvas(principalFrame, width=DimMap[0], height=DimMap[1])
centroMap = [1500/2-85,820/2-65]
canvas.pack()
# Background Map
background = PhotoImage(file='media/plotBackground.png').zoom(2)
background_id = canvas.create_image((0, 0), image=background, anchor='nw')

# Position of each button
xpos, ypos = gen.positions(n)

# Declare buttons
button_img = PhotoImage(file='media/circle.png').subsample(60)
for i in range(n):
    button = Button(principalFrame, image = button_img, bg='black',  borderwidth=0,
                    command=partial(on_click, xpos[i],ypos[i]))
    button.place(x=centroMap[0]+xpos[i]*centroMap[0], y=centroMap[1]+ypos[i]*centroMap[1]*2)







#Tamaño predefinido
dimVentana
ventanaPrincipal.geometry(str(dimVentana[0])+'x'+str(dimVentana[0]))
#Color de fondo
ventanaPrincipal.config(bg='gray')
#Loop para mantener ejecutando la ventana
ventanaPrincipal.mainloop()