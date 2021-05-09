from ViajeroFrecuente import ViajeroFrecuente
import csv

class Manejador:
#Lista viajeros

    def __init__(self):
        self.__lista = []
    
    def agregarViajero(self, unViajero):
        #agregar a la lista
        self.__lista.append(unViajero)
    
    def mostrarViajeros(self):
        for viajero in self.__lista:
            print(viajero)
    
    def testViajero(self):
        archivo = open('viajeros.csv')
        reader = csv.reader(archivo,delimiter=',')
        for fila in reader:
            numeroViajero = int(fila[0])
            dni = int(fila[1])
            nombre = fila[2]
            apellido = fila[3]
            millasAcumuladas = int(fila[4])
            unViajero = ViajeroFrecuente(numeroViajero,dni,nombre,apellido,millasAcumuladas)
            self.agregarViajero(unViajero)
    
    def buscarViajero (self,identificador):
        print(" ")
        print(f"IDENTIFICADOR: {identificador}")
        for i, unViajero in enumerate(self.__lista):
            if unViajero.getNumeroViajero()==identificador:
                return i
        return -1

    def getViajero(self, indice):

        return self.__lista[indice]

    def __str__(self):
        s=""
        for viajero in self.__lista:
            s+=str(viajero)+ '\n'
        return s

