# Import OS Module
import os

# Module for reading CSV files
import csv

csvpath = os.path.join('Resources','budget_data.csv')

#Lists to store data 
date = []
profit_losses = []

# Reading CSV
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile)

    csvheader=next(csvreader)
    for row in csvreader:
        # Add date
        date.append(row[0])

        # Add Profit_losses
        profit_losses.append(int(row[1]))

# The total number of months included in the dataset
print("Financial Analysis")
print('------------------')
total_months = len(date)
print(f'Total Months: {total_months}')

# The net total amount of "Profit/Losses" over the entire period
print(f'Total: ${sum(profit_losses)}')
# The changes in "Profit/Losses" over the entire period, and then the average of those changes
change_in_profit = [0] 
for i in range(len(profit_losses)-1):
    change = profit_losses[i+1] - profit_losses[i]
    change_in_profit.append(change)

average_change = round(sum(change_in_profit) / (len(change_in_profit) - 1),2)
print(f'Average change: ${average_change}')

# The greatest increase in profits (date and amount) over the entire period
# change_in_profit = [0]
greatest = list(zip(change_in_profit,date))
greatest_increase = max(greatest)
print(f'Greatest Increase in Profits: {greatest_increase[1]} (${greatest_increase[0]})')
# The greatest decrease in profits (date and amount) over the entire period
greatest_decrease = min(greatest)
print(f'Greatest decrease in Profits: {greatest_decrease[1]} (${greatest_decrease[0]})')

# Specify the file to write to
output_path = os.path.join("Analysis", "main.txt")

# Open the file using "write" mode. Specify the variable to hold the contents
with open(output_path, 'w') as txtfile:

# create txt file
    txtfile.write("Financial Analysis\n")
    txtfile.write('------------------\n')
    txtfile.write(f'Total Months: {total_months}\n')
    txtfile.write(f'Total: ${sum(profit_losses)}\n')
    txtfile.write(f'Average change: ${average_change}\n')
    txtfile.write(f'Greatest Increase in Profits: {greatest_increase[1]} (${greatest_increase[0]})\n')
    txtfile.write(f'Greatest decrease in Profits: {greatest_decrease[1]} (${greatest_decrease[0]})\n')