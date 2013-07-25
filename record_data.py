#import packages
import MySQLdb as sql
import logging
import json

logging.basicConfig(filename='db_exceptions.log', level=logging.DEBUG)

#setup the database conn
db = sql.connect(db='event_trip',username='rootsy',passwd='lfytopia',host='server_ip')
#instantiate the cursor class
cursor = db.cursor()


def record_trip_event(client_id,driver_id,start_time,lat,lng,fare,distance,rating):
	"""records trip event data to db - client_id,driver_id,start_time,lat,lng,fare,distance,rating"""
	
	sql_insert = """INSERT INTO event_trip (client_id,driver_id,start_time,lat,lng,fare,distance,rating) /
	VALUES (%s,%s,%s,%s,%s,%s,%s,%s)""" % (client_id,driver_id,start_time,lat,lng,fare,distance,rating)
	
	cursor.execute(sql_intert)
	db.commit()
	

def main():
	#open a file
	#incoming data is in json format
	#process each line
	
	while True:
		try:
			record_trip_event(123,100,'07-21-31 12:13:15', '77.5093383','-34.39383839', '22.11', '4.3', '4')
		except Exception, exc:
			logging.debug(traceback.format_exc())
	
	
if __name__ == "__main__":
	main()