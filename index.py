from tkinter import *
from PIL import ImageTk, Image
import modules as md

colors = ['gray','black','white']
ventanaPrincipal = Tk(className='Ventana en Python')
ventanaPrincipal.resizable(0,0)
imagen = ImageTk.PhotoImage(Image.open('/home/baruch/Documentos/GitHub/ProyectoPOOE/media/plotBackground.png'))
# # Con Label y la opción image, puedes mostrar una imagen en el widget:
background = Label(image = imagen, text = "Imagen S.O de fondo")
# # Con place puedes organizar el widget de la imagen posicionandolo
# # donde lo necesites (relwidth y relheight son alto y ancho en píxeles):
background.place(x = 0, y = 0, relwidth = 1, relheight = 1)

labelPrincipal = Label(ventanaPrincipal,text='Etiqueta en ventana principal',font=('AbyssinicaSIL',15))
labelPrincipal.pack()


#Usando Frames:
principalFrame = Frame()
principalFrame.pack()
principalFrame.config(width=400, height=100)
principalFrame.config(bg=colors[0])

# labelframe = Label(principalFrame,text='Etiqueta en frame',fg=colors[2],font=('arial',15))
# labelframe.config(bg=colors[1])
# labelframe.place(x=1,y=1)
imageFrame = ImageTk.PhotoImage(Image.open('/home/baruch/Documentos/GitHub/POOE/GraphicInterphase/bio.jpg'))

labelEnFrame = Label(principalFrame, image=imageFrame)
labelEnFrame.place(x=0,y=0)



##########  Grafica Mollweide con Botones ##########

background = Label(image = imagen, text = "Imagen S.O de fondo")
background.place(x = 0, y = 0, relwidth = 1, relheight = 1)
 
img = PhotoImage(file='/home/baruch/Documentos/GitHub/ProyectoPOOE/media/circle.png')
dwnd = img.subsample(32) #with 250, I ended up running out of memory
boton = Button(ventanaPrincipal, image=dwnd, command=None, borderwidth = 0)

boton.pack(pady=10)
boton.place(x=3000/2, y=1570/2)




#Tamaño predefinido
ventanaPrincipal.geometry('3000x1570')
#Color de fondo
ventanaPrincipal.config(bg='gray')
#Loop para mantener ejecutando la ventana
ventanaPrincipal.mainloop()