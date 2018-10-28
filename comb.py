import itertools
lst = ['k','m','o','e','y']
for L in xrange(1, len(lst)+1):
                        comb = []
                        esl = [list(x) for x in itertools.combinations(lst,2)]
                        comb.append(esl)
print(comb)
