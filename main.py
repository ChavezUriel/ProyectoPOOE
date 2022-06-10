from tkinter import *
import objast as oa
from functools import partial
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
from PIL import Image, ImageTk


# Variables globales



ret_args = []

n_obj = []

fields_custom = 'Cuásar z < 2.1', 'Cuásar z > 2.1', 'Galaxia z < 2.1', 'Galaxia z > 2.1'

fields = ['Cantidad de objetos']


# Funciones del menú de preferencias 

# Verificación de ingreso de solo digitos
def only_numbers(char):
    return char.isdigit()

# Limitación de cantidad de objetos
def character_limit(entry_text, lim):
    if (only_numbers(entry_text.get())):
        if (int(entry_text.get()) > lim):
            entry_text.set(lim)
    else:
        entry_text.set(entry_text.get()[:-1])

# Guardar cantidades ingresadas
def save_data(entries,root):
    global n_obj
    for entry in entries:
        text  = entry.get()
        n_obj.append(int(text))
    formato_args()
    root.destroy()
    Map(ret_args)
    
# Escribir en el formato necesario las cantidades ingresadas
def formato_args():
    global ret_args
    if(len(n_obj) == 4):
        ret_args = [0,True,int(n_obj[0]),int(n_obj[1]),int(n_obj[2]),int(n_obj[3])]
    else:
        ret_args = [int(n_obj[0]),False,0,0,0,0]


# Sección de cantidades personalizadas del menu de preferencias
class menu_custom_objs():
    def __init__(self, frame, root):
        
        lab1 = Label(frame, text=fields_custom[0]+": ", anchor='e')
        entry_text1 = StringVar()
        ent1 = Entry(frame, textvariable = entry_text1)
        entry_text1.trace("w", lambda *args: character_limit(entry_text1,500))
        lab1.grid(row=1,column=0, sticky="nse", padx=5, pady=5)
        ent1.grid(row=1,column=1, sticky="nsw", padx=5, pady=5)
        
        lab2 = Label(frame, text=fields_custom[1]+": ", anchor='e')
        entry_text2 = StringVar()
        ent2 = Entry(frame, textvariable = entry_text2)
        entry_text2.trace("w", lambda *args: character_limit(entry_text2,500))
        lab2.grid(row=2,column=0, sticky="nse", padx=5, pady=5)
        ent2.grid(row=2,column=1, sticky="nsw", padx=5, pady=5)
        
        lab3 = Label(frame, text=fields_custom[2]+": ", anchor='e')
        entry_text3 = StringVar()
        ent3 = Entry(frame, textvariable = entry_text3)
        entry_text3.trace("w", lambda *args: character_limit(entry_text3,500))
        lab3.grid(row=3,column=0, sticky="nse", padx=5, pady=5)
        ent3.grid(row=3,column=1, sticky="nsw", padx=5, pady=5)
        
        lab4 = Label(frame, text=fields_custom[3]+": ", anchor='e')
        entry_text4 = StringVar()
        ent4 = Entry(frame, textvariable = entry_text4)
        entry_text4.trace("w", lambda *args: character_limit(entry_text4,500))
        lab4.grid(row=4,column=0, sticky="nse", padx=5, pady=5)
        ent4.grid(row=4,column=1, sticky="nsw", padx=5, pady=5)
        
        ents = [ent1, ent2, ent3, ent4]
        
        frame.bind('<Return>', (lambda event, e=ents: save_data(e,frame)))
        b1 = Button(frame, text='Generar', command=(lambda e=ents: save_data(e,root)))
        b1.grid(row=5, column=0, columnspan=2, padx=5, pady=5)

