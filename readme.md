### Memory Management

#### Python Interpreter version: 
Python 3.9

##### To activate virtual environment:

    https://stackoverflow.com/questions/1534210/use-different-python-version-with-virtualenv


### Installation guide

#### Install the requirements

    pip install -r requirements.txt

***
#### Create database and tables

    python init_db.py

***
#### Run the redis server

    redis-server

***
#### Run celery beat in a new terminal
    celery -A main_app.celery beat -l info

***
#### Run celery worker in a new terminal

    celery -A main_app.celery worker -l info

***

#### Run the Flask app on your local host in a new terminal

    python main.py

***
#### To check the api service

Enter this address in the browser

    http://127.0.0.1:5000/get-ram-info?n=5

and check the result.

