-- manufacturer
CREATE OR REPLACE PROCEDURE fill_manufacturer(count INT)
    language plpgsql
AS
$$
BEGIN
    for i in 1..count
        loop
            INSERT INTO manufacturer(manufacturer_id, manufacturer_name)
            SELECT (i)::INT, ('Manufacturer ' || i)::VARCHAR;
        end loop;
END
$$;
DROP PROCEDURE fill_manufacturer(count INT);
CALL fill_manufacturer(3);



CREATE OR REPLACE FUNCTION random_in(min INT, max INT)
    RETURNS INT AS
$$
BEGIN
    RETURN floor(random() * (max - min + 1) + min);
END;
$$ language plpgsql;


--model
CREATE OR REPLACE PROCEDURE fill_model(models INT)
    language plpgsql
AS
$$
declare
    k   INT;
    i   INT;
    sum INT;
BEGIN
    k = 0;
    for m in 1..3
        loop
            i = 0;
            for i in 1..models
                loop
                    sum = k + i;
                    INSERT INTO model
                    SELECT (sum)::int, ('MODEL ' || i || ' ' || sum)::varchar, (random_in(100, 300))::money, m::int;
                end loop;
            k = k + 5;
        end loop;
END
$$;
CALL fill_model(models := 5);
DROP PROCEDURE fill_model(models INT);

-- car
CREATE OR REPLACE PROCEDURE fill_car(count INT)
    language plpgsql
AS
$$
BEGIN
    for i in 1..count
        loop
            INSERT INTO car(car_id, car_no, model_id)
            SELECT (i)::INT, (random_in(10000, 99999))::INT, (i)::INT;
        end loop;
END
$$;
CALL fill_car(15);
DROP PROCEDURE fill_car(count INT);

-- telephone
CREATE OR REPLACE PROCEDURE fill_telephone(count INT)
    language plpgsql
AS
$$
BEGIN
    for i in 1..count * 2 / 3
        loop
            INSERT INTO telephone(tel_id, tel_number)
            SELECT (i)::INT, ('+' || random_in(1000, 9999)::varchar || random_in(1000, 9999)::varchar)::varchar;
        end loop;
    for i in 1..count / 3
        loop
            I = I + 0;
            INSERT INTO telephone(tel_id, tel_number)
            SELECT (random_in(1, 12000))::INT,
                   ('+' || random_in(1000, 9999)::varchar || random_in(1000, 9999)::varchar)::varchar;
        end loop;
END
$$;
CALL fill_telephone(12000);
DROP PROCEDURE fill_telephone(count INT);


INSERT INTO public.street_type (type_id, type_name)
VALUES (1, 'Road'),
       (2, 'Street'),
       (3, 'Avenue'),
       (4, 'Boulevard'),
       (5, 'Lane'),
       (6, 'Drive'),
       (7, 'Way'),
       (8, 'Plaza'),
       (9, 'Terrace'),
       (10, 'Place'),
       (11, 'Frontage Road '),
       (12, 'Highway'),
       (13, 'Interstate'),
       (14, 'Turnpike'),
       (15, 'Freeway'),
       (16, 'Parkway'),
       (17, 'Causeway'),
       (18, 'Beltway'),
       (19, 'Crescent'),
       (20, 'Alley'),
       (21, 'Esplanade');


-- City s
CREATE OR REPLACE PROCEDURE fill_city(count INT)
    language plpgsql
AS
$$
BEGIN
    for i in 1..count
        loop
            INSERT INTO city(city_id, city_name)
            SELECT (i)::INT, ('Mykhosransk ' || i)::VARCHAR;
        end loop;
END
$$;
CALL fill_city(15);
DROP PROCEDURE fill_city(count INT);

-- Street
CREATE OR REPLACE PROCEDURE fill_street(count INT)
    language plpgsql
AS
$$
BEGIN

    for i in 1..count
        loop
            INSERT INTO street(street_id, street_name, city_id)
            SELECT i::INT, ('Street ' || i % 800 + 1)::varchar(255), (i % 15 + 1)::INT;
        end loop;

END
$$;
CALL fill_street(12000);
DROP PROCEDURE fill_street(count INT);

-- ALTER TABLE address drop COLUMN city_id;

-- Address
CREATE OR REPLACE PROCEDURE fill_address(count INT)
    language plpgsql
