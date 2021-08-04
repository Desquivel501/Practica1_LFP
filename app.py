import datetime

date = datetime.datetime.now()
from tkinter.filedialog import askopenfilename


def leer(ruta):
    archivo = open(ruta, "r")
    contenido = archivo.read()
    archivo.close()
    return contenido

def analizar(texto):
    nombre_curso = ""
    for c in texto:
        if c == "=":
            break
        else:
            nombre_curso += c
    
    estudiantes = ""
    inicio_estudiantes = False
    
    for c1 in texto:
        if c1 == "{":
            inicio_estudiantes = True
        elif c1 != "}" and c1 != "{" and inicio_estudiantes == True:
            estudiantes += c1
        elif c1 == "}":
            break
        
    lista_estudiantes_base = estudiantes.split(",")
    lista_estudiantes = []
    diccionario_estudiantes = {}
    
    for i in lista_estudiantes_base:
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
 
    #print(lista_estudiantes)
    
    for estudiante in lista_estudiantes:
        valor = estudiante.split(";")
        diccionario_estudiantes[valor[0]] = int(valor[1])
    
    print(diccionario_estudiantes)
            
    

filename = askopenfilename()
print(filename)
text = leer(filename)
#print(analizar(text))
analizar(text)