import sys, os, time

# Se armar una url con el nombre del servicio jenkins que nos dan

print('******************** Fix Build Number ********************')
nombre_artefacto = input('Entre el  nombre del artefacto \n'
                        'Debe ser similar a este: DMT-OSB12-IFS_consultaNumerosAmigos-TP_MDW_BUS_APL \n'
                        'Nombre de artefacto: ')
testing_area = input('Indique si el error fue en TESTING(1) o TESTING_B(2) \n'
            'Entre 1 o 2 para proceder: ')

if testing_area == '1':
    tst = ''
else:
    tst = '_B'

# url

url = 'https://jenkins.personal.corp/view/' + nombre_artefacto + '/job/RA_' + nombre_artefacto + '_DEPLOY_TESTING' + tst + '/configure'

print(url)