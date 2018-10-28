'''
Program To Read Three Numbers And Print
The Biggest Of Given Three Numbers.
'''

a = raw_input("ENTER VALUE FOR A: ")
b = raw_input("ENTER VALUE FOR B: ")
c = raw_input("ENTER VALUE FOR C: ")

if a > b and a > c:
    print "A is greater"

elif b > c:
    print "B is greater"

else:
    print "C is greater"
