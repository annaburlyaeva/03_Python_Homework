# Dependencies
import os
import csv

# Set path for file
csvpath = os.path.join("budget_data.csv")

# Define variables
months = ["first_element"]
profit_losses_total = 0
profit_losses = []
changes = []
changes_sum = 0
profits = []
losses = []
first_check = True

# Open the CSV
with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    header = next(csvreader)
    # Loop
    for row in csvreader:

        # Calculate the total amount for profit / losses
        profit_losses_total += int(row[1])

        # Calculate the average of the profit / losses changes
        if first_check == True:
            profit_losses.append(int(row[1]))
            first_check = False
        else: # Start calculating the average with the second value
            changes.append(int(row[1])-int(profit_losses[-1]))
            profit_losses.append(int(row[1]))
            changes_sum += int(changes[-1])
        
        # Calculate the total number of months
        if row[0] != months[-1]:
           months.append(row[0])
        else:
            pass

        # Calculate the greatest increase / decrease in profits / losses (date and amount)
        if int(row[1]) == max(profit_losses):
           max_profit_date = row[0]
        elif int(row[1]) == min(profit_losses):
            max_loss_date = row[0]
       
print("Financial Analysis")
print("----------------------------------------------")

months_total = len(months)-1
print("Total Months: " + str(months_total))

print("Total: $" + str(profit_losses_total))

avg_changes = changes_sum / len(changes)
print("Average  Change: $" + str(avg_changes))

print("Greatest Increase in Profits: " + str(max_profit_date) + " ($" + str(max(profit_losses)) + ")")

print("Greatest Decrease in Profits: " + str(max_loss_date) + " ($" + str(min(profit_losses)) + ")")

# Write the results into the file
output_path = os.path.join("financial_analysis_results.csv")
with open(output_path, 'w', newline='') as csvfile:

    csvwriter = csv.writer(csvfile, delimiter=',')

    # Write the rows
    csvwriter.writerow(["Financial Analysis"])
    csvwriter.writerow(["----------------------------------------------"])
    csvwriter.writerow(["Total Months: ", str(months_total)])
    csvwriter.writerow(["Total ($): ", str(profit_losses_total)])
    csvwriter.writerow(["Average  Change ($): ", str(avg_changes)])
    csvwriter.writerow(["Greatest Increase in Profits ($): ", str(max_profit_date), str(max(profit_losses))])
    csvwriter.writerow(["Greatest Decrease in Profits ($): ", str(max_loss_date), str(min(profit_losses))])