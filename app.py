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
        elif c1 != "}" and c1 != "{" and inicio_estudiantes == True:
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
 
    #print(lista_estudiantes)
    
    diccionario_estudiantes = {}
    for estudiante in lista_estudiantes:
        valor = estudiante.split(";")
        diccionario_estudiantes[valor[0]] = int(valor[1])
        
    print(nombre_curso)
    print(diccionario_estudiantes)  
    print(lista_parametros)
            
    

filename = askopenfilename()
print(filename)
text = leer(filename)
#print(analizar(text))
analizar(text)