import math
from types import NoneType

class Circulo():
    radio= None

    # Sobreescribo el metodo __new__ para verificar que radio > 0. Caso contrario, se cancela la instanciacion
    def __new__(cls, *args):
        if args[0] > 0:
            obj = super().__new__(cls)
            return obj
        else:
            print("Error. El radio tiene que ser mayor a 0")

    # Constructor
    def __init__(self, radio: float):
        self.radio= radio

    # Pi x Radio^2
    def calcular_area(self):
        return "{:.2f}".format(math.pi * self.radio**2)

    # 2 x Pi x Radio
    def calcular_perimetro(self) -> float:
        return "{:.2f}".format(math.pi * 2 * self.radio)

    # Modificar el radio si nuevo_radio > 0
    def modificar_radio(self, nuevo_radio: float):
        if nuevo_radio > 0:
            self.radio= nuevo_radio
        else:
            print("Error. El nuevo radio debe ser mayor a 0")

    # Creo una nueva instancia de circulo con el radio n veces mas grande. La verificacion de n > 0 se hace en __new__
    def multiplicar_circulo(self, n: int):
        nuevo_circulo= Circulo(self.radio * n)
        return nuevo_circulo

    def __str__(self):
        return (f"El circulo tiene un radio de {self.radio} cm")

def mostrar(circulo):
    if circulo != None:
        print(circulo)

def test():
    import doctest
    doctest.testmod()
    
# MAIN
if __name__ == '__main__':
    try:
        r= float(input("Ingrese radio: "))
        circulo= Circulo(r)
        mostrar(circulo)
        print(f"Area del circulo: {circulo.calcular_area()}")
        print(f"Perimetro del circulo: {circulo.calcular_perimetro()}")
        circulo.modificar_radio(10)
        otro_circulo = circulo.multiplicar_circulo(0)
        mostrar(circulo)
        mostrar(otro_circulo)
        test()
    except BaseException:
        pass