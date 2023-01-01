First install the requirements

    pip install -r requirements.txt

***
Create database and tables

    python init.py

***
Run the redis server

    redis-server

***
Run celery beat in a new terminal

    celery -A main_app.celery beat -l info

***
Run celery worker in a new terminal

    celery -A main_app.celery worker -l info

***

Run the Flask app on your local host in a new terminal

    python main.py

***

You can go to

    http://127.0.0.1:5000/get-ram-info?n=5

and check the result.