# Sección de cantidades estandar del menu de preferencias
class menu_estandar_objs():
    def __init__(self, frame, root):
        
        lab1 = Label(frame, text=fields_custom[0]+": ", anchor='e')
        entry_text1 = StringVar()
        ent1 = Entry(frame, textvariable = entry_text1)
        entry_text1.trace("w", lambda *args: character_limit(entry_text1,2000))
        lab1.grid(row=2,column=0, sticky="nse", padx=10, pady=10)
        ent1.grid(row=2,column=1, sticky="nsw", padx=10, pady=10)
        
        ents = [ent1]
        
        frame.bind('<Return>', (lambda event, e=ents: save_data(e,frame)))   
        b1 = Button(frame, text='Generar', command=(lambda e=ents: save_data(e,root)))
        b1.grid(columnspan=2, padx=10, pady=10)

# Ventana de más información sobre generación de datos
def mas_info_ventana():
    root = Tk()
    root.geometry('1200x500+100+100')
    root.title('Información de generación predeterminada')
    root.resizable(False,False)
    #root.option_add( "*font", "Segoe 12" )
    
    mainFrame = Frame(root)
    mainFrame.pack(padx=20, pady=20, fill="both", expand=True)

    mainFrame.rowconfigure(0, weight=1)
    mainFrame.columnconfigure(0, weight=1)
    
    Label(mainFrame, text="Información de generación predeterminada", font="bold").grid(row=0, column=0, columnspan=2, sticky="nswe")    
    
    frame_ratio = Frame(mainFrame)
    frame_ratio.grid(row=1,column=0, sticky="ns")
    frame_z = Frame(mainFrame)
    frame_z.grid(row=1,column=1, sticky="ns")
    
    Message(frame_ratio, 
               text="La razón entre cuásares y galaxias se asumió como una distribución normal.", 
               justify="center",
               width=410).grid(row=1, column=0, sticky="nswe", pady=5)
    Message(frame_ratio, 
               text="La media y desviación de la distribución se obtuvo de datos de 10 catalogos de observación del proyecto SDSS (Sloan Digital Sky Survey).", 
               justify="center",
               width=410).grid(row=2, column=0, sticky="nswe", pady=5)
    Message(frame_ratio, 
               text="Media = 0.376", 
               justify="center",
               width=410).grid(row=3, column=0, sticky="nswe", pady=5)
    Message(frame_ratio, 
               text="Desviación estándar = 0.043", 
               justify="center",
               width=410).grid(row=4, column=0, sticky="nswe", pady=5)
    
    im_razon = Canvas(frame_ratio, width = 500, height = 200)  
    im_razon.grid(row=6, column=0, padx=10, pady=10)  
    img1 = ImageTk.PhotoImage(Image.open("media/Razon_QSO-GAL.png"), master = im_razon)  
    im_razon.create_image(250, 100, anchor="c", image=img1)  
    
    Message(frame_z, 
               text="La distribución de los objetos en el corrimiento al rojo es una distribución obtenida mediante KDE (Kernel Distribution Estimation) con el conjunto de datos experimentales utilizados para la generación de espectros.", 
               justify="center",
               width=410).grid(row=0, column=0, sticky="nswe", pady=5)
    
    im_distz = Canvas(frame_z, width = 500, height = 200)
    im_distz.grid(row=1, column=0, pady=10, padx=10, sticky="ns")
    img2 = ImageTk.PhotoImage(Image.open("media/dist_z.png"), master = im_distz)
    im_distz.create_image(250, 100, anchor="c", image=img2)
    
    root.mainloop()

