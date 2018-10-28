'''
Program to accept a number and print mathematical table of the given no.
'''

val = int(raw_input("Enter a value to find the mathemetical table: "))

for i in range(1, 16):
    print "%s X %s = %s" % (i, val, i*val)
