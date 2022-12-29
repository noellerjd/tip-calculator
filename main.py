print("Welcome to the tip calculator.")
# Take in total amount of bill
total = float(input("What was the total bill? $"))
# What percentage of tip will we give
percentage_amount = int(input("What percentage would you like to give? 10, 12, or 15? "))
# How many people we will divide the bill by
split = int(input("How many people to split the bill? "))
# divide the total by the split
total_divided = round(total / split,2)
# convert into a percentage
percentage = percentage_amount / 100
# multiply the total by the tip percentage and split the tip
tip = round((total * percentage) / split,2)
# calculate total per person and format the 0 to show up at the end i.e. $36.50
each_total = "{:.2f}".format(total_divided + tip)
# Print total each person should pay with tip included
print(f"Each person should pay: ${each_total}")
