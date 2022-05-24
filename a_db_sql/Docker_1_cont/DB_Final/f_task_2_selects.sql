-- Task 2 Selects with joins & indexes

SET enable_seqscan TO on;
SET enable_seqscan TO off;

-- rented cars with no-s 6,12
EXPLAIN ANALYSE
SELECT c.car_id, c.car_no, c.model_id
FROM car c
    LEFT JOIN rental
        ON rental.car_no = c.model_id
    WHERE rental.car_no IN (6,12)
ORDER BY c.model_id;
-- Merge Join  (cost=495.77..532.22 rows=2425 width=40) (actual time=1.894..2.412 rows=2425 loops=1)
CREATE INDEX car_id_idx ON car(car_id);
CREATE INDEX rental_idx ON rental USING btree(rental_id);
-- Nested Loop  (cost=0.00..370.99 rows=1180 width=40) (actual time=0.023..3.803 rows=1180 loops=1)
drop index if exists car_id_idx;
drop index if exists rental_idx;

-----------------------------

-- select data about users from cities 8....
EXPLAIN (ANALYSE, BUFFERS)
select first_name, last_name, a.address_id, city.city_name, street_name, a.house_no
from customer cus
         left join address a on cus.address_id = a.address_id
         left join street on a.street_id = street.street_id
         left join city on street.city_id = city.city_id
where city.city_id >8;

-- Hash Join  (cost=612.81..931.10 rows=4029 width=565) (actual time=12.614..177.762 rows=5600 loops=1)

create index customer_idx on customer USING hash(address_id);
create index city_id_idx on city using hash(city_id);
-- Nested Loop  (cost=288.65..907.52 rows=4000 width=565) (actual time=5.824..19.607 rows=5600 loops=1)
drop index if exists customer_idx;
drop index if exists city_id_idx;


--------------------------------------

-- select long rents
EXPLAIN (ANALYZE, BUFFERS)
    SELECT c.first_name, c.last_name, p.price, b.address_id, r.rental_period
FROM customer c
    LEFT JOIN rental r ON c.customer_id = r.rental_id
    LEFT JOIN payment p on r.rental_id = p.payment_id
    LEFT JOIN rental_branch b ON r.branch_id = b.branch_id
WHERE r.rental_period BETWEEN 8 AND 14;
--Hash Right Join  (cost=926.97..1358.55 rows=6008 width=47) (actual time=17.764..23.648 rows=5963 loops=1)