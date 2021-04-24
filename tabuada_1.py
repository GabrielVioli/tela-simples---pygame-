import math

def ShowLine():
    return print(30*"-")

def multiCa(a, b):
    return a * b

ShowLine()

b = float(input('numero: '))
a = 0
for a in range(0,11):
    m = multiCa(a,b)
    print(f'{math.trunc(b)} x {math.trunc(a)} = {math.trunc(m)}')

ShowLine()

