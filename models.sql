-- CREATE TABLE STMT
-- author: kevin p
create table event_trip(
	client_id int unsigned not null,
	driver_id int unsigned not null,
	start_time TIMESTAMP default null,
	lat decimal(16,9) default null,
	lng decimal(16,9) default null,
	fare float default null,
	distance decimal(9,2) not null,
	rating tinyint default null,
	PRIMARY KEY(client_id), 
	UNIQUE KEY(client,driver_id,start_time)
)