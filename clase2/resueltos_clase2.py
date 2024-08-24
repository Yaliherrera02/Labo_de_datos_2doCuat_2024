import random
"""prueba=random.random()
print(prueba)"""

random.seed(34)
prueba=random.random()
print(prueba)

import math

# Ejemplo 1: Raíz cuadrada
raiz = math.sqrt(2)
print(f"La raíz cuadrada de 2 es {raiz}")

# Definimos x para los otros ejemplos
x = 3

# Ejemplo 2: Exponencial
exponencial = math.exp(x)
print(f"El valor de e elevado a {x} es {exponencial}")

# Ejemplo 3: Coseno
coseno = math.cos(x)
print(f"El coseno de {x} radianes es {coseno}")

# Ejemplo 4: MCD (Máximo Común Divisor)
mcd = math.gcd(15, 12)
print(f"El MCD de 15 y 12 es {mcd}")
