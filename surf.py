from sort import shakesort
from sys import argv
script, filename = argv

with open(filename, 'r+') as file:
    contents = file.read()

lines = contents.split('\n')
li = [7,10,4,1,8,6,9,5,2,3]

print(li)
shakesort(li, 0, len(li))
print(li)
