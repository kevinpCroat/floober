#import packages
import sqlite3 as sql
import logging
import json
import traceback
import time

logging.basicConfig(filename='db_exceptions.log', level=logging.DEBUG)

#setup the database conn
db = sql.connect('/tmp/floober.db')
#instantiate the cursor class
cur = db.cursor()


def record_trip_event(client_id,driver_id,start_time,lat,lng,fare,distance,rating):
	"""records trip event data to db - client_id,driver_id,start_time,lat,lng,fare,distance,rating"""
	
	sql_insert = """INSERT INTO event_trip (client_id,driver_id,start_time,lat,lng,fare,distance,rating)
	VALUES (%s,%s,%s,%s,%s,%s,%s,%s)""" % (client_id,driver_id,start_time,lat,lng,fare,distance,rating)
	
	cur.execute(sql_insert)
	db.commit()
	print 'success'
	

def main():
	#open a file
	# is incoming data is in json format?
	#process each line
	
	while True:
		try:
			record_trip_event(123,100,time.strftime('%Y-%m-%d %H:%M:%S'), '77.5093383','-34.39383839', '22.11', '4.3', '4')
		except Exception, exc:
			logging.debug(traceback.format_exc())
	
	
if __name__ == "__main__":
	main()