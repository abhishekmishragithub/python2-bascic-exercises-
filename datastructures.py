'''
@auhor ==> Abhishek
'''

seq = [0, 1, 2]
def sum(seq):
    def add(x,y): return x+y
    return reduce(add, seq)
print sum(seq)
