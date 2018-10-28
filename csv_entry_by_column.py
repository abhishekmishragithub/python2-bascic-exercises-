import csv
Col1 = "ColumnName1"
Col2 = "ColumnName2"
Col3 = "ColumnName3"
mydictionary={Col1:[], Col2:[], Col3:[]}
csvFile = csv.reader(open("myfile.csv", "rb"))
for row in csvFile:
  mydictionary[Col1].append(row[0])
  mydictionary[Col2].append(row[1])
  mydictionary[Col3].append(row[2])
