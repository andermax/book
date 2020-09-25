import csv
branch = 'EU'
chose = input("chose branch 1.- Bank or 2. Europe, or input 'q' for exit: ")
counter = 0
filename = 'output/report2.csv'
print('|| *N* || *ID* || *Name* || *Card* || *Issue* || *Access Group* || *Department* ||')
with open(filename, "r", newline="") as file:
    reader = csv.reader(file)

    for row in reader:
     if branch in row[6]:
         counter += 1
         print('|',counter,'|', row[0], '|', row[1], '|', row[2], '|', row[3],'|', row[4],'|', row[5], '|', row[6])


