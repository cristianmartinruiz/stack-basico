"""PILA (STACK) BÁSICA 
En programación, un "stack" es una estructura de datos que sigue el principio de LIFO (Last In, First Out),
lo que significa que el último elemento agregado a la pila es el primero en ser retirado. 
Imagina una pila de platos: cuando apilas un nuevo plato, este se coloca en la parte superior de la pila, 
y cuando retiras un plato, siempre tomas el de arriba primero.
En Python, puedes implementar un stack utilizando una lista. Puedes agregar elementos a la pila utilizando 
el método `append()`, y puedes retirar elementos de la pila utilizando el método `pop()` sin ningún índice 
especificado, ya que `pop()` por defecto elimina y devuelve el último elemento de la lista.
Los stacks son útiles en muchas situaciones, como algoritmos de búsqueda y recorrido, manejo de llamadas a 
funciones (con la pila de llamadas), manejos de historial y navegación y más.
Crea una clase "Pila" que represente una pila (stack) básica. Implementa métodos para agregar elementos a 
la pila, quitar elementos y mostrar el contenido actual.
Por supuesto, estaré encantado de explicarte qué es un "stack" en el contexto de la programación y cómo se 
utiliza en Python."""

class Pila:
    def __init__ (self):
        self.items = []

    def agregar(self, elemento):
        self.items.append (elemento)

    def quitar (self):
        if not self.esta_vacia():
            return self.items.pop()
    
        else:
            print("La pila esta vacia.") 

    def esta_vacia (self):
        return len(self.items) == 0

    def mostrar_contenido(self):
        print ("Contenido de la pila:", self.items)        

# Ejemplo de uso

pila = Pila ()
pila.agregar (5)
pila.agregar (10)
pila.mostrar_contenido ()
pila.quitar ()
pila.mostrar_contenido()
