----Task 3 Views

--
CREATE OR REPLACE VIEW long_rents_view AS
SELECT rental_id, c.first_name, c.last_name, t.tel_number, rental_date, rental_period
FROM rental r
LEFT OUTER JOIN customer c on c.customer_id = r.customer_id
LEFT JOIN telephone t on c.tel_id = t.tel_id
WHERE r.rental_period BETWEEN 10 AND 15;

SELECT count(*) FROM long_rents_view;
DROP VIEW IF EXISTS get_over_price_rents;

--
CREATE OR REPLACE VIEW full_address_view AS
SELECT c.customer_id, first_name, last_name, city.city_name, s.street_name, a.house_no
FROM customer c
         LEFT JOIN address a on c.address_id = a.address_id
         LEFT JOIN street s on a.street_id = s.street_id
         LEFT JOIN city on s.city_id = city.city_id;


SELECT count(customer_id)
FROM full_address_view
WHERE city_name LIKE '%2';

DROP VIEW IF EXISTS full_address_view;

-- material
CREATE MATERIALIZED VIEW IF NOT EXISTS customers_n_cars_mview AS
SELECT c.first_name, c.last_name, r.rental_id, m.payment_for_car, m.model_name, man.manufacturer_name
FROM customer c
    LEFT JOIN rental r on c.customer_id = r.rental_id
    LEFT JOIN car cr on r.car_no = cr.car_id
    LEFT JOIN model m on cr.car_id = m.model_id
    LEFT JOIN manufacturer man on m.manufacturer_id = man.manufacturer_id;

SELECT count(*) FROM customers_n_cars_mview WHERE model_name LIKE '%2';

DROP MATERIALIZED VIEW IF EXISTS customers_n_cars_mview;