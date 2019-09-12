import os
import csv
csvpath = os.path.join('..', 'Bootcamp', 'election_data.csv')
total_votes = 0
candidates = []  #catch all candidates name in it as list
votes = []        #catch all votes as list
percent_votes = [] 

with open(csvpath, newline='') as csvfile:
   csvreader = csv.reader(csvfile, delimiter=",")
   csv_reader = next(csvreader)             #Skipping the header in csvfile
   for row in csvreader:                    #iterating through csv columns
        total_votes = total_votes + 1       #counting total votes
        if row[2] not in candidates:        #It will put any new candidat name in the list "candidates" and also put index of it to index 
            candidates.append(row[2])   
            index = candidates.index(row[2])
            votes.append(1)                  #voting list will keep appending everytime there is a new candidate
        else:
            index = candidates.index(row[2]) #Voting list will get data for candiates already in the list and their index as well. 
            votes[index] += 1
for vote in votes:                            #interating through the list "Votes" which carries number of votes for candidates. 
    percentage = (vote/total_votes) * 100     #getting percentage, rounding it to 3 decimal point and appending it
    percentage = round(percentage)
    percentage = "%.3f%%" % percentage
    percent_votes.append(percentage)

winner = max(votes)                            #check the max votes and assign it to "winners"
index = votes.index(winner)                     #checking the index for same "winner" by giving the argument in index function. 
winning_candidate = candidates[index]           #passing the index to candidate name list will return the name of that candiate got max votes. 

#printing out required output in certain format
print("Election Results" + '\n')
print("-------------------------" + '\n')
print(f"Total Votes : {total_votes}")
print("-------------------------" + '\n')
for i in range(len(candidates)):
    print(f"{candidates[i]}: {str(percent_votes[i])} ({str(votes[i])})")
print("--------------------------")
print(f"Winner: {winning_candidate}")
print("--------------------------")

#Writing into the text file named, "output.txt"
output = open("output.txt", "w")
line1 = "Election Results"
line2 = "--------------------------"
line3 = str(f"Total Votes: {str(total_votes)}")
line4 = str("--------------------------")
output.write('{}\n{}\n{}\n{}\n'.format(line1, line2, line3, line4))
for i in range(len(candidates)):
    line = str(f"{candidates[i]}: {str(percent_votes[i])} ({str(votes[i])})")
    output.write('{}\n'.format(line))
line5 = "--------------------------"
line6 = str(f"Winner: {winning_candidate}")
line7 = "--------------------------"
output.write('{}\n{}\n{}\n'.format(line5, line6, line7))