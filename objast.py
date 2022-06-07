import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.neighbors import KernelDensity
import puntos as pn
from pandas import DataFrame

# A partir de los datos de los coeficientes de la expansión 
# de datos reales en la base de PCAs, obtiene distribuciones
# (KDEs, Kernel Density Estimation) que muestreamos para 
# generar nuevos espectros.
def loadKdes(dist):
    kdes = []
    for i in range(n_components):
        margen = (dist[i].max()-dist[i].min())/4
        kde = KernelDensity(bandwidth=margen/8, kernel='gaussian')
        kde.fit(dist[i][:, None])
        kdes.append(kde)
    return kdes

# Genera espectros (vectores de coeficientes en la base de PCAs)
# muestreando las distribuciones (KDEs) generadas por la función
# anterior.
def generarEspectroKdes(kdes, n_samples = 1):
    samples = []
    for j in range(n_samples):
        sample = []
        for i in range(len(kdes)):
            sample.append(float(kdes[i].sample()))
        samples.append(sample)
    samples = np.array(samples)
    if(n_samples == 1):
        return samples[0]
    else:
        return samples

# Carga la distribución de los objetos en z (corrimiento al rojo), 
# se usa también KDE
def loadKde_z():
    margen = (dist_z.max()-dist_z.min())/4
    kde = KernelDensity(bandwidth=margen/8, kernel='gaussian')
    kde.fit(dist_z[:, None])
    return kde

# Genera z's muestreando el KDE obtenido de la función anterior
def generarZ(n_samples = 1):
    samples = []
    for j in range(n_samples):
        samples.append(float(kde_z.sample()))
    samples = np.array(samples)
    if(n_samples == 1):
        return samples[0]
    else:
        return samples
    

# VARIABLES GLOBALES Y CARGA DE ARCHIVOS
# Estos datos son necesarios para la generación de espectros
# y corrimientos al rojo (z)
dist_qso_mas = np.loadtxt("archivos/Distribution_QSO+2.1.txt")
spec_mean_qso_mas = np.loadtxt("archivos/spec_mean_QSO+2.1.txt")
evecs_qso_mas = np.loadtxt("archivos/evecs_QSO+2.1.txt")

dist_qso_menos = np.loadtxt("archivos/Distribution_QSO-2.1.txt")
spec_mean_qso_menos = np.loadtxt("archivos/spec_mean_QSO-2.1.txt")
evecs_qso_menos = np.loadtxt("archivos/evecs_QSO-2.1.txt")

dist_gal = np.loadtxt("archivos/Distribution_GAL.txt")
spec_mean_gal = np.loadtxt("archivos/spec_mean_GAL.txt")
evecs_gal = np.loadtxt("archivos/evecs_GAL.txt")

dist_z = np.loadtxt("archivos/Distribution_z.txt")

logwave = np.loadtxt("archivos/logwave.txt")

n_components = 50

# Los datos cargados se almacenan en un Dataframe al que podemos 
# acceder fácilmente con los índices y nombre de columnas.
generadores = pd.DataFrame([[loadKdes(dist_qso_menos),evecs_qso_menos,spec_mean_qso_menos],
                        [loadKdes(dist_qso_mas),evecs_qso_mas,spec_mean_qso_mas],
                        [loadKdes(dist_gal),evecs_gal,spec_mean_gal]],
                       index=["QSO-","QSO+","GAL"], columns=["kdes","evecs","spec_mean"]).T

# Cargamos también la distribución de z
kde_z = loadKde_z()

# Declaración de clases

# Clase madre objast (objeto astronómico)
# Solo tiene como atributo la posición en coordenadas (RA, DEC)
class objast():
    def __init__(self, RA_DEC = np.nan, *args, **kwargs):
        if(np.isnan(RA_DEC)):
            self.RA_DEC = self.rand_sphere()
        super(objast,self).__init__()
    
    def rand_sphere(self, npt=1):
        phi=np.random.uniform(-np.pi,np.pi,npt)
        theta=np.arccos(np.random.uniform(-1,1,npt))-np.pi/2
        pos = np.vstack((phi,theta)).T
        if(npt == 1):
            pos = pos[0]
            self.RA_DEC = pos
        return pos

# Clase oamas (objeto astronómico con z>2.1)
# Agrega como atributo el corrimiento al rojo, tiene un
# método para generarlo con el kde de z que cargamos antes
class oamas(objast):
    def __init__(self, z = np.nan, *args, **kwargs):
        if(np.isnan(z)):
            z = self.generarZ()
        else:
            self.z=z
        super(oamas,self).__init__(*args, **kwargs)
    
    def generarZ(self):
        z = 2.0
        while (z < 2.1):
            z = generarZ()
        self.z = z
        return z

