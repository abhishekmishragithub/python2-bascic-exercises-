'''
To reverse a string without var[::-1]
'''

string = raw_input("Enter a value: ")

reversed_string = ''

for i in range(len(string)):
    reversed_string += string[len(string) - i - 1]

print(reversed_string)
