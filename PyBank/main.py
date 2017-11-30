import os
import csv

budgetdata1= os.path.join("budget_data_1.csv")
budgetdata2 = os.path.join("budget_data_2.csv")

# Read the csv
with open(budgetdata1) as csvfile:
    csvreader = csv.reader(csvfile)

    # use of next to skip first title row in csv file
    next(csvreader) 
    #create empty lists to store values
    revenue = []
    date = []
    revenue_change = []

    # append values to empty lists and then calculate sum of total revenue and amount of months and store as variables
    for row in csvreader:

        revenue.append(int(row[1]))
        date.append(row[0])
        #add together entire revenue list
        total_revenue = sum(revenue)
        #count length of date list
        total_months = len(date)

    #Loop through revenue column 
    for values in range(1,len(revenue)):
        
        #append changes in values to list
        revenue_change.append(revenue[values] - revenue[values-1])   
       
        #calculate average change though sum of the entire list divided by length of list 
        average_change = sum(revenue_change)/len(revenue_change)
        
        #find max in revenue_change list and store as variable
        max_change = max(revenue_change)
        #find min in revenue_change list and store as variable
        min_change = min(revenue_change)

        #store corresponding dates using index function
        max_date = date[revenue_change.index(max_change)]
        min_date = date[revenue_change.index(min_change)]

#print to terminal

    print("Financial Analysis")
    print("-----------------------------------")
    print("Total Months:",str(total_months))
    print("Total Revenue: $",str(total_revenue))
    print("Average Revenue Change: $", round(average_change))
    print("Greatest Increase in Revenue:", str(max_date),"($", max_change,")")
    print("Greatest Decrease in Revenue:", str(min_date),"($", min_change,")")


#print to text file
with open("Output.txt", "w") as text_file:
    
    print("Financial Analysis", file=text_file)
    print("-----------------------------------", file=text_file)
    print("Total Months:",str(total_months), file=text_file)
    print("Total Revenue: $",str(total_revenue), file=text_file)
    print("Average Revenue Change: $", round(average_change), file=text_file)
    print("Greatest Increase in Revenue:", str(max_date),"($", max_change,")", file=text_file)
    print("Greatest Decrease in Revenue:", str(min_date),"($", min_change,")", file=text_file)
    
