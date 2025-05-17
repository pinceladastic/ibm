#OBJETOS MUTABLES

# Cuando pasamos un objeto mutable a una función que lo modifica internamente,
# el cambio afecta al exterior de la función

def minimo(l):
    l[0]= 1000   #modificamos el primer valor de la lista
    return min(l) #min devuelve el mínimo de un iterable o de 2 o más argumentos

l=[1,2,3]
print('l antes de llamar a la funcion: ',l)   #imprime 1,2,3

#print('Resultado de la función: ', minimo(l))  #en esta función se modifica el primer valor de la lista
                                               #imprime 2

print('l después de llamar a la función: ',l)  # imprime 1000,2,3

# PARA EVITAR ESTO, PODEMOS HACER UNA COPIA DE LAS LISTA QUE LE PASAMOS A LA FUNCIÓN
l2=l[:]

print('Resultado de la función al pasarle l2: ', minimo(l2))
print(l)
