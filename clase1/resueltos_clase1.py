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
    
    while i < len(cadena1) and i < len(cadena2):
        s += cadena1[i]
        s += cadena2[i]
        i += 1
    
        
    s += cadena1[i:]
    s += cadena2[i:]

    return s

# Ejemplos
print(mezclar("Pepe", "Jose"))    # Salida: "PJeopsee"
print(mezclar("Pepe", "Josefa"))  # Salida: "PJeopseefa"


mezclar("acdfghi","be")