from parametros import Parametros

class Reportes:
    
    def __init__(self):
        pass
    
    def generar(self, lista_estudiantes, nombre_curso, lista_parametros):
        html =  """<h1 style="text-align: center;">""" + nombre_curso.upper().replace("_"," ") +"""</h1>
                    <table style="height: 108px; width: 60%; border-collapse: collapse; margin-left: auto; margin-right: auto;" border="1">
                    <tbody>
                    <tr style="height: 18px;">
                    <td style="width: 33.3333%; height: 18px;"><strong>No.</strong></td>
                    <td style="width: 33.3333%; height: 18px;"><strong>Nombre Estudiante</strong></td>
                    <td style="width: 33.3333%; height: 18px;"><strong>Nota</strong></td>
                    </tr>
                    """
        cont = 1
        for i in lista_estudiantes:
            color = "#ffffff"
            if int(lista_estudiantes[cont-1][1]) >= 61:
                color = "#58b8fc"
            else:
                color = "#ff7070"
                
            html += """<tr style="height: 18px;">
                    <td style="width: 33.3333%; height: 18px;">""" + str(cont) +""".</td>
                    <td style="width: 33.3333%; height: 18px;">""" + str(lista_estudiantes[cont-1][0]) +"""</td>
                    <td style="width: 33.3333%; height: 18px; background-color:""" + color +""";">""" + str(lista_estudiantes[cont-1][1]) +"""</td>
                    </tr>"""
            cont += 1 
        html += """ </tbody>
                    </table>
                    <p>&nbsp;</p>"""
        
        for i in lista_parametros:
            if i == "ASC":         
                lista_ascendente = Parametros().ascendente(lista_estudiantes)
                html += """<h3 style="text-align: center;">ASCENDENTE</h3>
                    <table style="height: 108px; width: 60%; border-collapse: collapse; margin-left: auto; margin-right: auto;" border="1">
                    <tbody>
                    <tr style="height: 18px;">
                    <td style="width: 33.3333%; height: 18px;"><strong>No.</strong></td>
                    <td style="width: 33.3333%; height: 18px;"><strong>Nombre Estudiante</strong></td>
                    <td style="width: 33.3333%; height: 18px;"><strong>Nota</strong></td>
                    </tr>"""
                cont = 1
                for j in lista_ascendente:
                    html += """<tr style="height: 18px;">
                                <td style="width: 33.3333%; height: 18px;">""" + str(cont) +""".</td>
                                <td style="width: 33.3333%; height: 18px;">""" + str(lista_ascendente[cont-1][0]) +"""</td>
                                <td style="width: 33.3333%; height: 18px;">""" + str(lista_ascendente[cont-1][1]) +"""</td>
                                </tr>"""
                    cont += 1
                html +="""</tbody>
                    </table>
                    <p>&nbsp;</p>"""
            
            elif i == "DESC":         
                lista_descendente = Parametros().descendente(lista_estudiantes)
                html += """<h3 style="text-align: center;">DESCENDENTE</h3>
                    <table style="height: 108px; width: 60%; border-collapse: collapse; margin-left: auto; margin-right: auto;" border="1">
                    <tbody>
                    <tr style="height: 18px;">
                    <td style="width: 33.3333%; height: 18px;"><strong>No.</strong></td>
                    <td style="width: 33.3333%; height: 18px;"><strong>Nombre Estudiante</strong></td>
                    <td style="width: 33.3333%; height: 18px;"><strong>Nota</strong></td>
                    </tr>"""
                cont = 1
                for j in lista_ascendente:
                    html += """<tr style="height: 18px;">
                                <td style="width: 33.3333%; height: 18px;">""" + str(cont) +""".</td>
                                <td style="width: 33.3333%; height: 18px;">""" + str(lista_descendente[cont-1][0]) +"""</td>
                                <td style="width: 33.3333%; height: 18px;">""" + str(lista_descendente[cont-1][1]) +"""</td>
                                </tr>"""
                    cont += 1
                html +="""</tbody>
                    </table>
                    <p>&nbsp;</p>"""
            
            elif i == "AVG":
                html += """<h3 style="text-align: center;">PROMEDIO DE CLASE</h3>
                            <p style="text-align: center;">La nota promedio es: """ + str(Parametros().promedio(lista_estudiantes)) +"""</p>
                            <p>&nbsp;</p>"""
            
            elif i == "MIN":
                html += """<h3 style="text-align: center;">MINIMO</h3>
                            <p style="text-align: center;">La nota minima de la clase es: """ + Parametros().minimo(lista_estudiantes) +"""</p>
                            <p>&nbsp;</p>"""
                            
            elif i == "MAX":
                html += """<h3 style="text-align: center;">MAXIMO</h3>
                            <p style="text-align: center;">La nota maxima de la clase es: """ + Parametros().maximo(lista_estudiantes) +"""</p>
                            <p>&nbsp;</p>"""
            
            elif i == "APR":
                html += """<h3 style="text-align: center;">ALUMNOS APROBADOS</h3>
                            <p style="text-align: center;">El numero de alumnos aprobados es: """ + str(Parametros().aprobado(lista_estudiantes)) +"""</p>
                            <p>&nbsp;</p>"""
            
            elif i == "REP":
                html += """<h3 style="text-align: center;">ALUMNOS REPROBADOS</h3>
                            <p style="text-align: center;">El numero de alumnos reprobados es: """ + str(Parametros().reprobado(lista_estudiantes)) +"""</p>
                            <p>&nbsp;</p>"""
            
            else:
                print("Parametro \"" + i + "\" no valido")

        archivo = open("Reporte.html","w+")
        archivo.write(html)
        archivo.close()
    
    def consola(self, lista_estudiantes, nombre_curso, lista_parametros):
        print(nombre_curso.upper().replace("_"," "))
        print("")
        print("NOMBRE       NOTA")
        
        cont = 0
        for i in lista_estudiantes:
            print(str(lista_estudiantes[cont][0]).strip() + "  " + str(lista_estudiantes[cont][1]))
            cont += 1
        
        for i in lista_parametros:
            if i == "ASC":
                lista_ascendente = Parametros().ascendente(lista_estudiantes)
                print("NOMBRE       NOTA")
                cont1 = 0
                for j in lista_ascendente:
                    print(str(lista_ascendente[cont1][0]).strip() + "  " + str(lista_ascendente[cont1][1]))
                    cont1 += 1
                print("")
            
            elif i == "DEC":
                lista_descendente = Parametros().descendente(lista_descendente)
                print("NOMBRE       NOTA")
                cont1 = 0
                for j in lista_descendente:
                    print(str(lista_descendente[cont1][0]).strip() + "  " + str(lista_descendente[cont1][1]))
                    cont1 += 1
                print("")
            
            elif i == "AVG":
                print("El promedio es: " + str(Parametros().promedio(lista_estudiantes)))
                print("")
                
            elif i == "MIN":
                print("La nota minima del curso es: " + str(Parametros().minimo(lista_estudiantes)))
                print("")
            
            elif i == "MAX":
                print("La nota maxima del curso es: " + str(Parametros().maximo(lista_estudiantes)))
                print("")
            
            elif i == "APR":
                print("La cantidad de alumnos aprobados es: " + str(Parametros().aprobado(lista_estudiantes)))
                print("")
            
            elif i == "REP":
                print("La cantidad de alumnos reprobados es: " + str(Parametros().reprobado(lista_estudiantes)))
                print("")
        
        