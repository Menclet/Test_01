import  pandas
import numpy
a =[12, 14,24, 36]
b=[12, 14,24, 36]

for i in (0, len(a)):
    a[i] += b[i]

print(a)