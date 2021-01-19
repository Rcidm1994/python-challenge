import os
import csv
import pandas as pd

csvpath = os.path.join('..','Resources','budget_data.csv')
output_path = os.path.join('..','Resources','results_pybank.csv')   

n = 0
t = 0
ch = 0

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile,delimiter=',')
    csvheader = next(csvreader)

    for row in csvreader:
        n = n + 1
        t = t + int(row[1])
        ch = int(row[1]) - ch
        newcsvfile = pd.DataFrame(csvfile)
        new_row = ch
        newcsvfile = newcsvfile.append(new_row,ignore_index=True)

a = ch/n

with open(output_path, 'w', newline='') as csvfile:

    csvwriter = csv.writer(csvfile,delimiter=' ')
    csvwriter.writerow([csvheader])
print("Financial Analysis")
print("------------------")
print(f"Total months: {n} ")
print(f"total: {t} ")
print(f"Average change: {a} ")