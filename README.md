floober
=======

This is a RESTful api you can use to access data regarding the floober service - powered by flask. 

cd into app's dir

```shell
sqlite3 /tmp/floober.db < models.sql
```

to setup an initial data load:
```shell
python record_event_data.py #will run until you kill it
```

to setup gunicorn:

```shell
gunicorn -w 4 -b 127.0.0.1:5060 floober:app
```

You can now access the api. 

You can run without gunicorn by running:
```shell
python floober.py
```

If you want to get fancy you can run floober w/ gevent. Caution: Do NOT run gevent w/ gunicorn - unicorns will die. and so will your server.
```shell
python floober_gevent.py
```
