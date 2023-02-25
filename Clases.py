class Prenda():
    def __init__(self, tipo, estilo, color, nombre):
        self.color = color
        self.estilo = estilo
        self.tipo = tipo
        self.nombre = nombre
class Pintas():
    def __init__(self,cabeza = None,torso  = None,piernas  = None,zapatos  = None):
        self.cabeza = cabeza
        self.torso = torso
        self.piernas = piernas
        self.zapatos = zapatos

class Pinta():
    def __init__(self):
        self.prendas = []
    
    def add_prenda(self, prenda):
        self.prendas.append(prenda)

    def mostrar(self):
        print(self.prendas)

class Armario():
    def __init__(self):
        pass

class Frontera():
    def __init__(self):
        self.frontera =[]
    
    def empty(self):
        return (len(self.frontera) == 0)

    def add(self, prenda):
        self.frontera.append(prenda)
    
    def eliminar(self):
        # LIFO o FIFO
        pass

    def contiene_estado(self, estado):
        return any(nodo.estado == estado for nodo in self.frontera)

class Pila(Frontera):
    def eliminar(self):
        if self.empty():        
            raise Exception("Frontera vacia")
        else:
            # Guardamos el ultimo item en la lista 
            # (el cual es el nodo recientemente añadido)
            nodo = self.frontera[-1]
            # Guardamos todos los items excepto el 
            # ultimo (eliminamos)
            self.frontera = self.frontera[:-1]
            return nodo
    
class Cola(Frontera):
    def eliminar(self):
        # Termina la busqueda si la frontera esta vacia
        if self.empty():        
            raise Exception("Frontera vacia")
        else:
            # Guardamos el primer item en la lista 
            # (el cual es el nodo añadido de primero)
            nodo = self.frontera[0]
            # Guardamos todos los items excepto el 
            # primero (eliminamos)
            self.frontera = self.frontera[1:]
            return nodo

class Armario():
    def __init__(self):
        # formato tipo, estilo, color, nombre 
        with open('C:\\Users\\wilhe\\OneDrive\\Escritorio\\inte\\taea\\Prendas.txt') as file:
            contenido = file.read()
        contenido = contenido.splitlines()
        self.fron = []
        #print(contenido)
        for i in contenido:
            tipo, estilo, color, nombre = i.split(", ")
            self.fron.append(Prenda(tipo, estilo, color, nombre))
        self.combitacion(self.fron)
        
    def combitacion(self,fron):
        fron1 = fron
        elem = ["cabeza","torso","piernas","zapatos"]
        bus1 = []
        bus2 = []
        bus3 = []
        bus4 = []
        for prenda in fron1:
            if prenda.tipo == elem[0]:
                bus1.append([prenda])
            elif prenda.tipo == elem[1]:
                for i in range(0,len(bus1)):
                    elm2 = bus1[i][0]
                    bus2.append([elm2,prenda])
            elif prenda.tipo == elem[2]:
                for j in range(0, len(bus2)):
                    elm3 = bus2[j]
                    bus3.append([elm3[0],elm3[1],prenda])
                    #print(bus4)
            elif prenda.tipo == elem[3]:
                for k in range(0,len(bus3)):    
                    elm4 = bus3[k]
                    bus4.append([elm4[0],elm4[1],elm4[2],prenda])
        pintaf = []
        for pinta in bus4:
            pintaf.append(Pintas(pinta[0],pinta[1],pinta[2],pinta[3]))
            
                        
        print(pintaf[1].cabeza.nombre)
        print(pintaf[1].torso.nombre)
        print(pintaf[1].piernas.nombre)
        print(pintaf[1].zapatos.nombre)
        return pintaf
                    
                    
a = Armario()

