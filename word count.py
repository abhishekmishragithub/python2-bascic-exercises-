'''
To count the total number of time each word has occured
'''

with open("test.txt", 'r') as f:
    wordcount={}
    for word in f.read().split():
        if word.lower() not in wordcount:
            wordcount[word.lower()] = 1
        else:
            wordcount[word.lower()] += 1
    for k,v in wordcount.items():
        print k, v
