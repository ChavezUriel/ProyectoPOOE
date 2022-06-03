import tkinter as tk
from PIL import ImageTk, Image
from pip import main

from pyparsing import col
from yaml import AnchorToken

def only_numbers(char):
    return char.isdigit()

def character_limit(entry_text, lim):
    if (only_numbers(entry_text.get())):
        if (int(entry_text.get()) > lim):
            entry_text.set(lim)
    else:
        entry_text.set(entry_text.get()[:-1])

def save_data(entries,root):
    global n_obj
    for entry in entries:
        text  = entry.get()
        n_obj.append(int(text))
    formato_args()
    root.destroy()

def formato_args():
    global ret_args
    if(len(n_obj) == 4):
        ret_args = [0,True,int(n_obj[0]),int(n_obj[1]),int(n_obj[2]),int(n_obj[3])]
    else:
        ret_args = [int(n_obj[0]),False,0,0,0,0]

def makeform(root, fields):
    entries = []
    if(len(fields) == 4):
        lim = 2500
    else:
        lim = 10000
    entry_text = []
    for i in range(len(fields)):
        row = tk.Frame(root)
        # row.rowconfigure(0, weight=1)
        # row.columnconfigure(0, weight=1)
        lab = tk.Label(row, text=fields[i]+": ", anchor='e')
        entry_text.append(tk.StringVar())
        ent = tk.Entry(row, textvariable = entry_text[i])
        entry_text[i].trace("w", lambda *args: character_limit(entry_text,lim))
        row.pack(side=tk.TOP, fill=tk.Y, padx=10, pady=10)
        lab.grid(row=0,column=0, sticky="e")
        ent.grid(row=0,column=1, sticky="w")
        entries.append((fields[i], ent))
    return entries


ret_args = []

n_obj = []

fields_custom = 'Cuásar z < 2.1', 'Cuásar z > 2.1', 'Galaxia z < 2.1', 'Galaxia z > 2.1'

class menu_custom_objs():
    def __init__(self, frame, root):
        ents = makeform(frame, fields_custom)
        frame.bind('<Return>', (lambda event, e=ents: save_data(e,frame)))
        b1 = tk.Button(frame, text='Generar', command=(lambda e=ents: save_data(e,root)))
        b1.pack(side=tk.BOTTOM, padx=5, pady=5)


class menu_custom_objs():
    def __init__(self, frame, root):
        
        lab1 = tk.Label(frame, text=fields_custom[0]+": ", anchor='e')
        entry_text1 = tk.StringVar()
        ent1 = tk.Entry(frame, textvariable = entry_text1)
        entry_text1.trace("w", lambda *args: character_limit(entry_text1,2500))
        lab1.grid(row=1,column=0, sticky="nse", padx=5, pady=5)
        ent1.grid(row=1,column=1, sticky="nsw", padx=5, pady=5)
        
        lab2 = tk.Label(frame, text=fields_custom[1]+": ", anchor='e')
        entry_text2 = tk.StringVar()
        ent2 = tk.Entry(frame, textvariable = entry_text2)
        entry_text2.trace("w", lambda *args: character_limit(entry_text2,2500))
        lab2.grid(row=2,column=0, sticky="nse", padx=5, pady=5)
        ent2.grid(row=2,column=1, sticky="nsw", padx=5, pady=5)
        
        lab3 = tk.Label(frame, text=fields_custom[2]+": ", anchor='e')
        entry_text3 = tk.StringVar()
        ent3 = tk.Entry(frame, textvariable = entry_text3)
        entry_text3.trace("w", lambda *args: character_limit(entry_text3,2500))
        lab3.grid(row=3,column=0, sticky="nse", padx=5, pady=5)
        ent3.grid(row=3,column=1, sticky="nsw", padx=5, pady=5)
        
        lab4 = tk.Label(frame, text=fields_custom[3]+": ", anchor='e')
        entry_text4 = tk.StringVar()
        ent4 = tk.Entry(frame, textvariable = entry_text4)
        entry_text4.trace("w", lambda *args: character_limit(entry_text4,2500))
        lab4.grid(row=4,column=0, sticky="nse", padx=5, pady=5)
        ent4.grid(row=4,column=1, sticky="nsw", padx=5, pady=5)
        
        ents = [ent1, ent2, ent3, ent4]
        
        frame.bind('<Return>', (lambda event, e=ents: save_data(e,frame)))
        b1 = tk.Button(frame, text='Generar', command=(lambda e=ents: save_data(e,root)))
        b1.grid(row=5, column=0, columnspan=2, padx=5, pady=5)


fields = ['Cantidad de objetos']

