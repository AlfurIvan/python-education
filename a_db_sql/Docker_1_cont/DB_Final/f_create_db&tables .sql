CREATE DATABASE car_rent_db_final;

CREATE TABLE customer
(
    customer_id int primary key unique,
    first_name varchar(255),
    last_name varchar(255),
    address_id int references address(address_id),
    tel_id int references telephone(tel_id)
);
drop table telephone cascade ;

CREATE TABLE telephone
(
    tel_id int,
    tel_number varchar(255)
);
CREATE TABLE address
(
    address_id int primary key unique,
    house_no int,
    street_id int references street(street_id) ,
    city_id int references city(city_id),
    type_id int references street_type(type_id)
);

drop table street;
CREATE TABLE IF NOT EXISTS street
(
    street_id SERIAL PRIMARY KEY UNIQUE ,
    street_name varchar(255),
    city_id int references city(city_id)
);
CREATE TABLE street_type
(
    type_id int primary key unique,
    type_name varchar(255)
);
CREATE TABLE city
(
    city_id int primary key unique,
    city_name varchar(255)
);

--
CREATE TABLE rental
(
    rental_id int primary key unique ,
    customer_id int references customer(customer_id),
    branch_id int references rental_branch(branch_id),
    car_no int references car(car_no),
    rental_date timestamp,
    rental_period int -- days
);

--
CREATE TABLE rental_branch
(
    branch_id int primary key unique,
    address_id int references address(address_id),
    tel_id int references telephone(tel_id)
);
CREATE TABLE payment
(
    payment_id int primary key,
    price money
);

DROP TABLE car cascade;
CREATE TABLE car
(
    car_id int primary key unique,
    car_no  varchar,
    model_id int references model(model_id)
);

drop table model cascade ;
CREATE TABLE model
(
    model_id int primary key unique,
    model_name varchar(255),
    payment_for_car money,
    manufacturer_id int references manufacturer(manufacturer_id)
);
CREATE TABLE manufacturer
(
    manufacturer_id int primary key unique ,
    manufacturer_name varchar(255)
);



