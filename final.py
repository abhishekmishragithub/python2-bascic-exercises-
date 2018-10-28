import getpass
import warnings

warnings.filterwarnings("ignore")

details = {}
while True:
    a = input("User Name: ")
    #b = input("Enter the Password: ")
    b = getpass.getpass()
    details[a] = b
    #a = input("Do you wish to continue (y/n)")
    #if a.lower() == 'n':
    if (input("Do you wish to continue (y/n)")).lower() == 'n':
        break

with open('test.txt', 'w') as f:
    f.write(details)

print(details)
    
