---------------------------------------------------------------------------

CREATE OR REPLACE VIEW products_view AS
SELECT product_title, product_description, in_stock, price, slug
FROM products;

SELECT product_title, product_description, price, slug
FROM products_view;

SELECT product_title, price, slug
FROM products_view
WHERE in_stock = 0;

SELECT product_title, price, slug
FROM products_view
ORDER BY price
LIMIT 20;

DROP VIEW IF EXISTS products_view;

---------------------------------------------------------------------------

CREATE OR REPLACE VIEW product_cats_view AS
SELECT product_title, in_stock, price, category_title, category_description
FROM products p
         LEFT JOIN categories c
                   ON p.category_id = c.category_id;

SELECT product_title, category_title, category_description
FROM product_cats_view
ORDER BY price DESC
LIMIT 10;

SELECT product_title, price, category_title, category_description
FROM product_cats_view
ORDER BY in_stock DESC
LIMIT 10;

SELECT *
FROM product_cats_view
WHERE category_title ~ '\s7';

DROP VIEW IF EXISTS product_cats_view;

---------------------------------------------------------------------------

CREATE OR REPLACE VIEW order_paid_view AS
SELECT order_id, cart_cart_id, shipping_total, total, updated_at
FROM orders
WHERE order_status_order_status_id = 3;

SELECT *
FROM order_paid_view
ORDER BY total
LIMIT 5;

SELECT order_id, cart_cart_id, shipping_total, total
FROM order_paid_view
WHERE updated_at < '2021-12-23'
ORDER BY total
LIMIT 20;

SELECT *
FROM order_paid_view
ORDER BY order_id
LIMIT 15;

DROP VIEW IF EXISTS get_full_product_info;

---------------------------------------------------------------------------

CREATE MATERIALIZED VIEW get_user_waiting_order AS
SELECT u.first_name, u.last_name, u.middle_name, o.total, os.status_name, o.updated_at
FROM users u
         LEFT JOIN carts c ON u.user_id = c.users_user_id
         LEFT JOIN orders o ON c.cart_id = o.cart_cart_id
         LEFT JOIN order_status os ON o.order_status_order_status_id = os.order_status_id
WHERE os.order_status_id <> 4;


SELECT first_name, middle_name, sum(total)
FROM get_user_waiting_order
GROUP BY first_name, middle_name
ORDER BY sum(total) DESC
LIMIT 25;


DROP MATERIALIZED VIEW get_user_waiting_order;

---------------------------------------------------------------------------
