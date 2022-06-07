class Nodo:

    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None
        self.anterior = None

class ListaC:

    def __init__(self):
        self.primero = None
        self.ultimo = None

    def vacia(self):
        if self.primero == None:
            return True
        else:
            return False
    
    def insertar(self, dato):
        if self.vacia():
            self.primero = self.ultimo = Nodo(dato)
        else:
            aux = self.ultimo
            self.ultimo = aux.siguiente = Nodo(dato)
            self.ultimo.anterior = aux
        self.unir()

    def unir(self):
        if self.primero is not None:
            self.primero.anterior = self.ultimo
            self.ultimo.siguiente = self.primero
    
    def ImprimirIF(self):
        aux = self.primero
        while aux:
            print('Dato: ', aux.dato)
            aux = aux.siguiente
            if aux == self.primero:
                break

    def buscar(self, dato):
        aux = self.primero
        while aux:
            if aux.dato == dato:
                print('Anterior: ', aux.anterior.dato)
                print('Actual: ', aux.dato)
                print('Siguiente: ', aux.siguiente.dato)
                break
            else:
                aux = aux.siguiente
                if aux == self.primero:
                    print('El valor no existe. ')
                    return

lst = ListaC()
class Principal():
    
    def datos():
               
        lst.insertar('32')        
        lst.insertar('40')        
        lst.insertar('58')
        lst.insertar('21')
        lst.insertar('56')
        lst.insertar('77')
        #print("")  
        print('Datos insertados, imprimiendo de inicio a fin.')
        lst.ImprimirIF()
        print('')
        a = input('Ingrese un número de la lista.\n')
        lst.buscar(a)
    datos()