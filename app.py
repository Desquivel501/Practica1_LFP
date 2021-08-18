from reporte import Reportes
from lector_archivo import Lector_archivo
from tkinter.filedialog import askopenfilename

archivo_cargado = False
datos = []
       
while(True):
    print("")
    print("--CONTROL ACADEMICO FACULTAD DE INGENIERIA--")
    print("|| Seleccione accion a realizar:          ||")
    print("|| 1. Cargar Archivo                      ||")
    print("|| 2. Mostrar Reporte en Consola          ||")
    print("|| 3. Exportar Reporte                    ||")
    print("|| 4. Salir                               ||")
    print("--------------------------------------------")
    res = input()

    if res == "1":
        try:
            filename = askopenfilename(filetypes = (('lfp files','*.lfp'),))
            text = Lector_archivo().leer(filename)
            datos = Lector_archivo().analizar(text)
            archivo_cargado = True
            print("Se ha leido el archivo correctamente")
        except Exception as e:
            print("ERROR: No se ha podido leer el archivo")
            print(e)           

    elif res == "2" and archivo_cargado:
        try:
            Reportes().consola(datos[1], datos[0], datos[2])
        except Exception as e:
            print("ERROR: Ha ocurrido un error al generar el reporte")
            print(e)
               
    elif res == "3" and archivo_cargado:
        try:
            Reportes().generar(datos[1], datos[0], datos[2])
            print("Se ha generado el reporte")
        except Exception as e:
            print("ERROR: Ha ocurrido un error al generar el reporte") 
            print(e)
            
    elif res == "2" and archivo_cargado == False:
        print("ERROR: No se ha cargado ningun archivo")
        
    elif res == "3" and archivo_cargado == False:
        print("ERROR: No se ha cargado ningun archivo")   
                
    elif res == "4":
        quit()
        
    else:
        print("ERROR: Opcion no valida")
    
