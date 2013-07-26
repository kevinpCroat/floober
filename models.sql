-- CREATE TABLE STMT
-- author: kevin p
drop table if exists event_trip;
create table event_trip(
	row_id integer not null primary key autoincrement,
	client_id integer not null,
	driver_id integer not null,
	start_time datetime not null,
	lat float not null,
	lon float not null,
	fare float not null,
	distance float not null,
	rating integer not null, 
	UNIQUE (client_id,driver_id,start_time)
);

-- INITIAL TEST DATA
INSERT INTO event_trip (client_id,driver_id,start_time,lat,lon,fare,distance,rating)
 VALUES (1,2,'2013-07-01 11:33:33', 37.791812,-122.432759,12.39,3.54,5);
INSERT INTO event_trip (client_id,driver_id,start_time,lat,lon,fare,distance,rating)
 VALUES (1,3,'2013-06-01 11:33:33', 37.791812,-122.432759,22.39,5.54,1);
INSERT INTO event_trip (client_id,driver_id,start_time,lat,lon,fare,distance,rating)
 VALUES (2,2,'2013-07-02 11:33:33', 37.791812,-122.432759,2.39,1.54,1);
INSERT INTO event_trip (client_id,driver_id,start_time,lat,lon,fare,distance,rating)
 VALUES (3,4,'2013-07-25 11:31:33', 37.791812,-122.432759,32.39,6.54,2);
INSERT INTO event_trip (client_id,driver_id,start_time,lat,lon,fare,distance,rating)
 VALUES (2,5,'2013-07-25 11:33:33', 37.791812,-122.432759,16.39,4.54,3);