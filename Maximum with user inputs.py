'''
Maximum number using user inputs
'''

def get_val(s):
    l = []
    for i in range(s):
        a = int(raw_input("Enter the {} value: ".format(i + 1)))
        # a = raw_input("Enter the %s value" % (i +1))
        l.append(a)
    return l

def maxi(ls = []):
    maxi = ls[0]
    for i in range(len(ls)):
        if ls[i] > maxi:
            maxi = ls[i]
    return maxi


print("The maximum value is {}".\
      format(maxi(get_val(int(raw_input("Enter the size of the list: "))))))
