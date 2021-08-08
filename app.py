from parametros import Parametros
from reporte import Reportes
from tkinter.filedialog import askopenfilename
import tkinter as tk

root = tk.Tk() 
root.iconify()



def leer(ruta):
    archivo = open(ruta, "r")
    contenido = archivo.read()
    archivo.close()
    return contenido

def analizar(texto):
    estudiantes = ""
    parametros = ""
    curso = ""
    
    inicio_estudiantes = False
    inicio_parametros = False
    fin_curso = False
    
    for c1 in texto:
        if c1 != "=" and fin_curso != True:
            curso += c1
        elif c1 == "=":
            fin_curso = True
        elif c1 == "{":
            inicio_estudiantes = True
        elif c1 != "}" and inicio_estudiantes == True:
            estudiantes += c1
        elif c1 == "}":
            inicio_parametros = True
            inicio_estudiantes = False
        elif c1 != " " and inicio_parametros == True:
            parametros += c1
    lista_parametros = parametros.split(",")
    nombre_curso = curso
        
    lista_estudiantes = []
    for i in estudiantes.split(","):
        inicio_nombre = False
        nuevo_valor = ""
        for c in i:
            if c == "<":
                inicio_nombre = True
            elif c != "<" and c != ">" and c != "\"" and inicio_nombre == True:
                nuevo_valor += c
            elif c == ">":
                break  
        lista_estudiantes.append(nuevo_valor)
    
    for estudiante in lista_estudiantes:
        valor = estudiante.split(";")
        t = (valor[0],int(valor[1]))
        lista_final.append(t)
    
    datos = [nombre_curso,lista_final,lista_parametros]
    
    return datos


archivo_cargado = False
text = ""
lista_final = []
lista_parametros = []
nombre_curso = ""

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
            filename = askopenfilename()
            text = leer(filename)
            datos = analizar(text)
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
    
