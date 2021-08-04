import os
from calculadora import CalEstandar, CalCientifica
from OperacionNumeros import Basico, Intermedio
from TratamientoListas import Lista
from OperacionesCadenas import Cadena

class Menu:
    def __init__(self,titulo,opciones=[]):
        self.titulo=titulo
        self.opciones=opciones
    def menu(self):
        print(self.titulo)
        for opcion in self.opciones:
            print(opcion)
        opc=input("\033[1;31m"+"Elija opcion[1...{}]:".format(len(self.opciones)))
        return opc

opc =""
while opc !="5":
    os.system("cls")
    men = Menu("\033[3;36m"+"Menu Principal",["\033[0;35m"+"1) Calculadora","2) Operacion Numeros","3) Tratamiento de Listas","4) Operaciones de Cadenas","5) Salir"])
    opc = men.menu()
    if opc == "1":
        opc1 =""
        while opc1 !="4":
            os.system("cls")
            men1 = Menu("\033[3;36m"+"Menu Calculadora",["\033[0;33m"+"1) Suma","2) Resta","3) Multiplicacion","4) Division","5) Exponente","6) Valor Absoluto","7) Circunferencia","8) Area Circulo","9) Area Cuadrado","10) Salir"])
            opc1 = men1.menu()
            os.system("cls")
            if opc1 == "1":

                print("\033[1;32m"+"Suma de dos Numeros")
                n1 = int(input("\033[0;37m"+"Ingrese numero 1: "))
                n2 = int(input("\033[0;37m"+"Ingrese numero 2: "))
                cal = CalEstandar(n1,n2)
                print(cal.suma())
                input("\033[0;34m""Presione una tecla para continuar...")

            elif opc1 == "2":
                print("\033[1;32m"+"Resta de dos Numeros")
                n1 = int(input("\033[0;37m"+"Ingrese numero 1: "))
                n2 = int(input("\033[0;37m"+"Ingrese numero 2: "))
                cal = CalEstandar(n1,n2)
                print(cal.resta())
                input("\033[0;34m"+"Presione una tecla para continuar...")

            elif opc1 == "3":
                print("\033[1;32m"+"Multiplicacion de dos Numeros")
                n1 = int(input("\033[0;37m"+"Ingrese numero 1: "))
                n2 = int(input("\033[0;37m"+"Ingrese numero 2: "))
                cal = CalEstandar(n1,n2)
                print("{}*{}={}".format(n1,n2,cal.multiplicacion()))
                input("\033[0;34m"+"Presione una tecla para continuar...")

            elif opc1 == "4":
                print("\033[1;32m"+"Division de dos Numeros")
                n1 = int(input("\033[0;37m"+"Ingrese numero 1: "))
                n2 = int(input("\033[0;37m"+"Ingrese numero 2: "))
                cal = CalEstandar(n1,n2)
                print(cal.division())
                input("\033[0;34m"+"Presione una tecla para continuar...")

            elif opc1 == "5":
                print("\033[1;32m"+"Exponente de un Numeros")
                n1 = int(input("\033[0;37m"+"Ingrese el valor de la base: "))
                n2 = int(input("\033[0;37m"+"Ingrese su exponente: "))
                cal = CalEstandar(n1,n2)
                print(cal.exponente())
                input("\033[0;34m"+"Presione una tecla para continuar...")

            elif opc1 == "6":
                print("\033[1;32m"+"Valor absoluto de un Numero")
                n1 = int(input("\033[0;37m"+"Ingrese numero 1: "))
                n2 = int(input("\033[0;37m"+"Ingrese numero 2: "))
                cal = CalEstandar(n1,n2)
                print("{}*{}={}".format(n1,n2,cal.valorAbsoluto()))
                input("\033[0;34m"+"Presione una tecla para continuar...")

            elif opc1 == "7":
                print("\033[1;32m"+"Circunferencia de un circulo")
                radio = int(input("\033[0;37m"+"Ingrese el radio del circulo: "))
                cienti = CalCientifica(radio)
                print(cienti.circunferencia())
                input("\033[0;34m"+"Presione una tecla para continuar...")

            elif opc1 == "8":
                print("\033[1;32m"+"Area de un circulo")
                radio = int(input("\033[0;37m"+"Ingrese el radio del circulo: "))
                cienti = CalCientifica(radio)
                print(cienti.areaCirculo)
                input("\033[0;34m"+"Presione una tecla para continuar...")

            elif opc1 == "9":
                print("\033[1;32m"+"Area de un cuadrado")
                lado = int(input("\033[0;37m"+"Ingrese el lado del cuadrado: "))
                cienti = CalCientifica(n1,n2)
                print(cienti.areaCuadrado())
                input("\033[0;34m"+"Presione una tecla para continuar...")


    elif opc == "2":
        opc2 =""
        while opc2 !="4":
            os.system("cls")
            men2 = Menu("\033[3;36m"+"Menu Operacion Numeros",["\033[0;33m"+"1) Presentar los numeros del 1 al n.","2) Sumar los números de 1 a n.","3) Multiplo de un numero,","4) Presentar los divisores de un numero.","5) Numero primo.","6) Factorial de cualquier numero.","7) Fibonacci de una serie de n números","8) Perfecto","9) Primos gemelos","10) Numeros amigos","11) Salir"])
            opc2 = men2.menu()
            os.system("cls")

            if opc2 == "1":
                print("\033[1;32m"+"Presentacion de los numeros del 1 al n")
                n = int(input("\033[0;37m"+"Ingrese hasta que numero quiere presentar: "))
                basi = Basico()
                print(basi.numerosN())
                input("\033[0;34m""Presione una tecla para continuar...")

            elif opc2 == "2":
                print("\033[1;32m"+"Suma de numeros de 1 a n")
                n1 = int(input("\033[0;37m"+"Ingrese hasta que numero quiere sumar: "))
                inter = Intermedio()
                print(inter.numerosN())
                input("\033[0;34m""Presione una tecla para continuar...")

            elif opc2 == "3":
                print("\033[1;32m"+"Multiplo de cualquier numero")
                n1 = int(input("\033[0;37m"+"Ingrese un numero: "))
                basi = Basico()
                print(basi.Multiplo())
                input("\033[0;34m""Presione una tecla para continuar...")

            elif opc2 == "4":
                print("\033[1;32m"+"Divisores de un numero")
                n1 = int(input("\033[0;37m"+"Ingrese un numero: "))
                basi = Basico()
                print(basi.DivisoresNumero())
                input("\033[0;34m""Presione una tecla para continuar...")

            elif opc2 == "5":
                print("\033[1;32m"+"Numeros primos")
                n1 = int(input("\033[0;37m"+"Ingrese un numero: "))
                basi = Basico()
                print(basi.primo())
                input("\033[0;34m""Presione una tecla para continuar...")

            elif opc2 == "6":
                print("\033[1;32m"+"Factorial de un numero")
                n1 = int(input("\033[0;37m"+"Ingrese un numero: "))
                inter = Intermedio()
                print(inter.factorial())
                input("\033[0;34m""Presione una tecla para continuar...")

            elif opc2 == "7":
                print("\033[1;32m"+"Fibonacci de una serie de n numeros")
                radio = int(input("\033[0;37m"+"Ingrese un numero: "))
                inter = Intermedio()
                print(inter.fibonacci())
                input("\033[0;34m""Presione una tecla para continuar...")

            elif opc2 == "8":
                print("\033[1;32m"+"Perfecto")
                radio = int(input("\033[0;37m"+"Ingrese un numero: "))
                basi = Basico()
                print(basi.perfecto())
                input("\033[0;34m""Presione una tecla para continuar...")

            elif opc2 == "9":
                print("\033[1;32m"+"Primos gemelos")
                n1 = int(input("\033[0;37m"+"Ingrese numero 1: "))
                n2 = int(input("\033[0;37m"+"Ingrese numero 2: "))
                inter = Intermedio()
                print(inter.primosGemelos())
                input("\033[0;34m""Presione una tecla para continuar...")

            elif opc2 == "10":
                print("\033[1;32m"+"Numeros amigos")
                n1 = int(input("\033[0;37m"+"Ingrese numero 1: "))
                n2 = int(input("\033[0;37m"+"Ingrese numero 2: "))
                inter = Intermedio()
                print(inter.amigos())
                input("\033[0;34m""Presione una tecla para continuar...")

    elif opc =="3":
            print("Listas")


    elif opc == "4":
            print("Cadenas")

    elif opc == "5":
            print("Gracias por usar el sistema ")
    else:
            print("Opcion no valida")

print("Lo esperamos en una proxima ocasion")