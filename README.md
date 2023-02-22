# CMS
## How to Run?

CMS uses django 4.1.5

### Open your favorite Terminal and run these commands.

Create a virtual environment:
1. Install virtualenv 
```sh
pip install virtualenv
```

2. Create virtual env
```sh
virtualenv venv
```

3. Activate Virtual env

- For Windows:
```sh
venv\Scripts\activate
```
- for mac/Linux:
```sh
venv/bin/activate
```

4. Install requirements:

```sh
pip install -r requirements.txt
```

## Setting up the Environment:
---
Rename ```.env.example``` as ```.env``` and paste your secret key 

Rename ```exampleinfo.py``` as ```info.py``` ans paste your email details

To run project:
Open terminal at the location where project is downloaded and ```manage.py``` file is present
run the following command:
```sh
python manage.py runserver
```
## Your server should be hosted at [Localhost](http://127.0.0.1:8000/)