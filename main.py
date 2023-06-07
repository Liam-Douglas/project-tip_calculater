#if the bill was $150.00, split between 5 people, with 12% tip.

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#write code below
bill = float(input("What was the total Bill? "))
people = int(input("How many people were there? "))
tip = int(input("what is the tip perctange? "))

# Calculate tip as percentage
tip_as_percent = tip / 100
# Calculate total tip amount
total_tip_amount = bill * tip_as_percent
# Calculate the total bill from the bill and tip amount
total_bill = bill + total_tip_amount
# Calculate bill amount per person
bill_per_person = total_bill / people
# the Final amount then rounded by 2 digits
final_amount = round(bill_per_person, 2)

print (f"Everyone should pay ${final_amount}")