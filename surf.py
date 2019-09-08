from sort import shakesort
import re
from sys import argv
script, filename = argv

def impr(li):
    for i in li:
        print(i,end=',')
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
    rm = exp.match(line)
    scor.append(int(line.strip(rm.group(0))))

impr(lines)
shakesort(scor, lines,0, len(lines))
impr(lines)
