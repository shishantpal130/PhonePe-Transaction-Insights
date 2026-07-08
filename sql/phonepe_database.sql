CREATE DATABASE phonepe;

USE phonepe;


CREATE TABLE aggregated_transaction
(
state VARCHAR(100),
year INT,
quarter INT,
transaction_type VARCHAR(100),
transaction_count BIGINT,
transaction_amount DOUBLE
);


CREATE TABLE aggregated_user
(
state VARCHAR(100),
year INT,
quarter INT,
registered_users BIGINT,
app_opens BIGINT
);


CREATE TABLE aggregated_insurance
(
state VARCHAR(100),
year INT,
quarter INT,
insurance_type VARCHAR(100),
transaction_count BIGINT,
transaction_amount DOUBLE
);



CREATE TABLE map_transaction
(
state VARCHAR(100),
year INT,
quarter INT,
district VARCHAR(100),
transaction_count BIGINT,
transaction_amount DOUBLE
);



CREATE TABLE map_user
(
state VARCHAR(100),
year INT,
quarter INT,
district VARCHAR(100),
registered_users BIGINT,
app_opens BIGINT
);



CREATE TABLE map_insurance
(
state VARCHAR(100),
year INT,
quarter INT,
district VARCHAR(100),
transaction_count BIGINT,
transaction_amount DOUBLE
);



CREATE TABLE top_transaction
(
state VARCHAR(100),
year INT,
quarter INT,
level VARCHAR(50),
name VARCHAR(100),
count BIGINT,
amount DOUBLE
);



CREATE TABLE top_user
(
state VARCHAR(100),
year INT,
quarter INT,
level VARCHAR(50),
name VARCHAR(100),
registered_users BIGINT
);



CREATE TABLE top_insurance
(
state VARCHAR(100),
year INT,
quarter INT,
district VARCHAR(100),
count BIGINT,
amount DOUBLE
);