#MANEJO DE CADENAS

#Dividir una cadena con split
cadena='Hola Mundo'
palabras=cadena.split()
print(palabras)

#parsing --> dividir una cadena en subcadenas a partir de un det. caracter o conjunto de caracteres
palabras=cadena.split('M') #la M se descarta
print(palabras)

#Buscar (find) y reemplazar (replace)
posicion='Hola Mundo'.find('mundo') #devuelve -1, pk tiene en cuenta las may/min
print(posicion)
cadena2='Hola Mundo'
posicion='Hola Mundo'.find('Mundo') #devuelve 5, la posición de la 1º ocurrencia en cadena
print(posicion)

nuevaCadena=cadena2.replace('Mundo','Amigo')
print(nuevaCadena)
print(cadena)
nuevaCadena=cadena.replace('Mundo','Amigo', posicion) #usando la posicion

#Concatenación de cadenas
c1='Hola '
c2='Mundo'
print('Concatenación:',c1+c2)
print('Concatenación:',"".join([c1+c2])) #usando el método join del objeto str

#Multiplicación de cadenas
cadena='Hola'
nuevaCadena=cadena*5
print(nuevaCadena)

#Strip --> Limpia una cadena
cadena='      Hola  '
limpia=cadena.split()
print(limpia)

cadena='.......Hola...'
limpia=cadena.split('.')
print(limpia)
cadena=3
print(cadena)
