# ver los apuntes al final
def addTowNum(a, b):
    sum = a + b
    return sum

result = addTowNum(3,4)
print(type(result))

print('sum of numbers is %i' %(result)) 
# si en vez de %i usamos %s funciona igual, por que?
print('sum of numbers is %s' %(result)) 

# probemos hacer el print con diferentes variables
a = 1
b = 1.2
c = 'Que cosa?'
print('imprimiendo variables %i' %(c))
print('imprimiendo variables %s' %(c))
print('imprimiendo variables %f' %(c))

# con a entero el resultado es:
# imprimiendo variables 1
# imprimiendo variables 1
# imprimiendo variables 1.000000

# con b decimal el resultado es:
# imprimiendo variables 1
# imprimiendo variables 1.2
# imprimiendo variables 1.200000

# con c string el resultado es:
# Traceback (most recent call last):
#   File "function-return-type.py", line 17, in <module>
#     print('imprimiendo variables %i' %(c))
# TypeError: %d format: a number is required, not str

# por lo tanto podemos decir que %() aplica un type casting