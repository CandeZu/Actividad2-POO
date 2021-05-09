import csv

class ViajeroFrecuente:
    __numViajero = None
    __dni = None
    __nombre = None
    __apellido = None
    __millasAcumuladas = None

    def __init__ (self, numViajero, dni, nombre, apellido, millasAcumuladas):

        self.__numViajero = numViajero
        self.__dni = dni
        self.__nombre = nombre
        self.__apellido = apellido
        self.__millasAcumuladas = millasAcumuladas
    
    def __str__(self):
        # return "{} {} {} {} {}".format(self.__numViajero,self.__dni,self.__nombre,self.__apellido,self.__millasAcumuladas)
        # return "%d %d %s %s %d" %(self.__numViajero,self.__dni,self.__nombre,self.__apellido,self.__millasAcumuladas)
        return 'Numero de viajero: {} \nDNI: {} \nNombre: {} \nApellido: {} \nMillas acumuladas: {}'.format(self.__numViajero,self.__dni,self.__nombre,self.__apellido,self.__millasAcumuladas)

    def getNumeroViajero (self):
        return self.__numViajero

    def getDni (self):
        return self.__dni

    def getNombre (self):
        return self.__nombre

    def getApellido (self):
        return self.__apellido

    def cantidadTotaldeMillas (self):
        return self.__millasAcumuladas
    
    def acumularMillas (self, millas):
        self.__millasAcumuladas += millas
    
    def canjearMillas (self, millas):
        if (millas <= self.__millasAcumuladas):
            self.__millasAcumuladas -= millas
        else:
            print('Error en la operación.')

