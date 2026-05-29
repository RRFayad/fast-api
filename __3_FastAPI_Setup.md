## Fast API

[Docs:](https://fastapi.tiangolo.com/)

### 4. Setup and Installation

- Pip is the Python Package Manager

#### Steps:

- Go to DOcuments folder (cd Documents)
- mkdir fastapi
  - cd fastapi
  - python3 -m venv fastapienv
  - We need to activate it: source fastapienv/bin/activate
    - we can simply type deactivate
  - pip install fastapi
- pip install "uvicorn[standard]"

#### Run Server

source .venv/bin/activate
python -m uvicorn main:app --reload
url: http://127.0.0.1:8000/...
