# Backend testing problems

Probation project

## Installation

##### Clone the project 
```bash
git clone https://github.com/KirillY/backend-testing-problems.git
```
##### Switch to the project dir
```bash
cd backend-testing-problems
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
##### Option 3: Using docker
install docker https://docs.docker.com/engine/installation/
```bash
docker-compose build
docker-compose up
```
copy and paste provided url into your browser, 
run Jupyter cells using Ctrl+Enter 

Ctrl+C in terminal to end up Jupyter session

## Usage (Option 1 or 2)
### 
##### Problem 1.1: execute an SQL query using join
```bash
cd sql_problem
python join_users_purchases.py
```
##### Problem 1.2: build bash script using wget (Unix)
```bash
cd bash_problem
rm -r pic
cat test2.txt | cut -d' ' -f3 > img_urls
wget -i img_urls -P pic && rm img_urls && ll pic
```
##### Problem 1.3: test HTTP API
##### run and follow localhost link to inspect .md document
```bash
pipenv install grip
cd http_api_problem
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