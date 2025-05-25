# Definir la función para comprobar si un valor es par 
def par(numero):
    esPar=False
    if (numero%2==0):
        esPar=True
    return esPar
    
print(par(22))
print(par(13))