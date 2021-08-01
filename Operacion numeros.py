class Basico:
    def  numerosN(self,n):
        for x in range(1,n):
            print (x)

    def Multiplo(self,numero):
        multiplos=[]
        i = 1
        multiplo = numero
        while multiplo:
            multiplos.append(multiplo)
            i += 1
            multiplo = numero * i
        return multiplos

    def DivisoresNumero(self,numero):
        cont=1
        divisores=[]
        for cont in range(1,numero):
            rec = numero % cont
            if rec == 0:
                divisores.append(cont)
        return divisores

    def primo(self,numero):
        contador = 0
        for i in range(1,numero+1):
            if numero % i == 0:
                contador += 1
        if contador ==2:
            return True
        else:
            return False

    def perfecto(self,numero):
        acu=0
        for i in range(1,numero):
            if numero % i ==0:
                acu=acu+i
        if numero == acu:
            print("{} es Perfecto".format(numero))
        else:
            print("{} no es Perfecto".format(numero))

class   Intermedio(Basico):

    def numerosN(self,n):
        suma = 0
        for i in range(1, n + 1):
            suma += i
        return suma

    def factorial(self,num):
        if num>=1:
            f=num
            while num>=2:
                num=num-1
                f=f*(num)
            print("el factorial es: ",f)
        if num==0:
            print("el factorial es 1")

    def fibonacci(self,n):
        a, b = 0,1
        while a < n:
            print(a, end=' ')
            a, b = b, a+b
        print()

    def amigos(self,num1,num2):
        suma_num1=0
        suma_num2=0
        for i in range(1,num1):
            if num1%i==0:
                suma_num1+=i
        for k in range(1,num2):
            if num2%k==0:
                suma_num2+=k
        return suma_num1==num2 and suma_num2==num1

# basi = Basico()
# print(basi.numerosN(20))
#print(basi.Multiplo(6))
#mult = basi.Multiplo(5)
#print(mult)
#print(basi.DivisoresNumero(6))
#print(basi.primo(13))
#print(basi.perfecto(5))
inter = Intermedio()
print(inter.numerosN(10))
#print(inter.factorial(5))
#print(inter.fibonacci(1000))
# n_1=int(input('Introduzca el nº 1: '))
# n_2=int(input('Introduzca el nº 2: '))
# if (n_1,n_2):
#     print ('¡Son amigos! :)')
# else:
#     print ('No son amigos :(')