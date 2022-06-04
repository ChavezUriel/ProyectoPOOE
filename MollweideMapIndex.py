from tkinter import *
import objast as oa
import puntos as gen
from functools import partial
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt



class Map():
    def __init__(self):
        #####   NUMERO DE PUNTOS  #######
        self.n = 10
        ## Detalles de ventana ##
        # Dimensiones de la ventana
        self.ventanaPrincipal = Tk(className='Mapa de objetos astronómicos')
        self.dimVentana = [1500,800]
        self.ventanaPrincipal.geometry(str(self.dimVentana[0])+'x'+str(self.dimVentana[1]))
        self.colors = ['gray','black','white']
        self.ventanaPrincipal.resizable(0,0)
        self.segLabelPrin = Label(self.ventanaPrincipal, text = 'CARRERA')
        self.segLabelPrin.pack()
        self.boton = Button(self.ventanaPrincipal,text='descarga Juegos sin viruz')
        self.boton.pack()
        ## Frame del mapa ##
        self.principalFrame = Frame()
        self.principalFrame.pack()
        self.principalFrame.config(width=1100, height=505)
        self.principalFrame.config(bg='black',borderwidth=1)



        ##########  Grafica Mollweide con Botones ##########



        def on_click(pos,lista_objetos,nu):
            emergente = details(pos,lista_objetos,nu)
            return 0

        
        self.DimMap = [1366,690]
        self.canvas = Canvas(self.principalFrame, width=self.DimMap[0], height=self.DimMap[1])
        self.centroMap = [1500/2-85,820/2-65]
        self.canvas.pack()
        # Background Map
        self.background = PhotoImage(file='media/plotBackground.png').zoom(2)
        self.background_id = self.canvas.create_image((0, 0), image=self.background, anchor='nw')

        # Position of each button
        lista_objetos = oa.generarObjetos(self.n)
        pos = oa.getpos(lista_objetos)
        self.xpos, self.ypos = gen.ang_to_mollweide(pos.T[0],pos.T[1])

        # Declare buttons
        self.button_img = PhotoImage(file='media/circle.png').subsample(60)
        for i in range(self.n):
            self.button = Button(self.principalFrame, image = self.button_img, bg='black',  borderwidth=0,
                            command=partial(on_click, pos,lista_objetos[i],i+1))
            self.button.place(x=self.centroMap[0]+self.xpos[i]*self.centroMap[0], y=self.centroMap[1]+self.ypos[i]*self.centroMap[1]*1.9)



        
        #Color de fondo
        self.ventanaPrincipal.config(bg='gray')
        #Loop para mantener ejecutando la ventana

        # #   Ventana emergente con los detalles
        # def details():
        #     emergente = details()

        Button(self.ventanaPrincipal, text="Quit", command=self.killApp).pack()
        self.ventanaPrincipal.mainloop()
    def killApp(self):
            self.ventanaPrincipal.quit()
    
class details():
    def __init__(self, pos, lista_objetos, nu):
        self.pos = pos
        self.lista_objetos = lista_objetos
        self.numeroDeObjeto = nu
        self.detalles = Tk(className='Mapa de objetos astronómicos')
        self.dimVentana = [800,600]
        self.detalles.geometry(str(self.dimVentana[0])+'x'+str(self.dimVentana[1]))
        self.colors = ['gray','black','white']
        self.detalles.resizable(0,0)
        

        # Barra superior
        self.TopBg = Frame(self.detalles)
        self.TopBg.config(bg='LightSkyBlue1',highlightbackground = "black", highlightcolor= "black")
        self.TopBg.place(x=15,y=1)
        self.TopBg.config(width=770, height=70)
        self.TopBg.pack()
        self.TopBar = Frame(self.detalles)
        self.TopBar.pack()
        self.TopBar.place(x=200,y=10)
        self.TopBar.config(width=770, height=707)
        self.Titulo = Label(self.TopBar, text=('Información de objeto '+str(self.numeroDeObjeto)))
        self.Titulo.config(font=("TimesNewRoman", 30))
        self.Titulo.config(bg='LightSkyBlue1',borderwidth=1)
        self.Titulo.pack()



        #Atributos del objeto astronomico:
        self.detTit = Frame(self.detalles)
        self.detTit.pack()
        self.detTit.place(x=40,y=90)
        self.Titulo = Label(self.detTit, text=('Información técnica'))
        self.Titulo.config(font=("TimesNewRoman", 16))
        self.Titulo.config(bg='Azure3',borderwidth=1)
        self.Titulo.pack()
        self.BarraDetalles = Frame(self.detalles)
        self.BarraDetalles.pack()
        self.BarraDetalles.place(x=40,y=120)
        self.BarraDetalles.config(width=100, height=400)
        self.BarraDetalles.config(bg='black',borderwidth=1,highlightbackground = "black", highlightcolor= "black")
        atributos = ('Datos del objeto'+str(self.numeroDeObjeto)+':\n'+
                    'RA,DEC: '+str(lista_objetos.RA_DEC)+'\n'+
                    'z: '+str(lista_objetos.z)+'\n'+
                    'Tipo de espectro: '+str(lista_objetos.tipo_espectro))
        self.atrib = Label(self.BarraDetalles, text = atributos, anchor="e", justify=LEFT)
        self.atrib.pack()

        # Barra de opciones:
        self.opcTit = Frame(self.detalles)
        self.opcTit.pack()
        self.opcTit.place(x=40,y=210)
        self.Titulo = Label(self.opcTit, text=('Opciones:'))
        self.Titulo.config(font=("TimesNewRoman", 16))
        self.Titulo.config(bg='Azure3',borderwidth=1)
        self.Titulo.pack()
        self.OpsBg = Frame(self.detalles)
        self.OpsBg.pack()
        self.OpsBg.place(x=40,y=240)
        self.OpsBg.config(width=200, height=100)
        self.OpsBg.config(bg='white',borderwidth=1,highlightbackground = "black", highlightcolor= "black")
        self.Ops = Frame(self.detalles)
        self.Ops.pack()
        self.Ops.place(x=50,y=250)
        self.Ops.config(width=100, height=400)
        self.OpsBg.config(bg='white',borderwidth=1,highlightbackground = "black", highlightcolor= "black")
            # Botones:
        self.Map3D = Button(self.Ops, text="Ubicación en mapa 3D", command=self.Map3dim).pack()
        ############ Agregar texto entre botones
        self.quitarDetalles = Button(self.Ops, text="Regresar a mapa", command=self.closeWin).pack()
        self.atrib.pack()

        #   Grafica de espectros
        self.EspecDisplay = Frame(self.detalles)
        self.EspecDisplay.pack()
        self.EspecDisplay.place(x=250,y=90)
        df1 = oa.datos_espectro(lista_objetos)
        figure1 = plt.Figure(figsize=(5,5), dpi=100)
        ax1 = figure1.add_subplot(111)
        bar1 = FigureCanvasTkAgg(figure1, self.EspecDisplay)
        bar1.get_tk_widget().pack(side=LEFT, fill=BOTH)
        df1 = df1[['wavelengths','espectro']].groupby('wavelengths').sum() 
        df1.plot(kind='line', legend=True, ax=ax1)#'-k'
        ax1.set_title('Wavelengths Vs. espectro')


        
        self.detalles.mainloop()
    
    def Map3dim(self):
            gen.oneGraf_3D(self.pos,self.numeroDeObjeto-1)

    def closeWin(self):
            self.detalles.destroy()
            self.detalles.quit()
    


def main():
    mi_app = Map()
    return 0

if __name__ == '__main__':
    main()