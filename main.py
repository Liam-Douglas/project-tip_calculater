#if the bill was $150.00, split between 5 people, with 12% tip.

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#write code below

x = float(input("What was the Bill? "))
y = int(input("fHow many people were there? "))
z = float(input("what is the tip perctange? "))

tip = (x / y) * z

print (float(tip))