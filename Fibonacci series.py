'''
@auhor ==> Abhishek

Program to print Fibonacci series
'''

a, b, c = 0, 1, 0

for i in range(1, 10):
    c = a + b
    print c,
    a, b = b, c
