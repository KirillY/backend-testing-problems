# Backend testing problems

Probation project

## Installation

##### Clone the repo

##### Clone the project 
```bash
git clone https://github.com/KirillY/backend-testing-project.git
```
##### Switch to the project dir
```bash
cd backend-testing-project
```
##### Option 1: Install pipenv, create virtual environment, switch to it and install all dependencies
```bash
pip install pipenv
pipenv --python 3.7
pipenv shell
pipenv install --dev
```
##### Option 2: Using venv+pip instead of pipenv (Unix)
```bash
virtualenv -p /usr/bin/python3 venv/
. venv/bin/activate
pip install -r requirements.txt
```

## Usage
### 
##### Problem 1.1: execute an SQL query using join
```bash
cd sql_project
python join_users_purchases.py
```
##### Problem 1.2: build bash script using wget (Unix)
```bash
cd bash_project
rm -r pic
cat test2.txt | cut -d' ' -f3 > img_urls
wget -i img_urls -P pic && rm img_urls && ll pic
```
##### Problem 1.3: test HTTP API
##### run and follow localhost link to inspect .md document
```bash
pipenv install grip
cd http_api_project
grip solution_description.md
```
##### Problem 2: build testing framework for a Google Places API
```bash

```
## Run internal tests
```bash
python -m pytest -v
```

## License
[MIT](https://choosealicense.com/licenses/mit/)