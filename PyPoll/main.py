#import modules
import os
import csv
electiondata1= os.path.join("election_data_1.csv")


#Read the csv
with open(electiondata1) as csvfile:
    csvreader = csv.DictReader(csvfile)

    #candidate counter
    current_row = 0

    #vote counter
    total_votes = 0

    #list to hold all appearances of candidates names
    candidates = []

    for row in csvreader:

        #skip header row
        current_row += 0


        if current_row == 1:
            continue

        #turn candidate column of csv into list
        candidates.append(row["Candidate"])

        #calculate total votes
        total_votes += 1

#Count total votes of each candidate and create new list
votes = [[x,candidates.count(x)] for x in set(candidates)]

#turn votes into dictionary
dict_votes = dict(votes)


#Print output to terminal
print("Election Results")
print("-----------------------------")
#print total votes
print ("Total Votes: " + str(total_votes))
print("-----------------------------")
#Format dictionary for printing candidate names, vote percentage and total votes for reach
for key, value in dict_votes.items():
    percentage = ((value / total_votes) * 100)
    print(key + ":",  format(percentage, '.2f')+ "%", "("+ str(value) +")")

print("-----------------------------")
#print winner
winner = [(value, key) for key, value in dict_votes.items()]
print ("Winner: "+ str(max(winner)[1]))

#print output to text file
with open("Output.txt", "w") as f:

    f.write("Election Results\n")
    f.write("-----------------------------\n")
    # print total votes
    f.write("Total Votes: " + str(total_votes)+"\n")
    f.write("-----------------------------\n")
    # Format dictionary for printing candidate names, vote percentage and total votes for reach
    for key, value in dict_votes.items():
        percentage = ((value / total_votes) * 100)
        candidates_votes = (key + ":", format(percentage, '.2f') + "%", "(" + str(value) + ")")
        f.write(str(candidates_votes)+"\n")

    f.write("-----------------------------\n")
    # print winner
    winner = [(value, key) for key, value in dict_votes.items()]
    f.write("Winner: " + str(max(winner)[1])+"\n")