#SINTAXIS Y LLAMADA A FUNCIONES
#definición de funciones
def suma(a,b):
    return a+b

def en_pantalla(frase1,frase2):
    print(frase1,frase2)

suma(2,3)
en_pantalla('Resultado de 2+3=',suma(2,3))
en_pantalla('Me gusta','Python')

#POLIMORFISMO
x=suma(2.7,4.2)
en_pantalla('Resultado de X: ',x)

#FUNCIONES ANIDADAS
def funcion1(a):
    b=100
    print ('Funcion 1:',a)

    def funcion2(x):
        print ('Resultado de funcion2:',x)

    # Llamada a la funcion2
    funcion2(b)

#llamada a la funcion principal 1    
funcion1('Python')

#RECURSIVIDAD: una función puede llamarse a sí misma. Debe devolver un valor para que no haya recursividad infinita
def factorial(x):
    
    if x>1:
        a=x*factorial(x-1) #la recursividad se cumple cuando x>1
        return a
    else: 
        return 1

#ejecucion del factorial
print('Factorial de 5 =',factorial(5))

#DEVOLVER MÚLTIPLES VALORES SIMULTÁNEAMENTE
def devolver_valores_multiples(lista):
    return max(lista),min(lista) #devuelve una tupla de 2 elementos

l = [1,3,5,6,0]
maximo, minimo = devolver_valores_multiples(l) #desempaqueta la tupla en 2 variables

print(minimo,maximo, sep=' ')


# EJERCICIO: Saber si un número es primo

def esPrimo(x):
    primos =[]
    
    for i in range (2,x+1):
        while (x%i==0):
            primos.append(i)
            x=x/i
            
    print(primos)

esPrimo(7)
esPrimo(12)

#AMBITOS DE VARIABLES
a='Python' #ámbito global

print(a)

def funcion():
    a=33
    print('Valor dentro:', a) #ámbito local a la funcion

funcion()
print('Valor fuera: ',a) #ámbito global (al módulo)

#ARGUMENTOS DE LAS FUNCIONES: se pasan por referencia
# --- 
def suma(a,b):
    a=3
    b=4
    print(a+b)
    return a+b

a,b=5,10
print('suma dentro de la funcion: ', suma(a,b))
print('a:',a, 'b: ',b)

# PASOS DE ARGUMENTOS A FUNCIONES
'''
- Por POSICIÓN (por defecto): en el mismo orden en el que está definida la función
- Por KEYWORDS (palabras clave): se pasan indicando el nombre del argumento y su valor, con el orden que queramos
'''

'POR POSICIÓN'
def f(a,b,c):
    print(a,b,c)

print('POR POSICION',f(1,2,3))
print('POR KEYWORDS',f(c=12, a=10, b=100))

