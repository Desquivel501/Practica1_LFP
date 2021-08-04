class Lector_archivo: 

    def leer(ruta):
        archivo = open(ruta, "r")
        contenido = archivo.read()
        archivo.close()
        return contenido
        