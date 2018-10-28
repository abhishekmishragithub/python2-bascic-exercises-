'''
Round-off for negative and positive values
'''

def neg(a):
    a = a * (-1)
    b = int(a)
    if a - b >= 0.5:
        print("The rounded off value is: ", (b + 1) * (-1))
    else:
        print("The rounded off value is: ", b * -1)

def pos(a):
    b = int(a)

    if a - b >= 0.5:
        print("The rounded off value is: ", b + 1)
    else:
        print("The rounded off value is: ", b)
    
a = float(input("enter the 1st value: "))

if a < 0:
    neg(a)
else :
    pos(a)
