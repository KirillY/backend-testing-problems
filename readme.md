# Backend testing problems

Probation project

## Installation

##### Clone the repo

##### Switch to the project dir
```bash
cd yourproject
```
##### Clone the project 
```bash
git clone https://github.com/KirillY/backend-testing-project.git
```
##### Option 1: Install pipenv, create virtual environment, switch and install all dependencies
```bash
pip install pipenv
pipenv --python 3.7
pipenv shell
pipenv install --dev
```
##### Option 2: More traditional workflow without pipenv (Unix)
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
##### Problem 1.2: build bash script using wget
```bash
cat test2.txt | cut -d' ' -f3 > img_urls
wget -i img_urls -P pic && rm img_urls
```
##### Problem 1.3: test HTTP API
```python
```
##### Problem 2: build framework for a Google Places API testing
```python
```
## Run tests
```bash
pytest -v
```

## License
[MIT](https://choosealicense.com/licenses/mit/)