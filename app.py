from flask import Flask,jsonify,make_response,abort,render_template,request,_app_ctx_stack
import json
from sqlite3 import dbapi2 as sqlite3

#db_config
DATABASE = '/tmp/floober.db'
USERNAME = ''
PASSWORD = ''

#setup the app
app = Flask(__name__)
app.config.from_object(__name__)
app.config.from_envvar('APP_SETTINGS', silent=True)

def connect_db():
	top = _app_ctx_stack.top
	if not hasattr(top,'sqlite_db'):
		sqlite_db = sqlite3.connect(app.config['DATABASE'])
		sqlite_db.row_factory = sqlite3.Row
		top.sqlite_db = sqlite_db
		
	return top.sqlite_db
	
@app.teardown_appcontext
def close_db_conn(exception):
	top = _app_ctx_stack.top
	if hasattr(top,'sqlite_db'):
		top.sqlite_db.close()


@app.route('/')
@app.route('/api')
def index():
	#db = connect_db()
	#cur = db.execute('Select driver_id from event_trip')
	#driver_list = cur.fetchall()
	
	#drivers = []
	
	#for each_driver in driver_list:
		#drivers.append({'driver_id':each_driver[0]})
	
	#return jsonify( {'driver': drivers})
	return render_template('index.html')

@app.errorhandler(404)
def resource_not_found(error):
	return make_response(jsonify({'error':str('Resource not found: ' + request.url)}), 404)


@app.route('/api/trips', methods= ['GET'])
@app.route('/api/trips/<start_date>/<end_date>', methods = ['GET'])
def get_number_of_trips(start_date=None,end_date=None):
	""" sums the total number of trips format YYYY-MM-DD"""
	
	db = connect_db()
	
	if not start_date:
		cur = db.execute('Select count(*) from event_trip')
	elif start_date:
		qry = "Select count(*) from event_trip where start_time between '%s' and '%s'" % (start_date,end_date)
		cur = db.execute(qry)
	
	trip_count = cur.fetchall()
	
	trips_list = []
	total_num_of_trips = {}
	total_num_of_trips['start_date']=start_date
	total_num_of_trips['end_date']=end_date
	total_num_of_trips['trips']=trip_count[0][0]
	trips_list.append(total_num_of_trips)

	return jsonify({'total_number_of_trips' : trips_list})
	

@app.route('/api/clients', methods = ['GET'])
@app.route('/api/clients/<start_date>/<end_date>', methods = ['GET'])
def get_total_number_of_clients(start_date=None,end_date=None):
	""" sums the total number of clients who've taken trips"""
	
	db = connect_db()
	
	if not start_date:
		cur = db.execute('Select count(distinct(client_id)) from event_trip where driver_id is not null')
	elif start_date:
		qry = "Select count(distinct(client_id)) from event_trip where start_time between '%s' and '%s' and driver_id is not null" % (start_date,end_date)
		cur = db.execute(qry)
	
	client_count = cur.fetchall()
	
	#added in these lists so I always return a list of dicts
	clients_list = []
	total_num_of_clients = {}
	total_num_of_clients['start_date']=start_date
	total_num_of_clients['end_date']=end_date
	total_num_of_clients['clients']=client_count[0][0]
	clients_list.append(total_num_of_clients)


	return jsonify({'total_number_of_clients' : clients_list})

@app.route('/api/trips/hour', methods = ['GET'])
def get_total_number_of_trips_last_hour():
	db = connect_db()
	
	cur = db.execute("Select count(*) from event_trip where start_time between  datetime('now','-1 hours') and datetime('now') and driver_id is not null")
	trips_count = cur.fetchall()
	
	#added in these lists so I always return a list of dicts
	trips_hr_list = []
	total_num_of_trips = {}
	total_num_of_trips['time_slice']='last_hour'
	total_num_of_trips['clients']=trips_count[0][0]
	trips_hr_list.append(total_num_of_trips)

	return jsonify({'total_number_of_trips_last_hour' : trips_hr_list})

@app.route('/api/clients/miles', methods = ['GET'])
@app.route('/api/clients/miles/<start_date>/<end_date>', methods = ['GET'])
def get_miles_per_client(start_date=None,end_date=None):
	pass
	
	db = connect_db()
	
	cur = db.execute("select sum(distance) as dist,client_id from event_trip group by client_id")
	client_list = cur.fetchall()
	
	miles_client_list = []
	
	for each_client in client_list:
		miles_client_list.append({'client_id':each_client[1], 'distance':each_client[0]})
	
	#return jsonify( {'driver': drivers})
		
		
	return jsonify({'total_miles_per_client' : miles_client_list})

@app.route('/api/trips/fare/avg/city/<upper_right>/<lower_left>' , methods = ['GET'])
@app.route('/api/trips/fare/avg/city/<upper_right>/<lower_left>/<start_date>/<end_date>' , methods = ['GET'])
def get_avg_fare_for_city(upper_right,lower_left,start_date=None,end_date=None):
	pass
	return jsonify({'avg_fare_for_city' : avg_fare_for_city})


@app.route('/api/driver/<int:driver_id>/rating/median', methods = ['GET'])
@app.route('/api/driver/<int:driver_id>/rating/median/<start_date>/<end_date>', methods = ['GET'])
def get_median_rating_for_driver(driver_id,start_date=None,end_date=None):
	"""gets the median rating for a driver"""
	pass
	median_rating_for_driver = {}
	median_rating_for_driver['driver_id']=driver_id
	median_rating_for_driver['median_rating']=median_rating
	median_rating_for_driver['start_date']=start_date
	median_rating_for_driver['end_date']=end_date
		
	return jsonify({'median_rating_for_driver' : median_rating_for_driver})


if __name__ == "__main__":
	app.run(debug = True)
	