class menu_estandar_objs():
    def __init__(self, frame, root):
        
        lab1 = tk.Label(frame, text=fields_custom[0]+": ", anchor='e')
        entry_text1 = tk.StringVar()
        ent1 = tk.Entry(frame, textvariable = entry_text1)
        entry_text1.trace("w", lambda *args: character_limit(entry_text1,10000))
        lab1.grid(row=2,column=0, sticky="nse", padx=10, pady=10)
        ent1.grid(row=2,column=1, sticky="nsw", padx=10, pady=10)
        
        ents = [ent1]
        
        frame.bind('<Return>', (lambda event, e=ents: save_data(e,frame)))   
        b1 = tk.Button(frame, text='Generar', command=(lambda e=ents: save_data(e,root)))
        b1.grid(columnspan=2, padx=10, pady=10)


def mas_info_ventana():
    root = tk.Tk()
    root.geometry('1200x500+100+100')
    root.title('Información de generación predeterminada')
    root.resizable(False,False)
    #root.option_add( "*font", "Segoe 12" )
    
    mainFrame = tk.Frame(root)
    mainFrame.pack(padx=20, pady=20, fill="both", expand=True)

    mainFrame.rowconfigure(0, weight=1)
    mainFrame.columnconfigure(0, weight=1)
    
    tk.Label(mainFrame, text="Información de generación predeterminada", font="bold").grid(row=0, column=0, columnspan=2, sticky="nswe")    
    
    frame_ratio = tk.Frame(mainFrame)
    frame_ratio.grid(row=1,column=0, sticky="ns")
    frame_z = tk.Frame(mainFrame)
    frame_z.grid(row=1,column=1, sticky="ns")
    
    tk.Message(frame_ratio, 
               text="La razón entre cuásares y galaxias se asumió como una distribución normal.", 
               justify="center",
               width=410).grid(row=1, column=0, sticky="nswe", pady=5)
    tk.Message(frame_ratio, 
               text="La media y desviación de la distribución se obtuvo de datos de 10 catalogos de observación del proyecto SDSS (Sloan Digital Sky Survey).", 
               justify="center",
               width=410).grid(row=2, column=0, sticky="nswe", pady=5)
    tk.Message(frame_ratio, 
               text="Media = 0.376", 
               justify="center",
               width=410).grid(row=3, column=0, sticky="nswe", pady=5)
    tk.Message(frame_ratio, 
               text="Desviación estándar = 0.043", 
               justify="center",
               width=410).grid(row=4, column=0, sticky="nswe", pady=5)
    
    im_razon = tk.Canvas(frame_ratio, width = 500, height = 200)  
    im_razon.grid(row=6, column=0, padx=10, pady=10)  
    img1 = ImageTk.PhotoImage(Image.open("media/Razon_QSO-GAL.png"), master = im_razon)  
    im_razon.create_image(250, 100, anchor="c", image=img1)  
    
    tk.Message(frame_z, 
               text="La distribución de los objetos en el corrimiento al rojo es una distribución obtenida mediante KDE (Kernel Distribution Estimation) con el conjunto de datos experimentales utilizados para la generación de espectros.", 
               justify="center",
               width=410).grid(row=0, column=0, sticky="nswe", pady=5)
    
    im_distz = tk.Canvas(frame_z, width = 500, height = 200)
    im_distz.grid(row=1, column=0, pady=10, padx=10, sticky="ns")
    img2 = ImageTk.PhotoImage(Image.open("media/dist_z.png"), master = im_distz)
    im_distz.create_image(250, 100, anchor="c", image=img2)
    
    root.mainloop()


class ventana_principal():
    def __init__(self):
        root = tk.Tk()
        root.geometry('1000x320+100+100')
        root.title('Preferencias')
        root.resizable(False,False)
        #root.option_add( "*font", "Segoe 12" )
        
        mainFrame = tk.Frame(root)
        mainFrame.pack(padx=20, pady=20, fill="both", expand=True)
        
        titulo = tk.Label(mainFrame, text="Preferencias", font="bold")
        titulo.grid(row=0, column=0, columnspan=2, sticky="nswe", padx=20, pady=20)
        
                            
        frame_estandar = tk.Frame(mainFrame)
        frame_estandar.grid(row = 1, column=0, sticky="nsw")
        
        label_estandar = tk.Label(frame_estandar, width=60, text="Generar objetos con razón entre galaxias y cuásares preestablecida.")
        label_estandar.grid(columnspan=2, padx=10, pady=10)
        
        mas_info = tk.Button(frame_estandar, text="Más información", command=mas_info_ventana)
        mas_info.grid(columnspan=2, padx=10, pady=10)
        
        menu_estandar_objs(frame_estandar, root)
        
        
        frame_custom = tk.Frame(mainFrame)
        frame_custom.grid(row = 1, column=1, sticky="nse")
        
        label_custom = tk.Label(frame_custom, width=60, text="Generar objetos en cantidades personalizadas.")
        label_custom.grid(columnspan=2, padx=10, pady=10)
        
        menu_custom_objs(frame_custom, root)
        
        
        root.mainloop()

ventana_principal()

print(ret_args)

