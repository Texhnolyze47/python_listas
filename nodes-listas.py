class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        

class LinkedList:
    def __init__(self):
        self.head = None
        self.last = None  

    #metodo para comprobar 
    def isEmpty(self):
        return self.head

    def add(self, key):
        #creamos un objecto de la clase node
        nodo = Node(key)
        #comprobamos si esta vacia la lista
        if not self.isEmpty():
            #colocamos el dato al principio
            self.head = nodo
            #
            self.last = nodo

        else:
            #mueve el primer elemento al segundo
            nodo.next = self.head
            #el nuevo elemento va ser el nodo 
            self.head = nodo

    def print (self):
        #creamos un indice
        i = self.head #apunta a la cabeza
        while i:
            #imprimi el dato 
                print(i.data)
            #camvbia al siguiente elemento 
                i = i.next
            #imprime
                print()


    def search(self, key):
        #indice
        i = self.head
        while i:
            #comparamos el data que estamos buscando
            if  int(i.data) == int(key):
                #al encontrarlo se muestra
                print("El numero " + key + " existe ")
                return True
                #busca en la siguienre posicion
            i = i.next 
            #si no lo encuentra returna falso
        return False
    
    def delete(self,  key):
        curr = self.head
        prev = None
        #compara los datos
        while curr and curr.data != key:
            prev = curr
            curr = curr.next
        if prev is None:
            #si no hay nada pasa a la siguiente posiocion
            self.head = curr.next
        elif curr:
            #borra el dato
            prev.next = curr.next
            curr.next = None
                        
    #no se implemento
    # def modify(self, x , y):
    #     if x == y:
    #         return
 
    #     prevX = None
    #     currX = self.head
    #     while currX != None and currX.data != x:
    #         prevX = currX
    #         currX = currX.next
 
    #     prevY = None
    #     currY = self.head
    #     while currY != None and currY.data != y:
    #         prevY = currY
    #         currY = currY.next
 
    #     if currX == None or currY == None:
    #         return
    #     if prevX != None:
    #         prevX.next = currY
    #     else:  
    #         self.head = currY
 
        
    #     if prevY != None:
    #         prevY.next = currX
    #     else:  
    #         self.head = currX
 
   
    #     temp = currX.next
    #     currX.next = currY.next
    #     currY.next = temp



if __name__ == "__main__":
    # instacia la clase
    ll = LinkedList()
 
    while(True):
        print("---Menu---\n"+
              "1.- Insertar Numero\n"+
              "2.- Mostrar Datos\n"+
              "3.- Buscar Datos\n"+
              "4.- Eliminar Datos\n"+
              "5.- Modificar Datos\n"+
              "6.- Salir\n")
              
        num = input("Selecciona la opcion a trabajar: ")

        if num == "1":
            numero = input("Inserta un numero ")
            ll.add(numero)
        elif num == "2":
            ll.print()
        elif num == "3":
            numero = input("Inserta un numero ")
            ll.search(numero)
        elif num == "4":
            numero = input("Inserta un numero ")
            ll.delete(numero)
        elif num == "5":
            posicion = input("Inserta un numero ")
            cambio = input("Inserta un numero ")
            ll.modify(1,3)
            ll.print()
        elif num == "6":
            break
            