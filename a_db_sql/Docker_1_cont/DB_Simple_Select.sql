-- TASK 1 --
---- all users
SELECT first_name || ' __ ' || last_name || ' __ ' || middle_name -- *
FROM users;

---- all products
SELECT product_title -- *
FROM products;

---- all order statuses
SELECT status_name -- *
FROM order_status;


-- TASK 2 --
---- payed and delivered orders
SELECT order_id -- *
FROM orders
WHERE order_status_order_status_id = 4; --дос_тав_ле_ны и опл_аче_ны:
                                        -- опл_ата по_сле дос_та_вки?
                                        -- ес_ли да: IN (3, 4)


-- TASK 3 --

---- 80 < price <= 150
SELECT product_title
FROM products
WHERE price > 80 -->=81
  AND price < 151;
--<=150
------other--
SELECT product_title
FROM products
WHERE price BETWEEN 81 AND 150;

---- orders after 01.10.2020
SELECT order_id -- *
FROM orders
WHERE created_at > '01-10-2020';
------other--
SELECT order_id -- *
FROM orders
WHERE created_at BETWEEN '01-10-2020' AND now();

---- orders for first half 2020
SELECT order_id -- *
FROM orders
WHERE created_at >= '2020-01-01' AND created_at <= '2020-07-01';
------other--
SELECT order_id -- *
FROM orders
WHERE created_at BETWEEN '01-01-2020' AND '01-07-2020';

---- products from Category 7, Category 11, Category 18
SELECT product_title -- *
FROM products
WHERE category_id IN (7, 11, 18);
------other--
SELECT product_title -- *
FROM products
WHERE category_id = 7 OR category_id = 11 OR category_id = 18;

---- unfinished orders at 31.12.2020
SELECT order_id -- *
FROM orders
WHERE order_status_order_status_id != 4 AND updated_at <= '2020-12-31';

---- cancelled orders
SELECT cart_cart_id -- * это_т зна_чок зна_чит, что тут
FROM orders         -- мож_но мн_ого че_го раз_но_го пис_ать
WHERE order_status_order_status_id = 5;


-- TASK 5
----AVERAGE
SELECT avg(total)
FROM orders
WHERE order_status_order_status_id = 4;
----MAX FOR 3-TH QU
SELECT max(total)
FROM orders
WHERE created_at >= '2020-07-01' AND created_at < '2020-10-01';
--WHERE created_at >= '01-07-2020' AND created_at < '01-10-2020'; -- wrong
------other--
SELECT max(total)
FROM orders
WHERE created_at >= '2020-07-01' AND created_at < timestamp '2020-07-01' + interval '3 months';

