# en este caso compararemos dos objetos
# 

def compareObjects(a,b):

    if a is b:
        print('a es el mismo objeto que b, tiene el mismo id')
    if a == b:
        print('los valores de a y b son identicos')
    if type(a) is type(b):
        print('los objetos son del mismo tipo')

x = [1, 2, 3]
y = [1, 2, 3]

print(id(x))
print(id(y))

compareObjects(x,y)