AS
$$
DECLARE
    f INT;
BEGIN

    for i in 1..count
        loop
            f = i;
            INSERT INTO address(address_id, street_id, type_id, house_no)
            SELECT f::INT, i::INT, random_in(1, 21)::INT, (f / 10000 + f / 1000 % 10 + f / 100 % 10 + f % 10)::INT;
        end loop;

END
$$;
CALL fill_address(12000);
DROP PROCEDURE fill_address(count INT);

----------------------------------
--rental
CREATE OR REPLACE PROCEDURE fill_rental(count INT)
    language plpgsql
AS
$$
DECLARE
    f INT;
BEGIN

    for i in 1..count / 3 * 2
        loop
            f = i;
            INSERT INTO rental(rental_id, customer_id, branch_id, car_no, rental_date, rental_period)
            SELECT f::INT,
                   f::INT,
                   random_in(1, 10)::INT,
                   random_in(1, 15)::INT,
                   ((2018 + random_in(1, 4))::varchar || '-' ||
                    (random_in(1, 12))::varchar || '-' ||
                    (random_in(1, 27))::varchar)::timestamp,
                   random_in(1, 14)::INT;
        end loop;
    for i in 1..count / 3
        loop
            f = i;
            INSERT INTO rental(rental_id, customer_id, branch_id, car_no, rental_date, rental_period)
            SELECT f + count / 3 * 2::INT,
                   random_in(1, 12000)::INT,
                   random_in(1, 10)::INT,
                   random_in(1, 15)::INT,
                   ((2018 + random_in(1, 4))::varchar || '-' ||
                    (random_in(1, 12))::varchar || '-' ||
                    (random_in(1, 27))::varchar)::timestamp,
                   random_in(1, 14)::INT;
        end loop;
END
$$;
CALL fill_rental(18000);
DROP PROCEDURE fill_rental(count INT);

-- Customers
CREATE OR REPLACE PROCEDURE fill_customers(count INT)
    language plpgsql
AS
$$
DECLARE
    f INT;
BEGIN

    for i in 1..count
        loop
            f = i;
            INSERT INTO customer(customer_id, first_name, last_name, address_id, tel_id)
            SELECT f::INT,
                   'First Name ' || f::varchar(255),
                   'Last Name ' || f::varchar(255),
                   f::INT,
                   f::INT;
        end loop;

END
$$;
CALL fill_customers(12000);


-- rental address
CREATE OR REPLACE PROCEDURE fill_address(count INT)
    language plpgsql
AS
$$
DECLARE
    f INT;
BEGIN

    for i in 1..count
        loop
            f = i;
            INSERT INTO address(address_id, street_id, type_id, house_no)
            SELECT f + 12000::INT,
                   i * 14::INT,
                   random_in(1, 21)::INT,
                   (f / 10000 + f / 1000 % 10 + f / 100 % 10 + f % 10)::INT;
        end loop;

END
$$;
CALL fill_address(10);
DROP PROCEDURE fill_address(count INT);

-- rental telephone
-- telephone
CREATE OR REPLACE PROCEDURE fill_telephone(count INT)
    language plpgsql
AS
$$
BEGIN
    for i in 1..count
        loop
            INSERT INTO telephone(tel_id, tel_number)
            SELECT (i + 12000)::INT, ('+' || 9989000::varchar || (i - 1)::varchar)::varchar;
        end loop;
END
$$;
CALL fill_telephone(10);
DROP PROCEDURE fill_telephone(count INT);

-- rental_branch
INSERT INTO public.rental_branch (branch_id, address_id, tel_id)
VALUES (1, 12001, 12001),
       (2, 12002, 12002),
       (3, 12003, 12003),
       (4, 12004, 12004),
       (5, 12005, 12005),
       (6, 12006, 12006),
       (7, 12007, 12007),
       (8, 12008, 12008),
       (9, 12009, 12009),
       (10, 12010, 12010);

-- price
CREATE OR REPLACE PROCEDURE fill_price(count INT)
    language plpgsql
AS
$$
DECLARE

BEGIN
   for i in 1..count
        loop
            INSERT INTO payment(payment_id, price)
            SELECT (i)::INT, NULL;
        end loop;

END
$$;
CALL fill_price(18000);
DROP PROCEDURE fill_price(count INT);


-- price field added manually after manipulations in LibreOffice, like Excel)