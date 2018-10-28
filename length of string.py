'''
to find the length of a given string
'''

a = raw_input("Enter a string: ")

count = 0

for char in a:
    count += 1

print("The length of the entered string is:", count)
