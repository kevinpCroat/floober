from flask import Flask,jsonify,make_response,abort,render_template,request
import json

app = Flask(__name__)

@app.route('/')
@app.route('/api')
def index():
	return render_template('index.html')

@app.errorhandler(404)
def not_found(error):
	return make_response(jsonify({'error':str('Resource not found: ' + request.url)}), 404)


@app.route('/api/trips', methods= ['GET'])
@app.route('/api/trips/<start_date>/<end_date>', methods = ['GET'])
def get_number_of_trips(start_date=None,end_date=None):
	""" sums the total number of trips"""
	#cursor.execute("Select count(*) from event_trip")
	#result = cursor.result()
	#total_num_of_trips = result.fetch_one()
		
	total_num_of_trips = {}
	total_num_of_trips['start_date']=start_date
	total_num_of_trips['end_date']=end_date
	total_num_of_trips['trips']='33'

	return jsonify({'total_number_of_trips' : total_num_of_trips})
	

@app.route('/api/clients', methods = ['GET'])
@app.route('/api/clients/<start_date>/<end_date>', methods = ['GET'])
def get_total_number_of_clients(start_date=None,end_date=None):
	""" sums the total number of trips"""
	#cursor.execute("Select count(*) from event_trip")
	#result = cursor.result()
	#total_num_of_trips = result.fetch_one()
	total_num_of_clients = {}
	total_num_of_clients['start_date']=start_date
	total_num_of_clients['end_date']=end_date
	total_num_of_clients['clients']='33'


	return jsonify({'total_number_of_clients' : total_num_of_clients})

@app.route('/api/trips/hour', methods = ['GET'])
def get_total_number_of_trips_last_hour():
	pass

	return jsonify({'total_number_of_trips_last_hour' : total_num_of_trips_last_hour})

@app.route('/api/clients/miles', methods = ['GET'])
@app.route('/api/clients/miles/<start_date>/<end_date>', methods = ['GET'])
def get_miles_per_client(start_date=None,end_date=None):
	pass
	
	if start_date and end_date:
		miles_per_client = {}
		miles_per_client['start_date']=start_date
		miles_per_client['end_date']=end_date
		miles_per_client['client_id']='33'
		miles_per_client['miles']='15'
	else:
		miles_per_client = 22
		
		
	return jsonify({'total_miles_per_client' : miles_per_client})

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
	
