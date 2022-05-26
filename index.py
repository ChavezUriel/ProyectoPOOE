from tkinter import *
from PIL import ImageTk, Image

def imprimirNombre():
    print('Bienvenido al mundo del sida')

def imprimirMensajeIngresado():
    labelPrincipal['text']=cajaTexto.get()
colors = ['gray','black','white']

ventanaPrincipal = Tk()
#Agregar un titilo en la ventana
ventanaPrincipal.title("Titulo de la interfaz.")
#Bloquear redimensionar ventana
ventanaPrincipal.resizable(1,0)
#Icono de ventana
ventanaPrincipal.iconbitmap(('/home/baruch/Documentos/GitHub/POOE/GraphicInterphase/inoco.ico'))
#Fodno
imagen = ImageTk.PhotoImage(Image.open('/home/baruch/Documentos/GitHub/POOE/GraphicInterphase/ss.jpg'))
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

#Botones
segLabelPrin = Label(ventanaPrincipal, text = 'CARRERA')
segLabelPrin.pack()
boton = Button(ventanaPrincipal,text='descarga Juegos sin viruz', command=imprimirNombre)
boton.pack()

cajaTexto = Entry(ventanaPrincipal)
cajaTexto.pack()

boton2 = Button(ventanaPrincipal,text = 'descarga aquí :D', command=imprimirMensajeIngresado)
boton2.pack()





#Tamaño predefinido
ventanaPrincipal.geometry('960x540')
#Color de fondo
ventanaPrincipal.config(bg='gray')
#Loop para mantener ejecutando la ventana
ventanaPrincipal.mainloop()