# Clase oamenos (objeto astronómico con z<2.1)
class oamenos(objast):
    def __init__(self, z = np.nan, *args, **kwargs):
        if(np.isnan(z)):
            z = self.generarZ()
        else:
            self.z=z
        super(oamenos,self).__init__(*args, **kwargs)
    
    def generarZ(self):
        z = 2.2
        while (z > 2.1):
            z = generarZ()
        self.z = z
        return z


# Clase qsomas (cuásar con z>2.1)
# Agrega como atributo el espectro, tiene un método para 
# generarlo con los kde que cargamos antes
class qsomas(oamas):
    def __init__(self, *args, **kwargs):
        self.espectro = self.generarEspectro()
        self.tipo_objeto = "QSO+"
        self.tipo_espectro = "QSO+"
        super(qsomas,self).__init__(*args, **kwargs)
    
    def generarEspectro(self,n_espectros=1):
        espectro_generado = generarEspectroKdes(generadores["QSO+"]["kdes"], n_espectros)
        self.espectro = espectro_generado
        return espectro_generado

# Clase qsomenos (cuásar con z<2.1)
class qsomenos(oamenos):
    def __init__(self, *args, **kwargs):
        self.espectro = self.generarEspectro()
        self.tipo_objeto = "QSO-"
        self.tipo_espectro = "QSO-"
        super(qsomenos,self).__init__(*args, **kwargs)
    
    def generarEspectro(self,n_espectros=1):
        espectro_generado = generarEspectroKdes(generadores["QSO-"]["kdes"], n_espectros)
        self.espectro = espectro_generado
        return espectro_generado

# Clase galmas (Galaxia con z>2.1)
class galmas(oamas):
    def __init__(self, *args, **kwargs):
        self.espectro = self.generarEspectro()
        self.tipo_objeto = "GAL+"
        self.tipo_espectro = "GAL"
        super(galmas,self).__init__(*args, **kwargs)
    
    def generarEspectro(self,n_espectros=1):
        espectro_generado = generarEspectroKdes(generadores["GAL"]["kdes"], n_espectros)
        self.espectro = espectro_generado
        return espectro_generado

# Clase galmenos (Galaxia con z<2.1)
class galmenos(oamenos):
    def __init__(self, *args, **kwargs):
        self.espectro = self.generarEspectro()
        self.tipo_objeto = "GAL-"
        self.tipo_espectro = "GAL"
        super(galmenos,self).__init__(*args, **kwargs)
    
    def generarEspectro(self,n_espectros=1):
        espectro_generado = generarEspectroKdes(generadores["GAL"]["kdes"], n_espectros)
        self.espectro = espectro_generado
        return espectro_generado


# Genera lista de objetos astronómicos con opción a fijar la 
# cantidad de cada tipo de objeto que se requiera.
def generarObjetos(n_objetos=0, custom=False, n_qsomas=0, n_qsomenos=0, n_galmas=0, n_galmenos=0):
    
    lista_objetos = []

    if(not custom):
        ratio_avg = 0.37625819972845664
        ratio_std = 0.042980063642444125
        ratio = np.random.normal(ratio_avg, ratio_std,1)
        n_qso = int(ratio * n_objetos)
        n_gal = n_objetos - n_qso
        
        # Ciclo de generación de QSO
        for i in range(n_qso):
            z = generarZ()
            if(z>2.1):
                lista_objetos.append(qsomas(z=z))
            else:
                lista_objetos.append(qsomenos(z=z))
        
        # Ciclo de generación de GAL
        for i in range(n_gal):
            z = generarZ()
            if(z>2.1):
                lista_objetos.append(galmas(z=z))
            else:
                lista_objetos.append(galmenos(z=z))
    
    else:
        for i in range(n_qsomas): lista_objetos.append(qsomas())
        for i in range(n_qsomenos): lista_objetos.append(qsomenos())
        for i in range(n_galmas): lista_objetos.append(galmas())
        for i in range(n_galmenos): lista_objetos.append(galmenos())
    
    return lista_objetos


# Obtiene la posición de la lista de objetos en un arreglo de numpy
# Creada con el objetivo de graficar con más facilidad la posición
def getpos(lista_objetos):
    return np.array([objeto.RA_DEC for objeto in lista_objetos])


