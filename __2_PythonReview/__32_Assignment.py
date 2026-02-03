my_vehicle = {
    "model": "Ford",
    "make": "Explorer",
    "year": 2018,
    "mileage": 40000
}

for key, value in my_vehicle.items():
    print(key, value)


vehicle2 = my_vehicle.copy()

vehicle2["number_of_tires"] = 4

vehicle2.pop("mileage")

for key in vehicle2.items():
    print(key)


print("---------- FINAL RESULT -------------")
print("my_vehicle", my_vehicle)
print("vehicle2", vehicle2)
