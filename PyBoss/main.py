import os
import csv
from datetime import datetime
employeedata= os.path.join("employee_data1.csv")

#Hold state abbreviation dictionary
us_state_abbrev = {
    'Alabama': 'AL',
    'Alaska': 'AK',
    'Arizona': 'AZ',
    'Arkansas': 'AR',
    'California': 'CA',
    'Colorado': 'CO',
    'Connecticut': 'CT',
    'Delaware': 'DE',
    'Florida': 'FL',
    'Georgia': 'GA',
    'Hawaii': 'HI',
    'Idaho': 'ID',
    'Illinois': 'IL',
    'Indiana': 'IN',
    'Iowa': 'IA',
    'Kansas': 'KS',
    'Kentucky': 'KY',
    'Louisiana': 'LA',
    'Maine': 'ME',
    'Maryland': 'MD',
    'Massachusetts': 'MA',
    'Michigan': 'MI',
    'Minnesota': 'MN',
    'Mississippi': 'MS',
    'Missouri': 'MO',
    'Montana': 'MT',
    'Nebraska': 'NE',
    'Nevada': 'NV',
    'New Hampshire': 'NH',
    'New Jersey': 'NJ',
    'New Mexico': 'NM',
    'New York': 'NY',
    'North Carolina': 'NC',
    'North Dakota': 'ND',
    'Ohio': 'OH',
    'Oklahoma': 'OK',
    'Oregon': 'OR',
    'Pennsylvania': 'PA',
    'Rhode Island': 'RI',
    'South Carolina': 'SC',
    'South Dakota': 'SD',
    'Tennessee': 'TN',
    'Texas': 'TX',
    'Utah': 'UT',
    'Vermont': 'VT',
    'Virginia': 'VA',
    'Washington': 'WA',
    'West Virginia': 'WV',
    'Wisconsin': 'WI',
    'Wyoming': 'WY',
}
emp_id = []
first_name =[]
last_name = []
dob = []
ssn = []
state =[]

#Read the csv
with open(employeedata) as csvfile:
    csvreader = csv.reader(csvfile)

    # skip header row
    next(csvreader)

    for row in csvreader:


        # Add employee id
        emp_id.append(row[0])

        # Split Names
        namesplit = row[1].split(" ")

        #Add names to new columns
        first_name.append(namesplit[0])
        last_name.append(namesplit[0])

        # rewrite DOB
        dob_old = datetime.strptime(row[2], "%Y-%m-%d")
        # Create new format
        dob_new = dob_old.strftime("%d-%m-%Y")
        # Add the formatted DOB into DOB list
        dob.append(dob_new)

        # rewrite SSN
        ssnsplit = row[3].split("-")
        ssn.append("***-**-" + ssnsplit[2])

        #add state abbreviation
        state.append(us_state_abbrev[row[4]])

#Zip new lists together
new_csv = zip(emp_id, first_name, last_name, dob, ssn, state)

# Set output file
output_file = os.path.join("employee_final.csv")

#  Open the output file
with open(output_file, "w", newline="") as datafile:
    writer = csv.writer(datafile)

    # Write the header row
    writer.writerow(["EmpID","First Name","Last Name","DOB","SSN","State"])

    # Write in zipped rows
    writer.writerows(new_csv)