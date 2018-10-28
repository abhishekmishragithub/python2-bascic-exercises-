string=raw_input("Enter Strings \n")
strings=string.split()
def removeDuplicate(strings):
    result = []
    for item in strings:
        if item not in result:
            result.append(item)
    return result
print("raw string is :")
print(string)
print ("after operation string is")
final=' '.join(removeDuplicate(strings))
print(final)

#main basic logic for single word-->
'''
string="Bill kills here but Bill here NOT HERE BILL not BILL"
strings=str(raw_input("enter  the string"))
result = []
for item in strings:
    if item not in result:
        result.append(item)
print(''.join(result))

'''
