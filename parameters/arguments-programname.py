import sys

print('el nombre del script es: %s' %(sys.argv[0]))

if len(sys.argv) > 1:
    print('el parametro que me pasaste es: %s' %(sys.argv[1]))
else:
    print('no me pasaste argumentos!!!')