my_list = [1, 2, 3, 4, 5]

for item in my_list:
    print("Current item:", item)

for item in range(2, 4):
    print("Current item:", item)


sum_of_items = 0
for x in my_list:
    sum_of_items += x
print("Sum of items:", sum_of_items)

test = ["test", "test2", "test3"]
for item in test:
    for char in item:
        print(char)
    else:
        print("Finished inner loop for item:", item)

i = 0
while i < 5:
    i += 1
    if i == 3:
        continue
    if i == 4:
        break
    print("Current i:", i)
else:
    print("i is no longer less than 5")
