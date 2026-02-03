user_dictionary = {
    "name": "alice",
    "age": 30,
    "city": "New York"
}

print(user_dictionary.get("name"))
print(user_dictionary["name"])

user_dictionary["married"] = True
print(user_dictionary)
print(len(user_dictionary))

user_dictionary.pop("age")
print(user_dictionary)

user_dictionary.clear()
print(user_dictionary)

for key, value in user_dictionary.items():
    print(f"{key}: {value}")

user_dictionary2 = user_dictionary
user_dictionary2.pop("age", None)
print(user_dictionary)

# Age has been removed for dictionay 1, as both variables point to the same dictionary in memory

del user_dictionary
# print(user_dictionary) - Returns an error, as its deleted
