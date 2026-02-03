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
