"""
Variables, comments, and string formatting in Python
"""

# Creating a variable and assigning a value to it
number = 10

print(number)

money = 50
cost = 15
tax = 0.03
total_cost = cost + (cost * tax)

print(money-total_cost)

print(f"Remaining money after purchase: {money - total_cost}")

sentence = "I had {} dollars, I bought an item for {} dollars (including tax of {}), and now I have {} dollars left."
print(sentence.format(money, cost, cost * tax, money - total_cost))
