from tkinter import *
from turtle import color

from pyparsing import col
import objast as oa
import puntos as gen
from functools import partial
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
from PIL import Image, ImageTk



class Map():
    def __init__(self):
        #####   NUMERO DE PUNTOS  #######
        self.n = 1000
        ## Detalles de ventana ##
        # Dimensiones de la ventana
        self.ventanaPrincipal = Tk(className='Mapa de objetos astronómicos')
        self.dimVentana = [1500,800]
        self.ventanaPrincipal.geometry(str(self.dimVentana[0])+'x'+str(self.dimVentana[1]))
        #Color de fondo
        self.ventanaPrincipal.config(bg='white')
        self.ventanaPrincipal.resizable(0,0)
        
        
        ##########  Barra superior ##########
        self.TopBg = Frame(self.ventanaPrincipal)
        self.TopBg.config(bg='dimgray',highlightbackground = "black", highlightcolor= "black")
        self.TopBg.place(x=0,y=0)
        self.TopBg.config(width=1500, height=80)
        self.TopBg.pack()
        self.TopBar = Frame(self.ventanaPrincipal)
        self.TopBar.pack()
        self.TopBar.place(x=50,y=10)
        self.TopBar.config(width=770, height=707)
        self.Titulo = Label(self.TopBar, text=('Generador de objetos astronómicos'), bg='white', fg='white', underline=0)
        self.Titulo.config(font=("Times", 30))
        self.Titulo.config(bg='dimgray',borderwidth=1)
        self.Titulo.pack()
        self.about = Frame(self.ventanaPrincipal)
        self.about.config(bg='aquamarine2',width=120, height=80)
        self.about.place(x=1380,y=0)
        self.ButtAbout = Button(self.ventanaPrincipal,bg='aquamarine2', text = 'About',font=("Times", 20),borderwidth=0,command=lambda:self.on_about())
        self.ButtAbout.place(x=1400,y=12)

        ##########  Panel lateral ##########
        self.Fil = Frame(self.ventanaPrincipal)
        # self.opcTit.grid(row = 2, column = 0)
        self.Fil.pack()
        self.Fil.place(x=13,y=88)
        self.Titulo = Label(self.Fil, text=('Filtro:                   '))
        self.Titulo.config(fg='black',font=("TimesNewRoman", 19))
        self.Titulo.config(bg='aquamarine2',borderwidth=1)
        self.Titulo.pack()

        self.BarraLateral = Frame(self.ventanaPrincipal)
        self.BarraLateral.pack()
        self.BarraLateral.config(bg='silver')
        self.BarraLateral.place(x=15,y=120)
        self.aplicar = Button(self.BarraLateral,text='Aplicar',font=("Times",11),command=lambda:self.apliFiltro(),bg='gainsboro')
        self.aplicar.grid(row= 3, column = 3)
        self.vacio = Label(self.BarraLateral, text = ' ', anchor="e", justify=LEFT,bg='silver')
        self.vacio.grid(row = 0, column = 0)
        self.vacio = Label(self.BarraLateral, text = ' ', anchor="e", justify=LEFT,bg='silver')
        self.vacio.grid(row = 0, column = 2)
        self.vacio = Label(self.BarraLateral, text = ' ', anchor="e", justify=LEFT,bg='silver')
        self.vacio.grid(row = 0, column = 5)
        self.var1 = IntVar()
        self.checkButt = Checkbutton(self.BarraLateral, text="Galaxia +",font=("Times",14), variable=self.var1,onvalue=1, offvalue=0,bg='silver')
        self.checkButt.grid(row= 1, column = 1)
        self.var2 = IntVar()
        self.checkButt = Checkbutton(self.BarraLateral, text="Galaxia -",font=("Times",14), variable=self.var2,onvalue=1, offvalue=0,bg='silver')
        self.checkButt.grid(row= 2, column = 1)
        self.var3 = IntVar()
        self.checkButt = Checkbutton(self.BarraLateral, text="Quasar +",font=("Times",14), variable=self.var3,onvalue=1, offvalue=0,bg='silver')
        self.checkButt.grid(row= 3, column = 1)
        self.var4 = IntVar()
        self.checkButt = Checkbutton(self.BarraLateral, text="Quasar -",font=("Times",14), variable=self.var4,onvalue=1, offvalue=0,bg='silver')
        self.checkButt.grid(row= 4, column = 1)
        self.vacio = Label(self.BarraLateral, text = ' ', anchor="e", justify=LEFT,bg='silver')
        self.vacio.grid(row = 8, column = 1)
        self.vacio = Label(self.BarraLateral, text = ' ', anchor="e", justify=LEFT,bg='silver')
        self.vacio.grid(row = 5, column = 1)
        self.salir = Label(self.BarraLateral, text = 'Salir del programa',font=("Times",11), anchor="e", justify=LEFT,bg='silver')
        self.salir.grid(row = 6, column = 1)
        self.quitar = Button(self.BarraLateral, text="Exit",font=("Times",13), command=self.killApp)
        self.quitar.grid(row= 7, column = 3)

    

        ##########  Grafica Mollweide con Botones ##########

        ## Frame del mapa ##
        self.principalFrame = Frame(self.ventanaPrincipal)
        self.principalFrame.pack()
        self.principalFrame.config(width=1100, height=505)
        self.principalFrame.place(x=240,y=105)
        self.principalFrame.config(bg='black')
        self.DimMap = [1366*0.9,690*0.9]
        self.canvas = Canvas(self.principalFrame, width=self.DimMap[0], height=self.DimMap[1])
        self.centroMap = [(1500/2-73)*0.9,(820/2-68)*0.9]
        self.canvas.pack()
        # Background Map
        image = Image.open(r"media/plotBackground.png").resize((1230,625))
        self.background = ImageTk.PhotoImage(image)
        self.background_id = self.canvas.create_image((0, 0), image=self.background, anchor='nw')
        
        # Position of each object
        self.lista_objetos = oa.generarObjetos(self.n)
        self.filtro()
        self.pos = oa.getpos(self.lista_objetos)
        self.xpos, self.ypos = gen.ang_to_mollweide(self.pos.T[0],self.pos.T[1])

        # Apply the filter and plot
        self.apliFiltro()

        self.ventanaPrincipal.mainloop()

    def on_click(self,pos,lista_objetos,nu):
            emergente = details(pos,lista_objetos,nu)
            return 0
    
    def on_about(self):
            emergente = aboutClass()
            return 0
    
    def killApp(self):
        self.ventanaPrincipal.quit()
    
    def filtro(self):
        self.galM = []
        self.galm = []
        self.QuaM = []
        self.Quam = []
        for obj in self.lista_objetos:
            if obj.tipo_objeto == 'GAL+':
                self.galM.append(self.lista_objetos.index(obj))
            elif obj.tipo_objeto == 'GAL-':
                self.galm.append(self.lista_objetos.index(obj))
            elif obj.tipo_objeto == 'QSO+':
                self.QuaM.append(self.lista_objetos.index(obj))
            else:
                self.Quam.append(self.lista_objetos.index(obj))
    
    def apliFiltro(self):
        self.button_img = PhotoImage(file='media/circle.png').subsample(60)
        indToPLot = []
        index = [self.galM,self.galm,self.QuaM,self.Quam]
        i = 0
        for con in [self.var1,self.var2,self.var3,self.var4]:
            if con.get() == 1:
                indToPLot += index[i]
                i += 1
          
        if len(indToPLot) == 0:
            for i in range(self.n):
                self.button = Button(self.principalFrame, image = self.button_img, bg='black',  borderwidth=0,
                                command=partial(self.on_click, self.pos,self.lista_objetos[i],i+1))
                self.button.place(x=self.centroMap[0]+self.xpos[i]*self.centroMap[0], y=self.centroMap[1]+self.ypos[i]*self.centroMap[1]*1.98)
        else:
            for i in indToPLot:
                self.button = Button(self.principalFrame, image = self.button_img, bg='black',  borderwidth=0,
                                command=partial(self.on_click, self.pos,self.lista_objetos[i],i+1))
                self.button.place(x=self.centroMap[0]+self.xpos[i]*self.centroMap[0], y=self.centroMap[1]+self.ypos[i]*self.centroMap[1]*1.98)
        
    
