
import sys

print('')
print('el nombre del script es: %s' %(sys.argv[0]))
if len(sys.argv) == 1:
    print('no me pasaste argumentos!!! \n'
        'vuelve a ejecutarme con argumentos!')
print('')
# el numero de argumentos es 'len(sys.argv)-1' porque el primero
# es el nombre del script, e.d. nombre_script = sys.argv[0]
numero_argumentos = len(sys.argv) - 1
print('el numero de argumentos que me pasaste es: %s' %(numero_argumentos))
print('')
print('el script ha sido llamado con los parametros en el siguiente orden: ')
posicion = 1
while (numero_argumentos >= posicion):
    print('parametro %i: %s' %(posicion, sys.argv[posicion]))
    posicion += 1
print('')