# Ventana principal de menu de preferencias
class menu_prefs():
    def __init__(self):
        root = Tk()
        icono = PhotoImage(file='media/icono.png')
        root.iconphoto(False, icono)
        root.geometry('1000x320+100+100')
        root.title('Preferencias')
        root.resizable(False,False)
        #root.option_add( "*font", "Segoe 12" )
        
        mainFrame = Frame(root)
        mainFrame.pack(padx=20, pady=20, fill="both", expand=True)
        
        titulo = Label(mainFrame, text="Preferencias", font="bold")
        titulo.grid(row=0, column=0, columnspan=2, sticky="nswe", padx=20, pady=20)
        
                            
        frame_estandar = Frame(mainFrame)
        frame_estandar.grid(row = 1, column=0, sticky="nsw")
        
        label_estandar = Label(frame_estandar, width=60, text="Generar objetos con razón entre galaxias y cuásares preestablecida.")
        label_estandar.grid(columnspan=2, padx=10, pady=10)
        
        mas_info = Button(frame_estandar, text="Más información", command=mas_info_ventana)
        mas_info.grid(columnspan=2, padx=10, pady=10)
        
        menu_estandar_objs(frame_estandar, root)
        
        
        frame_custom = Frame(mainFrame)
        frame_custom.grid(row = 1, column=1, sticky="nse")
        
        label_custom = Label(frame_custom, width=60, text="Generar objetos en cantidades personalizadas.")
        label_custom.grid(columnspan=2, padx=10, pady=10)
        
        menu_custom_objs(frame_custom, root)
        
        
        root.mainloop()


