class Animal:
    def comer():
        print('Como muchas veces al día')

    def dormir():
        print('Duermo muchas horas')

#Animal --> Padre 
#Perro --> Hija
class Perro(Animal): 
    def hacer_sonido():
        print('Puedo ladrar')

#PROGRAMA PRINCIPAL
print('***Ejemplo de herencia en Python***')

print('CLASE PADRE: Soy un animal')
animal1=Animal() #Python crea por defecto el constructor vacío
animal1.comer()
animal1.dormir()

print('CLASE HIJA: soy un Perro')
perro1=Perro()
perro1.comer()
perro1.dormir()
perro1.hacer_sonido()
