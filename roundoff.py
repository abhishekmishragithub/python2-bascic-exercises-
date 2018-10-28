'''
Round-off to the nearest integer
'''

a = float(raw_input("Enter a value to check "))
b = int(a)
#print(a,",", b)

if a - b < 0.5:
    print("The value after round-off is: ", b)
else:
    print("The value after round-off is: ", b + 1)
