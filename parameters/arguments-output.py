 
import sys

arguments = len(sys.argv) - 1
position = 1
print('el script ha sido llamado con los parametros en el siguiente orden: ')
while (arguments >= position):
    print('parametro %i: %s' %(position, sys.argv[position]))
    position = position + 1
    