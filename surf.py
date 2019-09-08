from sort import shakesort
import re
from sys import argv
script, filename = argv

def imprLst(li):
    for i in li:
        print(i,end=' ')
    print('\n')

def prPlaces(li, max):
    i = -1
    p = 1
    while(i >= max):
        print('Place No. {}'.format(p))
        print(li[i])
        i = i - 1
        p = p + 1
    print('\n')
# Para imprimir una lista bonita
#

with open(filename, 'r+') as file:
    contents = file.read()
lines = contents.split('\n')
# Extrae los contenidos del archivo txt y crea una lista
# con cada linea.
#li = [7,10,4,1,8,6,9,5,2,3]

exp = re.compile(r"^\D+")
# Crea una expresion regular para extraer unicamente 
# la puntuacion de cada linea

scor = []
for line in lines:
    l = line
    rm = exp.match(line)
    scor.append(int(l.strip(rm.group(0))))
#
#

shakesort(scor, lines,0, len(lines))
#
#
imprLst(lines)
prPlaces(lines, -3)
