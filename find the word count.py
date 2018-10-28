'''
Program to find the total number of times a particular word has repeated
'''

a = 0
with open("C:/Users/Jeri_Dabba/Desktop/test.txt", "r") as m:
    for i in m:
        if "Bari" in i:
            print("true")
            a += 1
print(a)
