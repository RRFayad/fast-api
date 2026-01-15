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

"""
# Taking user input
first_name = input("Enter your first name: ")
print(f"Hello, {first_name}!")

days = int(input("How many days until your birthday?"))
print(f"Your birthday is in {round(days/7)} weeks!")
"""


# Lists in Python
my_list = [80, 96, 72, 100, 8]
print(my_list[-1])  # Accessing the last element of the list
my_list[0:2]
print(my_list)  # Accessing the last element of the list
print(my_list[0:2])  # Accessing the last element of the list
test = my_list[0:2]
print(test)

my_list.append(55)  # Adding an element to the end of the list
print(my_list)

my_list.remove(72)  # Removing an element from the list (looks for the value)
print(my_list)

my_list.sort()  # Sorting the list in ascending order
print(my_list)

my_list.reverse()  # Reversing the order of the list
print(my_list)
