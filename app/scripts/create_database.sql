

DROP DATABASE iot;

CREATE DATABASE iot;

USE iot;

CREATE TABLE wagon (
        wagon_id int NOT NULL PRIMARY KEY
);

CREATE TABLE sensor_data (
	sensor_id int,
	timestamp bigint,
	type varchar(25),
	value float,
	wagon int,
        primary key(sensor_id,timestamp)	
);

CREATE TABLE actuator (
	ip_address varchar(25) NOT NULL PRIMARY KEY,
	state varchar(25),
	type varchar(25),
	wagon int
);
