# Import OS Module
import os

# Module for reading CSV files
import csv

csvpath = os.path.join('Resources','election_data.csv')

# Lists to store data and to create dictionary
ballot_num = 0
candidate = {}

# Reading CSV
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile)

    csvheader=next(csvreader)
    for row in csvreader:
        # Add total ballot id rows
        ballot_num += 1

        # Count candidates
        if row[2] not in candidate:
            candidate[row[2]] = 1
        else:
            candidate[row[2]] += 1

# The total number of votes cast
print("Election Results")

print('------------------')

# total_votes = len(ballot_id)
print(f'Total votes: {ballot_num}')
print('------------------')

# Specify the file to write to
output_path = os.path.join("Analysis", "main.txt")

# Open the file using "write" mode. Specify the variable to hold the contents
with open(output_path, 'w') as txtfile:

    txtfile.write("Election Results\n")
    txtfile.write('------------------\n')
    txtfile.write(f'Total votes: {ballot_num}\n')
    txtfile.write('------------------\n')

    # Complete list of candidates, total number of votes won and percetnage of votes
    winner=""
    percentage_of_votes = 0
    max_so_far = 0
    for name,count in candidate.items():
        if count > max_so_far:
            winner = name
            max_so_far = count

        print(f'{name}: {round(count/ballot_num*100,3)}% ({count})')
        txtfile.write(f'{name}: {round(count/ballot_num*100,3)}% ({count})\n')

    # The winner of the election based on popular vote
    print('------------------')
    txtfile.write('------------------\n')
    print(f'Winner: {winner}')
    txtfile.write(f'Winner: {winner}\n')
    print('------------------')
    txtfile.write('------------------\n')