# Ventana de mapa mostrando objetos
class Map():
    def __init__(self,lista_objs_args):
        #####   Lista de objetos  #######
        
        
        self.lista_objetos = oa.generarObjetos(lista_objs_args[0],lista_objs_args[1],lista_objs_args[2],lista_objs_args[3],lista_objs_args[4],lista_objs_args[5])
        
        self.n = lista_objs_args[0] + lista_objs_args[2] + lista_objs_args[3] + lista_objs_args[4] + lista_objs_args[5]
        ## Detalles de ventana ##
        # Dimensiones de la ventana
        self.ventanaPrincipal = Tk(className='Generador de objetos astronómicos')
        icono = PhotoImage(file='media/icono.png')
        self.ventanaPrincipal.iconphoto(False, icono)
        self.ventanaPrincipal.title("Generador de objetos astronómicos")
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
        self.TopBar = Frame(self.ventanaPrincipal)
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
        self.ButtAbout.place(x=1395,y=13)

        ##########  Panel lateral ##########
        self.Fil = Frame(self.ventanaPrincipal)
        # self.opcTit.grid(row = 2, column = 0)
        self.Fil.place(x=13,y=88)
        self.Titulo = Label(self.Fil, text=('Filtro'), width=12)
        self.Titulo.config(fg='black',font=("TimesNewRoman", 19))
        self.Titulo.config(bg='aquamarine2',borderwidth=1)
        self.Titulo.pack()

        self.BarraLateral = Frame(self.ventanaPrincipal)
        self.BarraLateral.config(bg='silver')
        self.BarraLateral.place(x=16,y=120)
        
        self.vacio = Label(self.BarraLateral, text = ' ', anchor="e", justify=LEFT,bg='silver')
        self.vacio.grid(row = 0, column = 0)
        self.vacio = Label(self.BarraLateral, text = ' ', anchor="e", justify=LEFT,bg='silver')
        self.vacio.grid(row = 0, column = 2)
        self.vacio = Label(self.BarraLateral, text = ' ', anchor="e", justify=LEFT,bg='silver')
        self.vacio.grid(row = 0, column = 5)
        
        self.var1 = IntVar()
        self.checkButt = Checkbutton(self.BarraLateral, text="Cuásar -",font=("Times",14), variable=self.var1,onvalue=1, offvalue=0,bg='silver')
        self.checkButt.grid(row= 1, column = 1, sticky="w", padx=10)
        self.var2 = IntVar()
        self.checkButt = Checkbutton(self.BarraLateral, text="Cuásar +",font=("Times",14), variable=self.var2,onvalue=1, offvalue=0,bg='silver')
        self.checkButt.grid(row= 2, column = 1, sticky="w", padx=10)
        self.var3 = IntVar()
        self.checkButt = Checkbutton(self.BarraLateral, text="Galaxia -",font=("Times",14), variable=self.var3,onvalue=1, offvalue=0,bg='silver')
        self.checkButt.grid(row= 3, column = 1, sticky="w", padx=10)
        self.var4 = IntVar()
        self.checkButt = Checkbutton(self.BarraLateral, text="Galaxia +",font=("Times",14), variable=self.var4,onvalue=1, offvalue=0,bg='silver')
        self.checkButt.grid(row= 4, column = 1, sticky="w", padx=10)
        
        
        self.aplicar = Button(self.BarraLateral,text='Aplicar',font=("Times",13),command=lambda:self.apliFiltro(),bg='gainsboro')
        self.aplicar.grid(row= 5, column = 1, columnspan=3, sticky="we", padx=10, pady=10)
        
        self.vacio = Label(self.BarraLateral, text = ' ', anchor="e", justify=LEFT,bg='silver')
        self.vacio.grid(row = 8, column = 1)
        self.quitar = Button(self.BarraLateral, text="Salir del programa",font=("Times",13),command=self.killApp,bg='gainsboro')
        self.quitar.grid(row= 6, column = 1, columnspan=3, sticky="we", padx=10, pady=10)

    

        ##########  Grafica Mollweide con Botones ##########

        ## Frame del mapa ##
        self.principalFrame = Frame(self.ventanaPrincipal)
        self.principalFrame.config(width=1100, height=505)
        self.principalFrame.place(x=240,y=105)
        self.principalFrame.config(bg='white')
        self.DimMap = [1366*0.9,690*0.9]
        self.canvas = Canvas(self.principalFrame, width=self.DimMap[0], height=self.DimMap[1], bg="white", highlightthickness=0)
        self.centroMap = [(1500/2-73)*0.9,(820/2-68)*0.9]
        self.canvas.pack()
        # Background Map
        image = Image.open(r"media/plotBackground.png").resize((1230,625))
        self.background = ImageTk.PhotoImage(image)
        self.background_id = self.canvas.create_image((0, 0), image=self.background, anchor='nw')
        
        # Position of each object
        self.filtro()
        self.pos = oa.getpos(self.lista_objetos)
        self.xpos, self.ypos = oa.ang_to_mollweide(self.pos.T[0],self.pos.T[1])

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
        self.button_img = PhotoImage(file='media/circle.png').subsample(300)
        indToPLot = []
        index = [self.Quam,self.QuaM,self.galm,self.galM]
        i = 0
        for con in [self.var1,self.var2,self.var3,self.var4]:
            if con.get() == 1:
                indToPLot += index[i]
            i += 1
          
        if len(indToPLot) == 0:
            for i in range(self.n):
                self.button = Button(self.principalFrame, image = self.button_img, bg="black", borderwidth=0,
                                command=partial(self.on_click, self.pos,self.lista_objetos[i],i+1))
                self.button.place(x=self.centroMap[0]+self.xpos[i]*self.centroMap[0], y=self.centroMap[1]+self.ypos[i]*self.centroMap[1]*1.98)
        else:
            for i in indToPLot:
                self.button = Button(self.principalFrame, image = self.button_img, bg="black", borderwidth=0,
                                command=partial(self.on_click, self.pos,self.lista_objetos[i],i+1))
                self.button.place(x=self.centroMap[0]+self.xpos[i]*self.centroMap[0], y=self.centroMap[1]+self.ypos[i]*self.centroMap[1]*1.98)
        

