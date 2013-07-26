floober
=======

This is a RESTful api you can use to access data regarding the floober service - powered by flask. 

cd into app's dir

sqlite3 /tmp/floober.db < models.sql

to setup an initial data load:
python record_event_data.py #will run until you kill it

gunicorn -w 4 -b 127.0.0.1:5060 floober:app

You can now access the api. 

You can run without gunicorn by running python floober.py
