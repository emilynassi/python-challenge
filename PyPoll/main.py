import os
import csv
electiondata1= os.path.join("election_data_1.csv")

#set votes to 0
votes = 0

#Read the csv
with open(electiondata1) as csvfile:
    csvreader = csv.reader(csvfile)

    #loop through rows
    for row in csvreader:

        votes += 1



print(votes)
