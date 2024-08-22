from math import sqrt,floor,ceil
import math
"""def caux(n:int,m:int)->int:
    return n+m

print(caux(5,3))

a=4
b=2
print(a+b)
print(a<b)
abc='hoy es lunes'
print (abc[5]) #imprime s de 'es' puede imprimir ''
print(abc[4:8]) #imprime de posicion 4 hasta 8
my_list=["Python",True,5,(a,b)]
print (my_list)

def pertenece (l:list,e:int)->bool:
    i:int=0
    while i<len(l):
      if l[i]==e:
          return True
      i+=1
    return False"""
"""def mas_larga (l1,l2)->list:
    if len(l1)>=len(l2):
        return l1
    else:
        return l2
print(mas_larga([],[1,2,3]))"""



def mezclar(cadena1, cadena2) -> str:
    s = ""
    i = 0
    
    while i < len(cadena1) and i < len(cadena2): #Termino todas las letras de cada cadena
        s += cadena1[i]
        s += cadena2[i]
        i += 1
    
        
    s += cadena1[i:] #parte del string que va desde la posición i hasta el final"
    s += cadena2[i:]

    return s

# Ejemplos
"""print(mezclar("Pepe", "Josefina"))   #obs: no agrega nada en la linea 42 porque ya se termino el str Pepe, ejecuta en la l43
print(mezclar("Josefina", "Pepe"))"""  #Obs: Si ejecuta en la linea 42, y no hace nada en la l43

def mezclar2 (cadena1, cadena2) -> str:
    s = ""
    i = 0
    while i < len(cadena1) and i < len(cadena2):
           s += cadena1[i]
           s += cadena2[i]
           i += 1
           
    for i in range (i,len(cadena1)):
        s+=cadena1[i]
        
    for i in range (i,len(cadena2)):
        s+=cadena2[i]
        
    return s
"""print(mezclar2("Pepe", "Josefina"))   
print(mezclar2("Josefina", "Pepe"))"""
        
def pago_del_credito (años:int)->float:
    cantidad_de_meses:int= años*12
    pago_mensual:float=2684.11
    pago_final:float=pago_mensual*cantidad_de_meses
    return round(pago_final,2)
    
print(pago_del_credito(30))

def calcular_hipoteca_con_pagos_extra():
    saldo = 500000
    tasa_mensual = 0.05 / 12
    pago_fijo = 2684.11
    pago_extra = 1000
    total_pagado = 0
    meses = 0

    while saldo > 0:
        # Calcular interés mensual
        interes = saldo * tasa_mensual

        # Durante los primeros 12 meses, añadir pago extra
        if meses < 12:
            pago_total = pago_fijo + pago_extra
        else:
            pago_total = pago_fijo

        # Reducir saldo con el pago realizado
        saldo = saldo + interes - pago_total

        # Asegurarse de no pagar más del saldo pendiente
        if saldo < 0:
            pago_total += saldo  # Ajustar el último pago
            saldo = 0

        # Acumular el total pagado
        total_pagado += pago_total
        meses += 1

    return total_pagado, meses

# Llamar a la función e imprimir resultados
total_pagado, meses = calcular_hipoteca_con_pagos_extra()
print(f'Total pagado: ${total_pagado:.2f} en {meses} meses.')