import generarPuntos as gen 


puntos = gen.rand_sphere(100)
pos_moll=gen.ang_to_mollweide(puntos.T[0],puntos.T[1])
print(pos_moll)
def getCordinates():
    return 9