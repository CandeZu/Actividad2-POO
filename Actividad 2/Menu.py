class Menu:
    __switcher=None
    def __init__(self):
        self.__switcher= {
            1: self.opcion1,
            2: self.opcion2,
            3: self.opcion3,
            4: self.salir
        }

    def getSwitcher(self):
        return self.__switcher

    def opcion (self,viajero,op):
        func=self.__switcher.get(op,lambda: print("Opcion no valida"))
        func(viajero)


    def opcion1(self, viajero):
        print("La cantidad Total de millas es de: {}".format(viajero.cantidadTotaldeMillas()))

    def opcion2(self,viajero):
        m=int(input("Ingrese millas para acumular: "))
        viajero.acumularMillas(m)
        print("Las millas se acumularon correctamente")

    def opcion3(self, viajero):
        s=int(input("Ingrese millas a canjear: "))
        viajero.canjearMillas(s)

    def salir(self,viajero):
        print("Chau :)")