# Construye el espectro de un objeto, recibe un objeto completo como argumento, 
# el cual tiene la información completa para reconstruir el espectro
def construir_espectro(objeto):
    plt.style.use('default')
    coeff = objeto.espectro
    generador = generadores[objeto.tipo_espectro]
    z = objeto.z
    evecs = generador["evecs"]
    spec_mean = generador["spec_mean"]
    wavelengths = 10**logwave/(1+z)
    
    fig = plt.figure(figsize=(6, 2))
    fig.subplots_adjust(hspace=0, top=0.95, bottom=0.1, left=0.12, right=0.93)
    
    espectro = spec_mean + np.dot(coeff[:n_components], evecs[:n_components])
    
    plt.plot(wavelengths, espectro , '-k')
    plt.text(x = wavelengths[0], y = espectro.max() - (espectro.max()-espectro.min())*0.1 , s = "z = " + str(round(z,3)))
    # plt.ylim(-10, 40)
    plt.ylabel('flujo')
    plt.xlabel(r'Longitud de onda${\rm (\AA)}$')
    plt.show()

# Reconstruye un espectro
def plotrecons(objeto):
    coeff = objeto.espectro
    generador = generadores[objeto.tipo_espectro]
    z = objeto.z
    evecs = generador["evecs"]
    spec_mean = generador["spec_mean"]
    wavelengths = 10**logwave/(1+z)
    
    spec = spec_mean + np.dot(coeff[:n_components], evecs[:n_components])
    
    iters = (np.array([0, 0.1, 0.25, 0.5, 1])*n_components).astype(int)
    
    fig = plt.figure(figsize=(6, 14))
    fig.subplots_adjust(hspace=0, top=0.95, bottom=0.1, left=0.12, right=0.93)
    
    for i, n in enumerate(iters):
        ax = fig.add_subplot(911 + i)
        ax.plot(wavelengths, spec, '-', c='gray')
        ax.plot(wavelengths, spec_mean + np.dot(coeff[:n], evecs[:n]), '-k')

        if i < 3:
            ax.xaxis.set_major_formatter(plt.NullFormatter())

        ax.set_ylim(-10, 25)
        ax.set_ylabel('flux')

        if n == 0:
            text = "mean"
        elif n == 1:
            text = "mean + 1 component\n"
        else:
            text = "mean + %i components\n" % n

        ax.text(0.02, 0.93, text, ha='left', va='top', transform=ax.transAxes)

    fig.axes[-1].set_xlabel(r'${\rm wavelength\ (\AA)}$')
    plt.show()



    
def construirUnespectro(objeto):
    plt.style.use('default')
    coeff = objeto.espectro
    generador = generadores[objeto.tipo_espectro]
    z = objeto.z
    evecs = generador["evecs"]
    spec_mean = generador["spec_mean"]
    wavelengths = 10**logwave/(1+z)
    
    fig = plt.figure(figsize=(6, 2))
    fig.subplots_adjust(hspace=0, top=0.95, bottom=0.1, left=0.12, right=0.93)
    
    espectro = spec_mean + np.dot(coeff[:n_components], evecs[:n_components])
    return pd.DataFrame([wavelengths,espectro],columns=['wavelengths','espectro'])
        
def oneGraf_3D(pos,n):
    plt.style.use('dark_background')
    fig = plt.figure(dpi=150)
    ax = fig.add_subplot(111, projection='3d')

    x,y,z = pn.ang_to_xyz(pos.T[0],pos.T[1])


    ax.scatter(x[n], y[n], z[n], marker="o",color='red')
    x = np.delete(x, n)
    y = np.delete(y, n)
    z = np.delete(z, n)
    ax.scatter(x, y, z, marker=".")
    u, v = np.mgrid[0:2*np.pi:30j, 0:np.pi:15j]
    x = 0.99*np.cos(u)*np.sin(v)
    y = 0.99*np.sin(u)*np.sin(v)
    z = 0.99*np.cos(v)
    ax.plot_wireframe(x, y, z, color="w", alpha=0.2)

    ax.axis(False)
    ax.set_box_aspect([1,1,1])

    plt.show()
    plt.style.use('default')

def datos_espectro(objeto):
    plt.style.use('default')
    coeff = objeto.espectro
    generador = generadores[objeto.tipo_espectro]
    z = objeto.z
    evecs = generador["evecs"]
    spec_mean = generador["spec_mean"]
    wavelengths = 10**logwave/(1+z)

    fig = plt.figure(figsize=(6, 2))
    fig.subplots_adjust(hspace=0, top=0.95, bottom=0.1, left=0.12, right=0.93)

    espectro = spec_mean + np.dot(coeff[:n_components], evecs[:n_components])

    data1 = {'wavelengths': wavelengths,
                'espectro': espectro}
    df = DataFrame(data1,columns=['wavelengths','espectro'])
    return df