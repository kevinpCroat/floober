#import packages
import sqlite3 as sql
import logging
import json
import traceback
import time
import random

logging.basicConfig(filename='db_exceptions.log', level=logging.DEBUG)

#setup the database conn
db = sql.connect('/tmp/floober.db')
#instantiate the cursor class
cur = db.cursor()


def record_trip_event(client_id,driver_id,start_time,lat,lon,fare,distance,rating):
	"""records trip event data to db - client_id,driver_id,start_time,lat,lon,fare,distance,rating"""
	
	sql_insert = """INSERT INTO event_trip (client_id,driver_id,start_time,lat,lon,fare,distance,rating) VALUES (%s,%s,'%s',%s,%s,%s,%s,%s)""" % (client_id,driver_id,start_time,lat,lon,fare,distance,rating)
	
	print sql_insert
	
	cur.execute(sql_insert)
	db.commit()
	print 'success'
		

def main():
	
	while True:
		try:
			#generate random data and insert into db
			distance = round(random.uniform(1,30),2)
			record_trip_event(random.randrange(1,40,1),random.randrange(1,12,1),time.strftime('%Y-%m-%d %H:%M:%S'), round(random.uniform(30,40),6),round(random.uniform(-122,-70),6), (3.5)+(1.75*distance), distance, random.randrange(1,6,1))
		except Exception, exc:
			logging.debug(traceback.format_exc())
	
	
if __name__ == "__main__":
	main()