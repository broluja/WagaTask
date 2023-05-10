# WagaTask made with FastAPI, SQLAlchemy and SQLite


## Table of contents
* [Introduction](#Introduction)
* [Technologies](#technologies)
* [Installation](#Installation)


# Introduction
Search through movies, series, actors and directors with a simple JWT 
based User authentication and authorisation. Project is made as final
project on ITBootcamp, Python for web developers Course.


# Technologies
Technologies used on this project:
+ Python 3.10
+ SQLAlchemy
+ FastAPI
+ Uvicorn


## Installation


### Create virtual environment
#### PyCharm
```bash
venv ./venv
```
#### Windows
Open Command Prompt or PowerShell, navigate to project folder and run
```bash
python -m venv ./venv
```
#### Linux/MacOS
Open terminal, navigate to project directory and run
```bash
python -m venv ./venv
```
In case that previous command didn't work, install virtualenv
```bash
pip install virtualenv
```
Run command in project directory to create virtual env
```bash
virtualenv venv
```


### Activate Virtual environment
Open terminal and navigate to project directory, than run

| Platform | Shell      | Command to activate virtual environment |
|----------|------------|-----------------------------------------|
| POSIX    | bash/zsh   | $ source venv/bin/activate              |
|          | fish       | $ source venv/bin/activate.fish         |
|          | csh/tcsh   | $ source venv/bin/activate.csh          |
|          | PowerShell | $ venv/bin/Activate.ps1                 |
| Windows  | cmd.exe    | C:\> venv\Scripts\activate.bat          |
|          | PowerShell | PS C:\> venv\Scripts\Activate.ps1       |


### Dependencies
Use the package manager [pip](https://pip.pypa.io/en/stable/) to install dependencies.
```bash
pip install -r requirements.txt
```


### Database
Start MySQL server and execute all commands in **_init_db/init_db.sql_**. 
You can run **_init_db/data_** file in MySQL if you want to have some initial data to work with.


### Environment variables
1. Create a new file **_.env_**
2. Copy all consts from **env-template** to **_.env_**
3. Assign values to const in .env file


## Run server
From terminal
```bash
python -m uvicorn app.main:app --reload --reload-delay 5 --host localhost --port 8000
```
From PyCharm
```bash
uvicorn app.main:app --reload --reload-delay 5 --host localhost --port 8000
```

Superuser credentials are in env-template file.
