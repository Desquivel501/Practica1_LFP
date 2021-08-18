class Lector_archivo: 
    
    def leer(self, ruta):
        archivo = open(ruta, "r")
        contenido = archivo.read()
        archivo.close()
        return contenido

    def analizar(self, texto):
        estudiantes = ""
        parametros = ""
        curso = ""
        lista_final = []
        
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
        
        datos = [curso,lista_final,lista_parametros]
        
        return datos
    
        