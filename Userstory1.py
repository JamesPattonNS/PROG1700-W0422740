# Prog1700-Student15
"""
Hello World Project

First In Class Work

Name...: James, Patton
ID...: W0422740
"""
__AUTHOR__ = "James Patton <w0422740@nscc.ca>"

#CupCost
costOfCup = 1.25
hsttaxes = 0.15

#Part1
print("Hello.")
Cups = input("How many cups today: ")
numCups = int(Cups)
Cost = float(numCups * costOfCup)
Result = str(Cost)
print("That will be "+Result+" before taxes ")

#Part2
tax = float(Result * hsttaxes)


print("Your tax will be " +tax+"")