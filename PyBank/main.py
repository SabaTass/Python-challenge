import os
import csv
csvpath = os.path.join('..', 'budget_data.csv')
months = 0
total = 0
avg_stack = []
dates = []
prev_row_element =0

with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    #Skipping Header
    csv_reader = next(csvreader)

    for row in csvreader:
    #iterating to get total months and The net total amount of "Profit/Losses" over the entire period
        months = months + 1
        total = total + int(row[1])
        
    #calculating average by collecting values in list variable
        
        diff = int(row[1])-prev_row_element
        prev_row_element = int(row[1])  
        avg_stack = avg_stack + [diff] 
        #keeping track of dates
        dates.append(row[0])
# Calculating the Greatest Increase in Profits
greatest_profit = max(avg_stack)
greatest_index = avg_stack.index(greatest_profit)
greatest_date = dates[greatest_index]

#Calculating the Greatest Decrease in Profits
lowest_profit = min(avg_stack)
lowest_index = avg_stack.index(lowest_profit)
lowest_date = dates[lowest_index]


avgPL = sum(avg_stack[1:]) / (len(avg_stack) - 1)  #[1:] is basicaly skipping that first index value in the list
avg_final = round(avgPL, 2)                        #rounding to 2 decimal points. 

#OUTPUT 
print(f"\nFinancial Analysis\n")
print (f"----------------------------\n")
print (f"Total Months: {months}")
print (f"Total: $ {total}")
print (f"Average  Change:  {avg_final}") 
print (f"Greatest Increase in Profits : {greatest_date}, (${greatest_profit})")
print (f"Greatest Decrease in Profits : {lowest_date}, (${lowest_profit})")