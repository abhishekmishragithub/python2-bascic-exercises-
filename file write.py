'''
Write data to file
'''

with open("C:/Users/Jeri_Dabba/Desktop/new.txt", 'a') as file:
    a = raw_input("Enter some text: ")
    file.write('\n' + a)
