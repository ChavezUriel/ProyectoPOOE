import tkinter as tk
from pip import main

from pyparsing import col
from yaml import AnchorToken

def only_numbers(char):
    return char.isdigit()

def save_data(entries,root):
    n_obj_local = []
    for entry in entries:
        field = entry[0]
        text  = entry[1].get()
        n_obj_local.append(int(text))
        print('%s: "%s"' % (field, text))
    global n_obj_custom
    n_obj_custom = n_obj_local
    root.destroy()

def makeform(root, fields):
    entries = []
    for field in fields:
        row = tk.Frame(root)
        # row.rowconfigure(0, weight=1)
        # row.columnconfigure(0, weight=1)
        lab = tk.Label(row, text=field+": ", anchor='e')
        validation = root.register(only_numbers)
        ent = tk.Entry(row, validate="key", validatecommand=(validation, '%S'))
        row.pack(side=tk.TOP, fill=tk.Y, padx=5, pady=5)
        lab.grid(row=0,column=0, sticky="e")
        ent.grid(row=0,column=1, sticky="w")
        entries.append((field, ent))
    return entries



fields_custom = 'Cuásar z < 2.1', 'Cuásar z > 2.1', 'Galaxia z < 2.1', 'Galaxia z > 2.1'
n_obj_custom = []

class menu_custom_objs():
    def __init__(self, frame, root):
        ents = makeform(frame, fields_custom)
        frame.bind('<Return>', (lambda event, e=ents: save_data(e,frame)))   
        b1 = tk.Button(frame, text='Generar', command=(lambda e=ents: save_data(e,root)))
        b1.pack(side=tk.BOTTOM, padx=5, pady=5)

fields = ['Cantidad de objetos']
n_obj_estandar = []

class menu_estandar_objs():
    def __init__(self, frame, root):
        ents = makeform(frame, fields)
        frame.bind('<Return>', (lambda event, e=ents: save_data(e,frame)))   
        b1 = tk.Button(frame, text='Generar', command=(lambda e=ents: save_data(e,root)))
        b1.pack(side=tk.BOTTOM, padx=5, pady=5)


class ventana_principal():
    def __init__(self):
        root = tk.Tk()
        root.geometry('1000x350')
        #root.option_add( "*font", "Segoe 12" )
        
        mainFrame = tk.Frame(root)
        mainFrame.pack(padx=30, pady=30, fill="both", expand=True)

        mainFrame.rowconfigure(0, weight=1)
        mainFrame.columnconfigure(0, weight=1)
        
        titulo = tk.Label(mainFrame, text="Preferencias", font="bold")
        titulo.grid(row=0, column=0, columnspan=2, sticky="nswe")
                                     
        frame_estandar = tk.Frame(mainFrame)
        frame_estandar.grid(row = 1, column=0, sticky="nsw")
        
        frame_custom = tk.Frame(mainFrame)
        frame_custom.grid(row = 1, column=1, sticky="nse")
        
        label_estandar = tk.Label(frame_estandar, width=60, text="Generar objetos con razón entre galaxias y cuásares preestablecida.")
        label_estandar.pack(fill = "x", side = "top", expand=False, padx=10, pady=10)
        
        label_custom = tk.Label(frame_custom, width=60, text="Generar objetos en cantidades personalizadas.")
        label_custom.pack(fill = "x", side = "top", expand=False, padx=10, pady=10)
        
        menu_estandar_objs(frame_estandar, root)
        menu_custom_objs(frame_custom, root)
        
        root.mainloop()

ventana_principal()



