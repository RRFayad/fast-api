## Project 4 - Unit 7 Integration Testing

- Types of testing:
  - **Manual**
  - **Unit Testing**
    - Testing isolated unit components
    - Tested by frameworks (In our case Pytest)
  - **Integration Testing**
    - Tests interactions between different units or components
    - Broader scope than unit testing, since we are testing multiple units together

- Create `test` folder, with `__init__.py`;
  - `pip install pytest`
  - create a file called `test__example.py`
  - Write an assertion test - checks if a condition is true
  - SO when we run pytest, it will run all these tests files
  - **Important:** All the tests functions must have `test_` in the prefix, thats how pytests confirms its a test (otherwise it will simply be skipped)

- Inside the test functions, we use `assert` to define what will be verified, example:
  - As we can see, we can add multiple asserts by test
  - Also, we can add the err message in a string after a comma
    ```python
      def test_equal_or_not_equal():
        assert 3 == 3
        assert 3 != 3, "3 should be equal 3"
    ```
  - Some basic assertions:
    - Values
    - instances `isInstance`
    - Types

  - For objects (that will be tested more than once):
    - Test function expects Pytest fixtures as arguments only

    ```python
      @pytest.fixture
      def default_student():
          return Student("John", "Doe", "CS", 3)


      def test_person_initialization(default_student):
          assert default_student.first_name == "John"
          assert default_student.last_name == "Doe"
          assert default_student.major == "CS"
          assert default_student.years == 3
    ```

### Testing the API

- `pip install httpx`
- test api routes:

  ```python
      import __Proj_3.main as main
      from fastapi.testclient import TestClient
      from fastapi import status

      client = TestClient(main.app)

      def test_return_health_check():
          response = client.get("/healthy")
          assert response.status_code == status.HTTP_200_OK
          assert response.json() == {"status": "Healthy"}
  ```

### Testing DB and Dependencies

- Basically we need to:
  - Create a test db
  - Override dependencies (in pour to do app case, `get_db` `get_user`)
  - Create a fixture that will:
    - Write in the DB
    - Clean up (using the `with` block)

  ```python
    @pytest.fixture
    def test_todo():
        todo = Todos(
            title="Learn to code",
            description="Need consistency",
            priority=5,
            complete=False,
            owner=1,
        )

        db = TestingSessionLocal()
        db.add(todo)
        db.commit()
        yield todo
        with engine.connect() as connection:
            connection.execute(text("DELETE FROM todos;"))
            connection.commit()


    def test_read_all_authenticated(test_todo):
        response = client.get("/todo/")
        assert response.status_code == status.HTTP_200_OK
        assert response.json() == [
            {
                "id": 1,
                "title": "Learn to code",
                "description": "Need consistency",
                "priority": 5,
                "complete": False,
                "owner": 1,
            }
        ]
  ```
