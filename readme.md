# WagaTask made with FastAPI, SQLAlchemy and SQLite


## Table of contents
* [Introduction](#Introduction)
* [Technologies](#technologies)
* [Installation](#Installation)


# Introduction
Read weather data from desired City (forecasted and measured)
Compare differences between measured and forecasted data, if exists.


# Technologies
Technologies used on this project:
+ Python 3.10
+ SQLAlchemy 1.4.46
+ FastAPI
+ Uvicorn
+ requests library
+ SQLite


## Installation


### Create virtual environment
#### PyCharm
```bash
venv ./venv
```
#### Windows
Open Command Prompt or PowerShell, navigate to project folder and run:
```bash
python -m venv ./venv
```
#### Linux/MacOS
Open terminal, navigate to project directory and run:
```bash
python -m venv ./venv
```
If that previous command didn't work, install virtualenv:
```bash
pip install virtualenv
```
Run command in project directory to create a virtual env:
```bash
virtualenv venv
```


### Activate Virtual environment
Open terminal and navigate to project directory, then run:

| Platform | Shell      | Command to activate virtual environment |
|----------|------------|-----------------------------------------|
| POSIX    | bash/zsh   | $ source venv/bin/activate              |
|          | fish       | $ source venv/bin/activate.fish         |
|          | csh/tcsh   | $ source venv/bin/activate.csh          |
|          | PowerShell | $ venv/bin/Activate.ps1                 |
| Windows  | cmd.exe    | C:\> venv\Scripts\activate              |
|          | PowerShell | PS C:\> venv\Scripts\Activate.ps1       |


### Dependencies
Use the package manager [pip](https://pip.pypa.io/en/stable/) to install dependencies.
```bash
pip install -r requirements.txt
```


### Environment variables
1. Create a new file **_.env_**
2. Copy all constants from **env-template** to **_.env_**
3. Assign values to constants in .env file


### Database
Run populate_base.py:
From PyCharm or terminal, activate venv, cd to app\command, then:
```bash
python populate_base.py
```


## Run server
Navigate back to project folder, venv is still active and then:

From terminal
```bash
python -m uvicorn app.main:app --reload --reload-delay 5 --host localhost --port 8000
```
From PyCharm
```bash
uvicorn app.main:app --reload --reload-delay 5 --host localhost --port 8000
```

Open localhost:8000 in your browser.
