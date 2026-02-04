## 1. Intro

#### Course Content

- Python Refresher
- Project 1 - CRUD basically
- Project 2 - Classes, Error handling
- Project 3 - Database & ORM, JWT auth, Routing
- Project 3.5 - Databases and Data Migration (with Alembic)
- Project 4 - Unit & Integration Testing
- Project 5 - Full Stack Web App

## Python Refresher

- Linting: autopep8 extension

- Remember we use snake_case for naming

- Variables, comments, string formatting
  `- print(f"Remaining money after purchase: {money}")`

#### Lists

- Same as arrays in JS, some obs and methods:
  - `len(list_name)`
  - `list_name[-1]` gets last item (or [-X] will get last x item)
  - `list_name[0:2]` gets the slice from 0 up to 2 NOT included (and it does not mutate the list)
  - `list_name.append()`
  - `list_name.remove()` remove by value
  - `list_name.pop()` remove by index
  - `list_name.reverse()`
  - `list_name.sort()`

#### Sets and Tuples

- Sets:
  - `my_set = {1, 2, 3, 4, 5, 1, 2}`
    - 2nd 1 and 2 wil be removed, as sets does not support duplication
  - Methods
    - `my_set.discard(3)`
    - `my_set.add(6)`
    - `my_set.update([7,8])`

- Tuples
  - `my_tuple = (1, 2, 3, 4, 5)`
  - Same as lists, but does not change (so it does not accept methods such as append, remove etc)

#### Booleans and Operators

- Booleans
  - Capital Letters (`True` , `False`)

- Equality Operators:
  - `1 == 1`
  - `1 != 2`
  - `1 < 2`
  - `2 > 1`
  - `1 <= 2`
  - `2 >= 1`

- Logical Operators:
  - `and`, `or`, `not`
    - e.g.: `print(1 == 1 and name == 'Renan')`

#### if else

- if, elif, else
- Watch identation:

```python
  x = 1

  if x == 1:
      print("x is equal to 1")
      print("x is equal to 1")
  elif x == 2 or x == 3:
      print("x is equal to 2 or 3")
  else:
      print("x is neither 1 nor 2 or 3")
      print("x is neither 1 nor 2 or 3")
  print("This is out of the identation block")
```

#### Loops

- `for in`, `while`
- Reminder: strings are iterable;
- `continue`, `break`
- Loops also can have `else`s, e.g.:
  ```python
  test = ["test", "test2", "test3"]
  for item in test:
      for char in item:
          print(char)
      else:
          print("Finished inner loop for item:", item)
  ```

#### Dictionaries

- Closer to maps (in JS) - key, value pairs
- Iterable methods like array;
  - `for key, value in user_dictionary.items():`
- Also, they are reference types, e.g.:

  ```python
      dict1 = {a:1, b:2}
      dict2 = dict1
      dict2.pop"a"
      print(dict1) # {b:2}
  ```

- **Obs.:** Remember to use `.copy()` to copy the dict instead of pointing to the same when assigning a new dictionary

#### Functions

- In python, I can explicitly set the args used by name. e.g:

```python
  def custom_print_numbers(first_num, second_num):
    print(first_num, second_num)


  custom_print_numbers(4, 3)  #prints 4, 3
  custom_print_numbers(second_num=4, first_num=3) #prints 3, 4
```

- **Obs.:** In another example, it was shown that there is hoisting for functions in python

#### Imports

- We dont need to export from the original file
  - And we import everything - so it will be `imported_name.function()`
  - `import __39_2_grade_avg_service as grade_service`

- Python comes with some standard libraries, like `random`and `math`

#### OOP (I just started skimming everything)

- Showed about creaintg classes (very readable syntax)
  - **Obs.:** We use `self` to refer to the instanciated object
    - e.g.- class with constructor with args

    ```python
          class Person():
            def __init__(self, age=20, name="John"):
              self.age = age
              self.name = name
              self.__arms_qty = 2

            def talk(self):
              print(f"Hi, I am {self.name}, {self.age} years old")

          p1 = Person(30, "Alice")
          p1.talk()
    ```

    - Also we dont need the `__init__` when the constructor has no parameters

- 4 Pilars
  - Abstraction
    - "Hide implementation and only show whats is necessary" - Basically creating the class
  - Encapsulation
    - Make some properties private
      - Like the `self.__arms_qty = 2` in our example
      - **Important:** So we need to create getters and setters to handle the private data

  - Inheritance
  - Polimorphism

#### Obs during the course / tests:

- In python the fallback has the same idea as in TS: `(len(homework_grades) or 1)`
