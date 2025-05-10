def suma(a,b): #modificamos los valores de a y b dentro de la función suma
    a=3
    b=4
    return a+b 

a,b=5,10 

print(suma(a,b)) #imprime 7
#a y b no cambian fuera de la función
print(a,b) #imprime 5 10