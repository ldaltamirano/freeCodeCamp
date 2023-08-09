# Python

# Palabras reservadas

# False – Valor booleano, resultado de operaciones de comparación u operaciones lógicas en Python
# None – Representa a un valor nulo
# True – Valor booleano, igual que false, resultado de operaciones de comparación u operaciones lógicas en Python
# __peg_parser__ – Llamado huevo de pascua, relacionado con el lanzamiento del nuevo analizador PEG no está definido aún.
# And – Operador lógico
# As – Se utiliza para crear un alias al importar un módulo.
# Assert – Se utiliza con fines de depuración
# Async – Proporcionada por la biblioteca ‘asyncio’ en Python. Se utiliza para escribir código concurrente en Python
# Await – Proporcionada por la biblioteca ‘asyncio’ en Python. Se utiliza para escribir código concurrente en Python
# Break – Se utiliza en el interior de los bucles for y while para alterar su comportamiento normal
# Class – Se usa para definir una nueva clase definida por el usuario
# Continue – Se utiliza en el interior de los bucles for y while para alterar su comportamiento normal
# Def – se usa para definir una función definida por el usuario
# Del – Para eliminar un objeto
# Elif – Se usa en declaraciones condicionales, igual ‘else’ e ‘if’
# Else – Se usa en declaraciones condicionales, igual ‘elif’ e ‘if’
# Except – Se usa para crear excepciones, qué hacer cuando ocurre una excepción, igual que ‘raise’ y ‘try’
# Finally – Su uso garantiza que el bloque de código dentro de él se ejecute incluso si hay una excepción no controlada
# For – Utilizado para hacer bucles. Generalmente lo usamos cuando sabemos la cantidad de veces que queremos que se ejecute ese bucle
# From – Para importar partes específicas de un módulo
# Global – Para declarar una variable global.
# If – Se usa en declaraciones condicionales, igual ‘else’ y ‘elif’
# Import – Para importar un módulo
# In – Para comprobar si un valor está presente en una lista, tupla, etc. Devuelve True si el valor está presente, de lo contrario devuelve False
# Is – Se usa para probar si las dos variables se refieren al mismo objeto. Devuelve True si los objetos son idénticos y False si no
# Lambda – Para crear una función anónima
# Nonlocal – Para declarar una variable no local
# Not – Operador lógico
# Or – Operador lógico
# Pass – Es una declaración nula en Python. No pasa nada cuando se ejecuta. Se utiliza como marcador de posición.
# Raise – Se usa para crear excepciones, qué hacer cuando ocurre una excepción, igual que ‘except y ‘try’
# Return – Se usa dentro de una función para salir y devolver un valor. 
# Try – Se usa para crear excepciones, qué hacer cuando ocurre una excepción, igual que ‘raise’ y ‘except
# While – Se usa para realizar bucles.
# With – Se usa para simplificar el manejo de excepciones
# Yield – Se usa dentro de una función al igual que ‘return’, salvo que ‘yield’ devuelve un generador.


# Asignaciom

x = 43
x = x + 1
print(x)
# imprime 44

# Operadores

x = x + 1 #suma
x = x - 1 #resta
x = x * 1 #multiplicacion
x = x / 1 #division
x = x ** 1 #exponente
x = x % 1 #resto

# Precedencia

() #parentesis
x = x ** 1 #exponente
x = x * 1 #multiplicacion
x = x / 1 #division
x = x + 1 #suma
x = x - 1 #resta

# Input() - Lectura de datos que teclea el usuario
nam = input("Quien sos?")
print("Bienvenido", nam)

# Operadores de comparacion
# < <= == != >= >

# Condicionales
if x > 0:
    print("0")
elif:
    print("2")
else:
    print("1")

# Funciones - def - return
def funcion():
    print("funcion")
    return "ok"

# Iteraciones - While - Break
n = 0
while True:
    if n == 3:
        break
    print(n)
    n = n + 1

# Iteraciones - for ... in
for i in [2,1,5]:
    print(i)

# Strings

# len - Cantidad de caracteres
cant = len("banana")

# slicing - Es para substrings
s = "lucio"
print(s[0:4])
# luci

# concatenacion 
s = "luc" + "io"

# Operador logico en string - in
"n" in  "banana"
# True
"m" in  "banana"
# false
"nan" in  "banana"
# True

# lower()
"Banana".lower()
# banana

# lower()
"Banana".upper()
# BANANA

# Encontrar substring - find()
"banana".find("na")

# Reemplazar cadenas de string - replace()
"banana".replace("na", "ma")

# Borras espacios 
lstrip()  # Borra espacios del ppio
rstrip()  # Borra espacios del final
strip()   # Borra espacios de ambos

# Prefijos - startswith()
"banana".startswith("na")
# False

# Archivos
## Abrir archivos
handle = open(filename, mode)

modes => 
    r => lectura
    w => escritura

## nueva linea \n

##Lectura  - read() 
handle = open(filename, mode)
inp = handle.read()

# Arrays/Listas
lista = ["uno", "dos", "tres"]

## Longitud - len(lista)
# len - Cantidad de caracteres
cant = len(lista)

# slicing - Es para substrings
s = [1,2,3]
print(s[0:1])
# [1,2]

# concatenacion
s = [1,2,3]
t = [4,5,6]
p = s + t
# [1,2,3,4,5,6]

# Metodos de lista
stuff = list() # Crear lista
stuff.append("book") #Agrega un elemento
"book" in stuff #Se fija si esta el elemento en la lista
"book" not in stuff #Se fija si no esta el elemento en la lista
stuff.sort() # Ordena la lista
sum(stuff) # Suma los elementos de una lista de numeros
max(stuff) # Busca el maximo de una lista de numeros
min(stuff) # Busca el maximo de una lista de numeros
"Lucio Altamirano lalt123@gmail.com".split() # Separa el string por los espacios
"Lucio Altamirano lalt123@gmail.com".split('@') # Separa el string tomando como referencia el @

# Metodos de la lista
['append', 'count', 'extend', 'index', 'insert',
'pop', 'remove', 'reverse', 'sort']
# Arrays asociativos / Diccionarios
purse = dict()
purse["money"] = 12
conunts = dict()
x = counts.get(name, 0) # Cantidad de veces que aparece en el dict. Si fuese otro valor seria un elemento que tenga es valor.

#  tuplas
## creacion
t = tuple()
(x,y) = (4, "fred")

d = dict()
tups = d.items()
# resultado = lista de tuplas

# Sorted
d = {'a': 10, 'b' : 1, 'c' : 22}
t = sorted(d.items())