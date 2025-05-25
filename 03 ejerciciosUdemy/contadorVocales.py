# Declarar la variable
cadena='María José'
# Agregar el ciclo for
i=0
for x in cadena:
    if(x in ['a','e','i','o','u','A','E','I','O','U','Á','É','Í','Ó','Ú','á','é','í','ó','ú']):
        i=i+1
        
# Imprimir la cantidad de vocales encontradas en la cadena
print(i)