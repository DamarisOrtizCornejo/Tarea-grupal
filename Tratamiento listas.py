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

    # def eliminarLista(self,valor):
    #     result = []
    #     for ele in lista:
    #         if ele not in result:
    #             result.append(ele)
    #         else:
    #             lista.remove(ele)

    def copiarTuplaLista(self,tupla):
        listaT=list(tupla)
        return listaT

lista = [2,4,6,8,6,5]
List = Lista(lista)
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
tupla=(1,2,3,4,5)
#lista=list(tupla)
print(List.copiarTuplaLista)

