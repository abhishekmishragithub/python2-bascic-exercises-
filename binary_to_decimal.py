# Method-1
binary = raw_input('enter a number: ')
decimal=int(binary, 2)
print(decimal)

# Method-2

binary = raw_input('enter a number: ')
decimal = 0
for digit in binary:
    decimal = decimal*2 + int(digit)
print decimal
