'''
To find maximum number
'''

from random import randint

a = []

for i in range(10):
    val = randint(0, 10)
    a.append(val)

g = a[0]

for i in range(len(a)):
    if a[i] > g:
        g = a[i]

print (a)
print (g)
