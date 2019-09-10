import os
import csv
csvpath = os.path.join('..', 'Resources', 'budget_data.csv')
with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvfile)
    total = 0
    for row in csvreader:
        row= total + row.total
        print(row)