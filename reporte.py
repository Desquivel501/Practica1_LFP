from parametros import Parametros
from colorama import Fore, Back, Style
import os

class Reportes:
    
    def __init__(self):
        pass
    
    def generar(self, lista_estudiantes, nombre_curso, lista_parametros):
        html =  """<!doctype html>
                    <html lang="en">
                    <head>
                    <!-- Required meta tags -->
                    <meta charset="utf-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">

                    <!-- Bootstrap CSS -->
                    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">

                    <title>Control de Estudiantes</title>
                    </head>
                    <body>
                    <h1 style="text-align: center;">""" + nombre_curso.upper().replace("_"," ") +"""</h1>
                    <p>&nbsp;</p>
                                        
                    <h3 style="text-align: center;">LISTA DE ESTUDIANTES</h3>
                    <table style="height: 108px; width: 60%; border-collapse: collapse; margin-left: auto; margin-right: auto;" class="table">
                    <thead>
                    <tr style="height: 18px;">
                    <th><strong>No.</strong></th>
                    <th><strong>Nombre Estudiante</strong></th>
                    <th><strong>Nota</strong></th>
                    </tr>
                    </thead>
                    <tbody>
                    """
        cont = 1
        for i in lista_estudiantes:
            color = "#ffffff"
            if int(lista_estudiantes[cont-1][1]) >= 61:
                color = "#0000ff"
            else:
                color = "#ff0000"
                
            html += """<tr style="height: 18px;">
                    <td><span style="color: """ + color + """;">""" + str(cont) +""".</span></td>
                    <td><span style="color: """ + color + """;">""" + str(lista_estudiantes[cont-1][0]) +"""</span></td>
                    <td><span style="color: """ + color + """;">""" + str(lista_estudiantes[cont-1][1]) +"""</span></td>
                    </tr>"""
            cont += 1 
        html += """ </tbody>
                    </table>
                    <p>&nbsp;</p>"""
        
        for i in lista_parametros:
            if str(i).upper() == "ASC":         
                lista_ascendente = Parametros().ascendente(lista_estudiantes)
                html += """<h3 style="text-align: center;">ASCENDENTE</h3>
                    <table style="height: 108px; width: 60%; border-collapse: collapse; margin-left: auto; margin-right: auto;" class="table">
                    <thead>
                    <tr style="height: 18px;">
                    <th><strong>No.</strong></th>
                    <th><strong>Nombre Estudiante</strong></th>
                    <th><strong>Nota</strong></th>
                    </tr>
                    </thead>
                    <tbody>"""
                cont = 1
                for j in lista_ascendente:
                    html += """<tr style="height: 18px;">
                                <td>""" + str(cont) +""".</td>
                                <td>""" + str(lista_ascendente[cont-1][0]) +"""</td>
                                <td>""" + str(lista_ascendente[cont-1][1]) +"""</td>
                                </tr>"""
                    cont += 1
                html +="""</tbody>
                    </table>
                    <p>&nbsp;</p>"""
            
            elif str(i).upper() == "DESC":         
                lista_descendente = Parametros().descendente(lista_estudiantes)
                html += """<h3 style="text-align: center;">DESCENDENTE</h3>
                    <table style="height: 108px; width: 60%; border-collapse: collapse; margin-left: auto; margin-right: auto;" class="table">
                    <thead>
                    <tr style="height: 18px;">
                    <th><strong>No.</strong></th>
                    <th><strong>Nombre Estudiante</strong></th>
                    <th><strong>Nota</strong></th>
                    </tr>
                    </thead>
                    <tbody>"""
                cont = 1
                for j in lista_ascendente:
                    html += """<tr style="height: 18px;">
                                <td>""" + str(cont) +""".</td>
                                <td>""" + str(lista_descendente[cont-1][0]) +"""</td>
                                <td>""" + str(lista_descendente[cont-1][1]) +"""</td>
                                </tr>"""
                    cont += 1
                html +="""</tbody>
                    </table>
                    <p>&nbsp;</p>"""
            
            elif str(i).upper() == "AVG":
                html += """<h3 style="text-align: center;">PROMEDIO DE CLASE</h3>
                            <p style="text-align: center;">La nota promedio es: """ + str(Parametros().promedio(lista_estudiantes)) +"""</p>
                            <p>&nbsp;</p>"""
            
            elif str(i).upper() == "MIN":
                html += """<h3 style="text-align: center;">MINIMO</h3>
                            <p style="text-align: center;">La nota minima de la clase es: """ + Parametros().minimo(lista_estudiantes) +"""</p>
                            <p>&nbsp;</p>"""
                            
            elif str(i).upper() == "MAX":
                html += """<h3 style="text-align: center;">MAXIMO</h3>
                            <p style="text-align: center;">La nota maxima de la clase es: """ + Parametros().maximo(lista_estudiantes) +"""</p>
                            <p>&nbsp;</p>"""
            
            elif str(i).upper() == "APR":
                html += """<h3 style="text-align: center;">ALUMNOS APROBADOS</h3>
                            <p style="text-align: center;">El numero de alumnos aprobados es: """ + str(Parametros().aprobado(lista_estudiantes)) +"""</p>
                            <p>&nbsp;</p>"""
            
            elif str(i).upper() == "REP":
                html += """<h3 style="text-align: center;">ALUMNOS REPROBADOS</h3>
                            <p style="text-align: center;">El numero de alumnos reprobados es: """ + str(Parametros().reprobado(lista_estudiantes)) +"""</p>
                            <p>&nbsp;</p>"""
            
            else:
                print("Parametro \"" + i + "\" no valido")

        html += """
                <script src="https://code.jquery.com/jquery-3.2.1.slim.min.js" integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN" crossorigin="anonymous"></script>
                <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.12.9/umd/popper.min.js" integrity="sha384-ApNbgh9B+Y1QKtv3Rn7W3mgPxhU9K/ScQsAP7hUibX39j7fakFPskvXusvfa0b4Q" crossorigin="anonymous"></script>
                <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js" integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl" crossorigin="anonymous"></script>
                </body>
                </html>
                """
 
        cwd = os.getcwd()
        archivo = open("Reporte.html","w+")
        archivo.write(html)
        print("Se ha generado el reporte en: " + cwd + "\Reporte.html")
        archivo.close()
    
    def consola(self, lista_estudiantes, nombre_curso, lista_parametros):
        
        print("")
        print(nombre_curso.upper().replace("_"," "))
        print("")
        
        print("LISTA ESTUDIANTES")
        print("")
        print("NOMBRE", '        ',"NOTA")
        cont = 0
        for i in lista_estudiantes:
            color = Fore.WHITE
            if int(lista_estudiantes[cont][1]) >= 61:
                color = Fore.BLUE
            else:
                color = Fore.RED
            
            print( color + str(lista_estudiantes[cont][0]).strip(), '        ',str(lista_estudiantes[cont][1]) + Style.RESET_ALL)
            cont += 1
        print("")
                
        for i in lista_parametros:
            if str(i).upper() == "ASC":
                print("ASCENDENTE")
                print("")
                lista_ascendente = Parametros().ascendente(lista_estudiantes)
                print("NOMBRE", '        ',"NOTA")
                cont1 = 0
                for j in lista_ascendente:
                    print(str(lista_ascendente[cont1][0]).strip(), '        ',str(lista_ascendente[cont1][1]))
                    cont1 += 1
                print("")
            
            elif str(i).upper() == "DESC":
                print("DESCENDENTE")
                print("")
                lista_descendente = Parametros().descendente(lista_descendente)
                print("NOMBRE", '        ',"NOTA")
                cont1 = 0
                for j in lista_descendente:
                    print(str(lista_descendente[cont1][0]).strip(), '        ',str(lista_descendente[cont1][1]))
                    cont1 += 1
                print("")
            
            elif str(i).upper() == "AVG":
                print("El promedio es: " + str(Parametros().promedio(lista_estudiantes)))
                print("")
                
            elif str(i).upper() == "MIN":
                print("La nota minima del curso es: " + str(Parametros().minimo(lista_estudiantes)))
                print("")
            
            elif str(i).upper() == "MAX":
                print("La nota maxima del curso es: " + str(Parametros().maximo(lista_estudiantes)))
                print("")
            
            elif str(i).upper() == "APR":
                print("La cantidad de alumnos aprobados es: " + str(Parametros().aprobado(lista_estudiantes)))
                print("")
            
            elif str(i).upper() == "REP":
                print("La cantidad de alumnos reprobados es: " + str(Parametros().reprobado(lista_estudiantes)))
                print("")
            
            else:
                print("Parametro \"" + i + "\" no valido")
        
        