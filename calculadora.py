from typing import AsyncIterable


class Calculadora:
    def __init__(self,numero1, numero2):
        self.num1 = numero1
        self.num2 = numero2

    def suma(self):
        return self.num1 + self.num2

    def resta(self):
        return self.num1 - self.num2

    def multiplicacion(self):
        multi = self.num1*self.num2
        print("{}*{}={}".format(self.num1,self.num2,multi))

    def division(self):
        return self.num1/self.num2

class CalEstandar(Calculadora):
    def __init__(self, numero1,numero2):
        super().__init__(numero1,numero2)

    def multiplicacion(self):
        return self.num1*self.num2

    def exponente(self):
        resultado = 1
        for i in range(self.num2):
            resultado *= self.num1
        return resultado

    def valorAbsoluto(self,numero):
        if numero < 0:
            numero = numero*-1
        return numero

class CalCientifica(Calculadora):
    def __init__(self, numero1, numero2):
            super().__init__(numero1, numero2)

    def circunferencia(self,radio):
        pi = 3.1416
        circun =2*pi*radio
        return circun

    def areaCirculo(self,radio):
        pi = 3.1416
        area = pi * radio **2
        return ("El area del circulo es igual a {:.2f}".format(area))

    def areaCuadrado(self,lado):
        area = lado*lado
        return area

def mensaje(men):
    print(men)
#cal = CalEstandar(3,3)
# print(cal.suma())
# print(cal.multiplicacion())
# print(cal.valorAbsoluto(-5))
cienti = CalCientifica(3,3)
# cienti.circunferencia()
# print(cienti.suma())
#print(cal.exponente())
# cienti.circunferencia(3)
# print(cienti.circunferencia(3))
# cienti.areaCirculo(5)
# print(cienti.areaCirculo(5))
cienti.areaCuadrado(5)
print(cienti.areaCuadrado(5))