# Ventana de detalles sobre objeto seleccionado
class details():
    def __init__(self, pos, lista_objetos, nu):
        self.pos = pos
        self.lista_objetos = lista_objetos
        self.numeroDeObjeto = nu
        self.detalles = Tk(className='Generador de objetos astronómicos')
        
        
        self.detalles.title("Generador de objetos astronómicos")
        # self.dimVentana = [900,600]
        # self.detalles.geometry(str(self.dimVentana[0])+'x'+str(self.dimVentana[1]))
        self.detalles.resizable(0,0)
        

        # Barra superior
        self.TopBar = Frame(self.detalles, bg='dark slate gray')
        self.TopBar.grid(row=0, column=0, columnspan=2, sticky="nswe")
        
        self.Titulo = Label(self.TopBar, text=('Información de objeto '+str(self.numeroDeObjeto)))
        self.Titulo.config(fg='white',font=("TimesNewRoman", 30),bg='dark slate gray')
        self.Titulo.pack(pady=20)

        # Panel Lateral
        self.panelLateral = Frame(self.detalles, width=100)
        self.panelLateral.grid(row=1, column=0, padx=20, pady=20)
        
        #Atributos del objeto astronomico:t=10
        self.detTit = Frame(self.panelLateral,bg='dark slate gray')
        self.detTit.pack(fill="x")
        self.Titulo = Label(self.detTit, text=('Información técnica'),fg='white',font=("TimesNewRoman", 16),bg='dark slate gray')
        self.Titulo.pack(padx=10, pady=10)
        
        self.BarraDetalles = Frame(self.panelLateral)
        self.datosObj = Label(self.BarraDetalles, text = 'ID:', bg='white',font=("Arial",12))
        self.datosObj.grid(row = 0, column = 0, sticky="e", padx=1, pady=2)
        self.datosObjVal = Label(self.BarraDetalles, text = self.numeroDeObjeto, bg='white',font=("Arial",12))
        self.datosObjVal.grid(row = 0, column = 1, sticky="w", padx=1, pady=2)
        self.datosObj = Label(self.BarraDetalles, text = 'RA,DEC: ', bg='white',font=("Arial",12))
        self.datosObj.grid(row = 1, column = 0, sticky="e", padx=1, pady=2)
        self.datosObjVal = Label(self.BarraDetalles, text = lista_objetos.RA_DEC.round(4), bg='white',font=("Arial",12))
        self.datosObjVal.grid(row = 1, column = 1, sticky="w", padx=1, pady=2)
        self.datosObj = Label(self.BarraDetalles, text = 'Redshift: ', bg='white',font=("Arial",12))
        self.datosObj.grid(row = 2, column = 0, sticky="e", padx=1, pady=2)
        self.datosObjVal = Label(self.BarraDetalles, text = lista_objetos.z.round(4), bg='white',font=("Arial",12))
        self.datosObjVal.grid(row = 2, column = 1, sticky="w", padx=1, pady=2)
        self.datosObj = Label(self.BarraDetalles, text = 'Tipo de objeto: ', bg='white',font=("Arial",12))
        self.datosObj.grid(row = 3, column = 0, sticky="e")
        self.datosObjVal = Label(self.BarraDetalles, text = lista_objetos.tipo_objeto, bg='white',font=("Arial",12))
        self.datosObjVal.grid(row = 3, column = 1, sticky="w", padx=1, pady=2)
        self.BarraDetalles.config(width=100, height=400)
        self.BarraDetalles.config(bg='white',borderwidth=1,highlightbackground = "white", highlightcolor= "white")
        self.BarraDetalles.pack()
        
        self.vacio = Label(self.panelLateral, text=" ")
        self.vacio.pack()
        
        # Barra de opciones:
        self.opcTit = Frame(self.panelLateral,bg='dark slate gray')
        self.opcTit.pack(fill="x")
        self.Titulo = Label(self.opcTit, text=('Opciones'), fg='white',font=("TimesNewRoman", 16),bg='dark slate gray')
        self.Titulo.pack(pady=10)
        

        #Panel de opciones
        self.Ops = Frame(self.panelLateral)
        self.Ops.config(width=100, height=400)
        self.Ops.config(bg='white',borderwidth=1,highlightbackground = "black", highlightcolor= "black")
        self.Ops.pack(fill="x")

        self.Map3D = Button(self.Ops, text="Ubicación en mapa 3D",font=("Times",12), command=self.Map3dim, bg = 'gainsboro')
        self.Map3D.pack(padx=10, pady=10)
        self.descri = Label(self.Ops, text=('Despliega una gráfica en 3D que \nrepresenta la bóveda celeste y los \nobjetos observados en ella. El objeto \n seleccionado aparecerá de color rojo.'))
        self.descri.config(font=("TimesNewRoman", 8),bg= 'white')
        self.descri.pack(fill="x")
        self.quitarDetalles = Button(self.Ops, text="Regresar a mapa",font=("Times",12), command=self.closeWin, bg = 'gainsboro')
        self.quitarDetalles.pack(padx=10, pady=10)
        self.descri = Label(self.Ops, text=('Regresa al mapa con todos los objetos.'))
        self.descri.config(font=("TimesNewRoman", 8),bg= 'white')
        self.descri.pack(fill="x")
        

        #   Grafica de espectros       
        self.EspecDisplay = Frame(self.detalles, bg="white")
        self.EspecDisplay.grid(row=1, column=1, padx=20, pady=20, sticky="nswe")
        
        self.espTitFrame = Frame(self.EspecDisplay,bg='dark slate gray')
        self.espTitFrame.pack(fill="x")
        self.espTitulo = Label(self.espTitFrame, text=('Espectro'), fg='white',font=("TimesNewRoman", 16),bg='dark slate gray')
        self.espTitulo.pack(pady=10)
        
        
        df1 = oa.datos_espectro(lista_objetos)
        
        figure1, ax1 = plt.subplots(figsize=(5,2.2), dpi=140)
        ax1.plot(df1["wavelengths"], df1["espectro"], color='black')
        ax1.set_ylabel("Flujo")
        ax1.set_xlabel(r"Longitud de onda $\left[Å\right]$")
        plt.tight_layout()
        bar1 = FigureCanvasTkAgg(figure1, self.EspecDisplay)
        bar1.get_tk_widget().pack(fill="x", expand=True)
        plt.close()
        self.detalles.mainloop()
    
    def Map3dim(self):
        while(plt.get_fignums()):
            plt.close(plt.get_fignums()[0])
        oa.oneGraf_3D(self.pos,self.numeroDeObjeto-1)

    def closeWin(self):
        self.detalles.destroy()
        self.detalles.quit()

