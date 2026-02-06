# ---------------> VARIABLES
my_string: str = 'My String Variable'
print(my_string)

my_int: int = 5
print(my_int)

my_bool: bool = True
print(my_bool)
print('----------------------------------------------------------------')

# ---------------> VARIABLES EN UNA SOLA LINEA
name, surname, alias, age = 'Felipe', 'Agudelo', 'Dresk76', 30
print(f'Me llamo: {name} {surname}, mi alias es: {alias} y mi edad es: {age}')
print('----------------------------------------------------------------')

# ---------------> INPUTS
'''
Pedir la edad y la altura del usuario desde consola 
y almacenarlas con el tipo de dato correcto.
'''

edad = int(input('Ingresa tu edad: '))
altura = float(input('Ingresa tu altura: '))

print(f'Tu edad es: {edad} y tu altura es: {altura}')
print('--------------------------------------------')

'''
Capturar nombre, edad y correo del usuario y 
mostrarlos en pantalla..
'''

usuario = {
    'nombre': input('Ingresa tu nombre: '),
    'edad': input('Ingresa tu edad: '),
    'correo': input('Ingresa tu correo: ')
}

print(f"Hola {usuario['nombre']}, veo que tienes {usuario['edad']} años y que tu correo es {usuario['correo']}. Bienvenido!")
print('--------------------------------------------')

# ---------------> ALGUNAS FUNCIONES DEL SISTEMA
# len: Cuenta los caracteres
print(len(my_string))
print(len(str(my_int)))
print('----------------------------------------------------------------')


# ---------------------------- EXERCISES

'''
1. Declara y asigna valores a las siguientes variables:
    name: una cadena que contenga tu nombre.
    age: un número entero que represente tu edad.
    height: un número flotante que represente tu altura.
Imprime cada variable en una línea separada.
'''
name: str = 'Felipe'
age: int = 30
height: float = 1.77

print(f'Mi nombre es: {name}.')
print(f'Mi edad es: {age} años.')
print(f'Mi altura es: {height} cm.')
print('----------------------------------------------------------------')

'''
2. Convierte la variable edad de entero a cadena y 
concatenala con un texto que diga cuántos años tienes.
'''
age = '30'
print(f'Actualmente tengo {age} años.')
print(f'El tipo de age ahora es: {type(age)}')  # str
print('----------------------------------------------------------------')

'''
3. Declara una variable booleana is_student que indique si 
eres estudiante o no. Usa True o False según corresponda 
e imprímela.
'''
is_student : bool = True
print(f'Actualmente se dice que soy un estudiante de Python?: {is_student}')
print('----------------------------------------------------------------')

'''
4. Usa la función len() para calcular cuántos caracteres 
tiene tu nombre completo, almacenado en una variable.
'''
full_name : str = 'Felipe Agudelo'
print(f'Mi nombre completo tiene {len(full_name)} carácteres')
print('----------------------------------------------------------------')

'''
5. Declara tres variables en una sola línea que representen 
tu nombre, apellido y ciudad de origen. Luego, imprime 
estos valores.
'''
name, surname, city = 'Felipe', 'Agudelo', 'Manizales'
print(f'Mi datos básicos solicitados son: \n- Nombre completo: {name} {surname} \n- Ciudad de nacimiento: {city}')
print('----------------------------------------------------------------')

'''
6. Usa la función input() para solicitar al usuario su 
color favorito y almacénalo en una variable color. 
Luego, imprime el valor ingresado.
'''
color = str(input('Ingrese su color favorito: '))
print(f'También me gusta el color {color}, que buena elección.')
print('----------------------------------------------------------------')

'''
7. Declara una variable fruit e inicialízala con un valor. 
Luego, cambia el valor de la fruta a otro diferente y 
vuelve a imprimirla.
'''
fruit : str = 'Lulo'
print(f'Mi fruta preferida es el {fruit}.')

fruit = 'Maracuya'
print(f'No, ya lo pense bien y mi fruta preferida es el {fruit}')
print('----------------------------------------------------------------')

'''
8. Convierte un número decimal, almacenado en la variable 
price, a un número entero y luego imprímelo.
'''
price : float = 3.14

print(f'Asi se imprime solo la parte entera de price {(int(price))}, \naunque sea de tipo: {type(price)}')
print('----------------------------------------------------------------')

'''
9. Declara una variable llamada address_len y almacena en 
ella la cantidad de caracteres de una dirección usando 
la función len(). Imprime el resultado.
'''
address : str = 'CRA 25 # 66 - 51'
address_len : int = len(address)
print(f'Mi dirección es {address}, y tiene {address_len} carácteres.')
print('----------------------------------------------------------------')

'''
10. Usa un tipo de dato forzado para declarar una 
variable phone, asegurándote de que siempre será un 
número. Luego, cambia su valor a un número diferente y 
verifica el tipo de la variable con type().
'''
phone : int = 3134912612
print(f'El tipo de dato de la variable phone es: {type(phone)}.')

phone = 3025970362
print(f'El tipo de dato de la variable phone ahora es: {type(phone)}.')
print('----------------------------------------------------------------')