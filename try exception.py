'''
Try - exception demonstration
'''

a = int(input("Enter a value"))
b = int(input("Enter second value"))

try:
    c = a / b
    print (c)
except ZeroDivisionError:
    print ("enter value other than '0' ")
