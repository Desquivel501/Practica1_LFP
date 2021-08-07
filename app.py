from parametros import Parametros
from tkinter.filedialog import askopenfilename
import tkinter as tk

root = tk.Tk() 
root.iconify()

def leer(ruta):
    archivo = open(ruta, "r")
    contenido = archivo.read()
    archivo.close()
    return contenido

def analizar(texto, type):
    
    nombre_curso = ""
    estudiantes = ""
    parametros = ""
    
    inicio_estudiantes = False
    inicio_parametros = False
    fin_curso = False
    
    for c1 in texto:
        if c1 != "=" and fin_curso != True:
            nombre_curso += c1
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
    
    lista_final = []
    for estudiante in lista_estudiantes:
        valor = estudiante.split(";")
        t = (valor[0],int(valor[1]))
        lista_final.append(t)
    
    
    
        
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

    archivo_cargado = False
    text = ""

    if res == "1":
        filename = askopenfilename()
        text = leer(filename)
        print(text)
    elif res == "2":
        print("Console")
    elif res == "4":
        quit()
    else:
        print("not here")
    

# filename = askopenfilename()
# print(filename)
# text = leer(filename)
# print(text)
# #print(analizar(text))
# analizar(text)
