'''VARIABLE: ubicación de memoria reservada donde se almacenan y manipulan datos
   - En Python no se declaran, se crean cuando se le asigna un nombre y se les da un valor
'''

suma=1+2
print(suma)

# DEFINICIÓN DE UNA VARIABLE
nombre='Luis'
edad=28
pais='Portugal'
print('Nombre:', nombre, '\nPaís:',pais, '\nEdad: ',edad)

# Asignar un valor a una variable
a=1
print(a)
a=3*4
print(a)
a='Python' #asigna una cadena a la variable
print(a)

# VARIABLES
# Lo ideal es declara e inicializar siempre las variables.
# ---------------------------------------

# En Python podemos asignar una variable a otra variable diferente.
var = "Hola mundo"
var2 = var #la variable var y var2 apuntan a la misma cadena de texto Hola mundo
print(var2)

''''Los nombres de las variables en Python  pueden tener cualquier longitud y pueden consistir en letras mayúsculas y
minúsculas (A-Z, a-z), dígitos (0-9) y el carácter de subrayado (_). 
Cualquier
otro carácter dará error:'''
'var& = "Hola mundo"'
#Aunque el nombre de una variable puede contener dígitos, el primer carácter de
# un nombre de variable no puede ser un dígito.
'2var = "Hola mundo"'

#El nombre de las variables en Python es sensible a mayúsculas y minúsculas
Var3 = "Hola mundo"
#print(var3) #Error, no se encuentra var3

# Declaración de variable numérica entera:
n_edad = 47
print(n_edad)

# Declaración de variable numérica de coma flotante:
n_numero = -23.5245

# Declaración de variable de tipo string:
s_nombre = 'Manolo es "amigo" mío'

# Declaración de variable de tipo string en varias líneas:
s_textoLargo = """Esto es un mensaje
...con tres saltos
...de linea"""

#Podemos cambiar el tipo de dato de las variables
# Sobreescribimos el valor de la variable n_edad y ahora la ponemos como string:
n_edad = "Cuarenta y Siete"
print(n_edad)

# Declaración de constante:
NUMEROPI = 3.14159

# Declaración de un boolean
is_verdadero = True
is_casado = False
print(is_verdadero,is_casado)

is_verdadero == 1 # es lo mismo que lo anterior
is_casado == 0
print(is_verdadero,is_casado)

# True = 1 y False = 0
True == 1
False == 0
print(True + 2)

# Cuando se valida una condición , Python devuelve True o False:
print(10 > 9)
print(10 == 9)
print(10 < 9)

# Declaración múltiple
# En una sola instrucción, estamos declarando tres variables: a, b y c, y 
# asignándoles un valor concreto a cada una.
a, b, c = 'string', 15, True

# Sería como poner:
a = 'string'
b = 15
c = True

# Para verificar el tipo de cualquier objeto en Python, usamos la función type() :
print(type(n_edad))
print(type(n_numero))
print(type(s_nombre))
print(type(NUMEROPI))
print(type(is_verdadero))

########################################### UDEMY

'VARIABLES'
X=5
nombre="Juan"
lista =['1','2','3','4','5'] #lista en la que asignamos múltiples valores
pais ='México'


# En python, el tipado de datos es DINÁMICO: el tipo de dato y el valor de la variable
# lo podemos cambiar en cualquier momento

nombre=1 #ANTES --> nombre="Juan"