class details():
    def __init__(self, pos, lista_objetos, nu):
        self.pos = pos
        self.lista_objetos = lista_objetos
        self.numeroDeObjeto = nu
        self.detalles = Tk(className='Mapa de objetos astronómicos')
        self.dimVentana = [800,600]
        self.detalles.geometry(str(self.dimVentana[0])+'x'+str(self.dimVentana[1]))
        self.detalles.resizable(0,0)
        

        # Barra superior
        self.TopBg = Frame(self.detalles)
        self.TopBg.config(bg='dark slate gray',highlightbackground = "black", highlightcolor= "black")
        self.TopBg.place(x=15,y=1)
        self.TopBg.config(width=770, height=70)
        self.TopBg.pack()
        self.TopBar = Frame(self.detalles)
        self.TopBar.pack()
        self.TopBar.place(x=200,y=10)
        self.TopBar.config(width=770, height=707)
        self.Titulo = Label(self.TopBar, text=('Información de objeto '+str(self.numeroDeObjeto)))
        self.Titulo.config(fg='white',font=("TimesNewRoman", 30))
        self.Titulo.config(bg='dark slate gray',borderwidth=1)
        self.Titulo.pack()

        # Panel Lateral
        self.panelLateral = Frame(self.detalles)

            #Atributos del objeto astronomico:
        self.detTit = Frame(self.panelLateral)
        self.detTit.grid(row = 0, column = 0)
        self.detTit.pack()
        self.Titulo = Label(self.detTit, text=('Información técnica'))
        self.Titulo.config(fg='white',font=("TimesNewRoman", 16))
        self.Titulo.config(bg='dark slate gray',borderwidth=1)
        self.Titulo.pack()
        self.BarraDetalles = Frame(self.detalles)
        self.datosObj = Label(self.BarraDetalles, text = 'Datos del objeto', anchor="e", justify=LEFT,bg='white')
        self.datosObj.grid(row = 0, column = 0)
        self.datosObjVal = Label(self.BarraDetalles, text = self.numeroDeObjeto, anchor="e", justify=LEFT,bg='white')
        self.datosObjVal.grid(row = 0, column = 1)
        self.datosObj = Label(self.BarraDetalles, text = 'RA,DEC: ', anchor="e", justify=LEFT,bg='white')
        self.datosObj.grid(row = 1, column = 0)
        self.datosObjVal = Label(self.BarraDetalles, text = lista_objetos.RA_DEC.round(4), anchor="e", justify=LEFT,bg='white')
        self.datosObjVal.grid(row = 1, column = 1)
        self.datosObj = Label(self.BarraDetalles, text = 'Redshift: ', anchor="e", justify=LEFT,bg='white')
        self.datosObj.grid(row = 2, column = 0)
        self.datosObjVal = Label(self.BarraDetalles, text = lista_objetos.z.round(4), anchor="e", justify=LEFT,bg='white')
        self.datosObjVal.grid(row = 2, column = 1)
        self.datosObj = Label(self.BarraDetalles, text = 'Tipo de onjeto: ', anchor="e", justify=LEFT,bg='white')
        self.datosObj.grid(row = 3, column = 0)
        self.datosObjVal = Label(self.BarraDetalles, text = lista_objetos.tipo_objeto, anchor="e", justify=LEFT,bg='white')
        self.datosObjVal.grid(row = 3, column = 1)
        # self.BarraDetalles.grid(row = 1, column = 0)
        self.BarraDetalles.pack()
        self.BarraDetalles.place(x=40,y=120)
        self.BarraDetalles.config(width=100, height=400)
        self.BarraDetalles.config(bg='white',borderwidth=1,highlightbackground = "white", highlightcolor= "white")

        # Barra de opciones:
        self.opcTit = Frame(self.detalles)
        # self.opcTit.grid(row = 2, column = 0)
        self.opcTit.pack()
        self.opcTit.place(x=30,y=220)
        self.Titulo = Label(self.opcTit, text=('Opciones:                  '))
        self.Titulo.config(fg='white',font=("TimesNewRoman", 16))
        self.Titulo.config(bg='dark slate gray',borderwidth=1)
        self.Titulo.pack()
        # self.OpsBg = Frame(self.detalles)
        # self.OpsBg.pack()
        # self.OpsBg.place(x=40,y=240)
        # self.OpsBg.config(width=200, height=100)
        # self.OpsBg.config(bg='white',borderwidth=1,highlightbackground = "black", highlightcolor= "black")

        #Panel de opciones
        self.Ops = Frame(self.detalles)
        self.Map3D = Button(self.Ops, text="Ubicación en mapa 3D",font=("Times",12), command=self.Map3dim, bg = 'gainsboro')
        self.Map3D.grid(row = 0, column = 0)
        self.descri = Label(self.Ops, text=('*despliega una grafica en 3D que \nrepresenta la bobeda celeste y los \nobjetos observados en ella. El objeto \n seleccionado aparecerá de color rojo.'))
        self.descri.config(font=("TimesNewRoman", 8),bg= 'white')
        self.descri.grid(row = 1, column = 0)
        self.quitarDetalles = Button(self.Ops, text="Regresar a mapa",font=("Times",12), command=self.closeWin, bg = 'gainsboro')
        self.quitarDetalles.grid(row = 2, column = 0)
        self.descri = Label(self.Ops, text=('**Regresa al mapa con todos los objetos.'))
        self.descri.config(font=("TimesNewRoman", 8),bg= 'white')
        self.descri.grid(row = 3, column = 0)
        self.Ops.pack()
        self.Ops.place(x=30,y=250)
        self.Ops.config(width=100, height=400)
        self.Ops.config(bg='white',borderwidth=1,highlightbackground = "black", highlightcolor= "black")
        
        self.panelLateral.pack()
        self.panelLateral.place(x=40,y=90)
        

        #   Grafica de espectros
        self.EspecDisplay = Frame(self.detalles)
        self.EspecDisplay.pack()
        self.EspecDisplay.place(x=250,y=90)
        df1 = oa.datos_espectro(lista_objetos)
        figure1 = plt.Figure(figsize=(5,4), dpi=100)
        ax1 = figure1.add_subplot(111)
        ax1.set_title('Wavelengths Vs. espectro')
        bar1 = FigureCanvasTkAgg(figure1, self.EspecDisplay)
        bar1.get_tk_widget().pack()
        df1 = df1[['wavelengths','espectro']].groupby('wavelengths').sum() 
        df1.plot(kind='line', legend=False, ax=ax1, color= 'black')#'-k'
        
        
        self.detalles.mainloop()
    
    def Map3dim(self):
        
        gen.oneGraf_3D(self.pos,self.numeroDeObjeto-1)

    def closeWin(self):
        self.detalles.destroy()
        self.detalles.quit()
    
