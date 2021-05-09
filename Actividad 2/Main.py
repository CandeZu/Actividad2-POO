from ViajeroFrecuente import ViajeroFrecuente
from Manejador import Manejador
from Menu import Menu

def mostrar():
    print('')
    print('------MENU---------')
    print('1. Consultar viajero')
    print('2. Salir')
    print('')

def imprimir():
    print('')
    print('---------MENU----------')
    print('1. Consultar cantidad de millas')
    print('2. Acumular millas')
    print('3. Canejar millas')
    print('0. Presione 0 para salir')
    print('')

def menu():
    band = True
    while band:
        imprimir()
        opcion = int(input("Ingrese la opcion: "))
        if opcion == 1:
            manejadorViajero = Manejador()
            manejadorViajero.testViajero()
            num = int(input("Ingrese número de viajero para ver sus datos: "))
            indice = manejadorViajero.buscarViajero(num)
            if indice != -1:
                print('Se encontró en el lugar: ', indice)
                viajero = manejadorViajero.getViajero(indice)
                print(viajero)
                bandera=True
                while bandera:
                    mostrar()
                    memenu=Menu()
                    opcionesViajero=int(input("Ingrese una opción: "))
                    memenu.opcion(viajero,opcionesViajero)
                    if opcionesViajero == 4:
                        print("\nChau :)")
                        print(" ")
                        bandera=False
            else:
                print('El número de viajero no existe')
        elif opcion==2:
            band=False
            print("\nPrograma finalizado.")
            print(" ")
            
        else:
            print("\n Opción no valida")

if __name__ == '__main__':
    menu()