# Ventana de descripción del programa
class aboutClass():
    def __init__(self):
        self.AboutWin = Tk(className='Generador de objetos astronómicos')
        self.AboutWin.title("Generador de objetos astronómicos")
        self.dimVentana = [800,600]
        self.AboutWin.geometry(str(self.dimVentana[0])+'x'+str(self.dimVentana[1]))
        self.AboutWin.resizable(0,0)
        

        # Barra superior
        self.TopBg = Frame(self.AboutWin,bg='dark slate gray')
        self.TopBg.pack(fill="x", side="top")
        self.TituloAbout = Label(self.TopBg, text="Descripción del prorgrama",bg='dark slate gray',fg='white',font=("TimesNewRoman", 20))
        self.TituloAbout.pack(pady=20)
        
        with open("archivos/description.txt", encoding='utf8') as f:
            text = f.readlines()
        f.close()
             
        for i in range(len(text)):
            Label(self.AboutWin,text=text[i],wraplength = 700,font=('Times',16)).pack(padx=20, pady=5)
        

        creditos = 'El programa fue elaborado por:'
        Label(self.AboutWin,text=creditos,font=('Times',18)).pack(pady=5)
        creditos = 'Uriel Chavez Flores\nBaruch Mejía Martinez\nFernando Emanuel Trujillo Cándido'
        Label(self.AboutWin,text=creditos,font=('Times',15)).pack(pady=5)

        self.quitarAbout = Button(self.AboutWin, text="Regresar a mapa",font=("Times",12), command=self.closeWin, bg = 'gainsboro').pack()
        
        self.AboutWin.mainloop()

    def closeWin(self):
        self.AboutWin.destroy()
        self.AboutWin.quit()


#Ejecución del menú de preferencias que da inicio al funcionamiento del programa
menu_prefs()