class aboutClass():
    def __init__(self):
        self.AboutWin = Tk(className='Mapa de objetos astronómicos')
        self.dimVentana = [800,600]
        self.AboutWin.geometry(str(self.dimVentana[0])+'x'+str(self.dimVentana[1]))
        self.AboutWin.resizable(0,0)
        

        # Barra superior
        self.TopBg = Frame(self.AboutWin)
        self.TopBg.config(bg='dark slate gray',highlightbackground = "black", highlightcolor= "black")
        self.TopBg.place(x=15,y=1)
        self.TopBg.config(width=770, height=20)
        self.TopBg.pack()
        desctiption = 'Este programa hace muchas cosas'
        self.descrip = Label(self.AboutWin,text=desctiption,font=('Times',20)).pack()

        creditos = 'El programa fue elaborado por:'
        self.credi = Label(self.AboutWin,text=creditos,font=('Times',18)).pack()
        creditos = 'Uriel Chavez Flores\nBaruch Mejía Martinez'
        self.credi = Label(self.AboutWin,text=creditos,font=('Times',15)).pack()

        self.quitarAbout = Button(self.AboutWin, text="Regresar a mapa",font=("Times",12), command=self.closeWin, bg = 'gainsboro').pack()
        
        self.AboutWin.mainloop()
    def Map3dim(self):
        
        gen.oneGraf_3D(self.pos,self.numeroDeObjeto-1)

    def closeWin(self):
        self.AboutWin.destroy()
        self.AboutWin.quit()


def main():
    mi_app = Map()
    return 0

if __name__ == '__main__':
    main()