## Bookstore Proj

- Now we going to create a more compelte API, including:
  - CRUD
  - Data Validation, Exception Handling, Status Codes, Swagger Config, Python Req Objects

### Pydanticts & Data Valdiation

- Pydantics is for: Data Validation, data modeling, data aprsing, error handling

- So the logic is:
  - Create Pydantic Request Model (like Zod probably, whic could be translated to the Books class);
  - Field data validation on each variable;
  - Convert the Pydantic object into the Book, after validation

### Notes / Obs during course:

- use of `**` in Python:
  - It is used for packing and unpacking kwargs

  ```python

    def intro(name, age):
    print(f"My name is {name} and I am {age} years old.")

      details = {"name": "Alice", "age": 30}

      # Unpacks the dictionary into name="Alice", age=30
      intro(**details)
      # Output: My name is Alice and I am 30 years old.


  ```

- **Obs.** (regarding Pydantic version):
  - .dict() function is now renamed to .model_dump()

  - chema_extra function within a Config class is now renamed to json_schema_extra

  - Optional variables need a =None example: id: Optional[int] = None
