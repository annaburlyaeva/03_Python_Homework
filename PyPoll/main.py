# Dependencies
import os
import csv

# Set path for file
csvpath = os.path.join("election_data.csv")

# Define variables
voters = []
votes_total = 0
candidates = {}
candidates_rating = {}

# Open the CSV
with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvreader)
    
    # Loop 
    for row in csvreader:

        # Calculate the total amount of votes
        voters.append(row[0])

        # Calculate the rating of candidates
        candidates[row[2]] = candidates[row[2]]+1 if row[2] in candidates else 1

# Get the set of unique element of the list
voters = set(voters)

for k, v in candidates.items():
    candidates_rating[k] = [v / len(voters) * 100, v]
        
winner = max(candidates, key=candidates.get)

print("Election Results")
print("------------------------------------------")

votes_total = len(voters)
print("Total Votes: " + str(votes_total))

print("------------------------------------------")

for cand, val in candidates_rating.items():
  print(cand, ': ', format(val[0], '.3f'), "% (", val[1], ")")

print("------------------------------------------")

print("Winner: ", str(winner)) 

output_path = os.path.join("election_results.csv")
with open(output_path, 'w', newline='') as csvfile:

    csvwriter = csv.writer(csvfile, delimiter=',')

    # Write the rows
    csvwriter.writerow(["Election Results"])
    csvwriter.writerow(["------------------------------------------"])
    csvwriter.writerow(["Total Votes: ", str(votes_total)])
    csvwriter.writerow(["------------------------------------------"])
    for cand, val in candidates_rating.items():
        csvwriter.writerow([str(cand) + ': ', str(format(val[0], '.3f')), "%" , str(val[1])])
    csvwriter.writerow(["------------------------------------------"])
    csvwriter.writerow(["Winner: ", str(winner)])

