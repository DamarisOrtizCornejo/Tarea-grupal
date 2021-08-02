class Lista:
    def __init__(self,lista):
        self.lista=lista

    def presentarLista(self):
        for ele in self.lista:
            print(ele)

    def buscarLista(self,valor):
        enc=False
        for pos,ele in enumerate(self.lista):
            if ele == valor:
                enc=True
                break
        if enc ==True:return pos
        else:return -1

    def listaFactorial(self,num):
        import math
        lista = []
        for c in range(1,num):
            facto = math.factorial(c)
            self.lista.append(facto)
        return lista

#     def listaPrimo(n):
#         lista_primos=[2]
#         for i in range(3,n+1,2):
#             primo=True
#             for j in range(3,int(sqrt(i)+1),2):
#                 if (i%j==0):
#                     primo=False
#                     break
#                 if primo:
#                     lista_primos.append(i)
#                     return lista_primos
# print(primos_hasta(1000))

    def insertarLista(self,valor,posicion):
        auxlista=[ ]
        for pos,ele in enumerate(self.lista):
            if valor < ele:
                auxlista.append(valor)
                break
            self.lista=self.lista[0:pos]+auxlista+self.lista[pos:]

    def eliminarLista(self,valor):
        for ele in self.lista:
            self.lista.remove(valor)
            return

    def retornaValorLista(self,posicion):
        num=self.lista.pop(posicion)
        return num

    def copiarTuplaLista(self,tupla):
        pass

lista = [2,4,6,8,6,5]
List = Lista()
# List.presentarLista()
# print(List.lista)
#print(List.buscarLista(3))
# valor = 8
# resp = List.buscarLista(valor)
# if resp !=-1:
#     print("Numero = {} se encuentra en la Posicion:({}) de la lista:{}".format(valor,resp, List.lista))
# else:
#     print("Numero = {} no se encuentra en la lista:{}".format(valor,List.lista))
# lista.insert (1,6)
# print(lista)
# print(List.eliminarLista(lista))
print(List.retornaValorLista(5))
tupla=(1,2,3,4,5)
lista=list(tupla)
print(lista)

