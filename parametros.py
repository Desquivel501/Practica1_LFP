
class Parametros:
     
    def ascendente(self, lista):
        self.lista = lista
        for x in range(len(self.lista)-1, -1, -1):
            swapped = False
            for i in range(x):
                if self.lista[i][1] > self.lista[i+1][1]:
                    self.lista[i], self.lista[i+1] = self.lista[i+1], self.lista[i]
                    swapped = True
            if not swapped:
                break
        return self.lista
    
    def descendente(self, lista):
        self.lista = lista
        for x in range(len(self.lista)-1, -1, -1):
            swapped = False
            for i in range(x):
                if self.lista[i][1] < self.lista[i+1][1]:
                    self.lista[i], self.lista[i+1] = self.lista[i+1], self.lista[i]
                    swapped = True
            if not swapped:
                break
        return self.lista
    
    def promedio(self, lista):
        acumulado = 0
        cont = 0
        for i in lista:
            acumulado += lista[cont][1]
            cont += 1
        prom = acumulado/len(lista)
        return prom
    
    def minimo(self,lista):
        lista = lista
        for x in range(len(lista)-1, -1, -1):
            swapped = False
            for i in range(x):
                if lista[i][1] > lista[i+1][1]:
                    lista[i], lista[i+1] = lista[i+1], lista[i]
                    swapped = True
            if not swapped:
                break
            
        t = lista[0]
        s = t[0] + ": " + str(t[1])
        return s
    
    def maximo(self,lista):
        lista = lista
        for x in range(len(lista)-1, -1, -1):
            swapped = False
            for i in range(x):
                if lista[i][1] < lista[i+1][1]:
                    lista[i], lista[i+1] = lista[i+1], lista[i]
                    swapped = True
            if not swapped:
                break
            
        t = lista[0]
        s = t[0] + ": " + str(t[1])
        return s
    
    def aprobado(self,lista):
        acumulado = 0
        cont = 0
        for i in lista:
            if lista[cont][1] >= 61:
                acumulado+=1
            cont += 1
        return acumulado  
    
    def reprobado(self,lista):
        acumulado = 0
        cont = 0
        for i in lista:
            if lista[cont][1] < 61:
                acumulado+=1
            cont += 1
        return acumulado  

