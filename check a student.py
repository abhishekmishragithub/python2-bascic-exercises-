'''
@auhor ==> Abhishek

Program to check whether a student to the particular class

'''

TEIT = ['abhi', 'mandar', 'joshi', 'nair']
SEIT = ['sushant', 'kiran', 'mishra', 'sanket']

name = input("Enter the student name: ")

if name in TEIT:
    print("You are a student of TEIT")

elif name in SEIT:
    print("You are a student of SEIT")

else:
    print("Sorry you dont belong to TEIT or SEIT")

