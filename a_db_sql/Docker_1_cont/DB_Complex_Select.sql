---------Task1---------
--create potential_customers
CREATE TABLE IF NOT EXISTS potential_customers
(
    potential_user_id serial primary key, -- id
    email             varchar(255),       -- email
    first_name        varchar(255),       -- name
    last_name         varchar(255),       -- surname
    middle_name       varchar(255),       -- second_name
    city              varchar(255)        -- city
);

--insert data
INSERT INTO potential_customers (email, first_name, last_name, middle_name, city)
VALUES ('email1@gmail.com', 'first_name 1', 'last_name 1', 'middle_name 1', 'city 3'),
       ('email2@gmail.com', 'first_name 2', 'last_name 2', 'middle_name 2', 'city 6'),
       ('email3@gmail.com', 'first_name 3', 'last_name 3', 'middle_name 3', 'city 2'),
       ('email4@gmail.com', 'first_name 4', 'last_name 4', 'middle_name 4', 'city 4'),
       ('email5@gmail.com', 'first_name 5', 'last_name 5', 'middle_name 5', 'city 14'),
       ('email6@gmail.com', 'first_name 6', 'last_name 6', 'middle_name 6', 'city 17'),
       ('email7@gmail.com', 'first_name 7', 'last_name 7', 'middle_name 7', 'city 13'),
       ('email8@gmail.com', 'first_name 8', 'last_name 8', 'middle_name 8', 'city 4'),
       ('email9@gmail.com', 'first_name 9', 'last_name 9', 'middle_name 9', 'city 9'),
       ('email10@gmail.com', 'first_name 10', 'last_name 10', 'middle_name 10', 'city 17'),
       ('email11@gmail.com', 'first_name 11', 'last_name 11', 'middle_name 11', 'city 14'),
       ('email12@gmail.com', 'first_name 12', 'last_name 12', 'middle_name 12', 'city 8'),
       ('email13@gmail.com', 'first_name 13', 'last_name 13', 'middle_name 13', 'city 17'),
       ('email14@gmail.com', 'first_name 14', 'last_name 14', 'middle_name 14', 'city 12'),
       ('email15@gmail.com', 'first_name 15', 'last_name 15', 'middle_name 15', 'city 1'),
       ('email16@gmail.com', 'first_name 16', 'last_name 16', 'middle_name 16', 'city 6'),
       ('email17@gmail.com', 'first_name 17', 'last_name 17', 'middle_name 17', 'city 17'),
       ('email18@gmail.com', 'first_name 18', 'last_name 18', 'middle_name 18', 'city 19'),
       ('email19@gmail.com', 'first_name 19', 'last_name 19', 'middle_name 19', 'city 3'),
       ('email20@gmail.com', 'first_name 20', 'last_name 20', 'middle_name 20', 'city 4'),
       ('email21@gmail.com', 'first_name 21', 'last_name 21', 'middle_name 21', 'city 7'),
       ('email22@gmail.com', 'first_name 22', 'last_name 22', 'middle_name 22', 'city 5'),
       ('email23@gmail.com', 'first_name 23', 'last_name 23', 'middle_name 23', 'city 2'),
       ('email24@gmail.com', 'first_name 24', 'last_name 24', 'middle_name 24', 'city 18'),
       ('email25@gmail.com', 'first_name 25', 'last_name 25', 'middle_name 25', 'city 6');

--pot_users & users from city 17
SELECT u.first_name,
       u.last_name,
       u.middle_name,
       u.email,
       pc.first_name,
       pc.last_name,
       pc.middle_name,
       pc.email
FROM potential_customers as pc
         INNER JOIN users u ON u.city = 'city 17'
WHERE  u.city = pc.city;
--
SELECT first_name || ' ' || last_name || ' ' || middle_name, email
FROM users
WHERE city = 'city 17'
UNION
SELECT first_name || ' ' || last_name || ' ' || middle_name, email
FROM potential_customers
WHERE city = 'city 17';


---------Task2---------
--names & emails ordered_by city & name
SELECT first_name, email
FROM users
ORDER BY city, first_name;


---------Task3---------
-- cat_name & count ord_by count desc
SELECT category_title, products.in_stock
FROM categories,
     products
WHERE categories.category_id = products.category_id
GROUP BY categories.category_title, products.category_id, products.in_stock
ORDER BY count(products.in_stock) DESC;


---------Task4---------
-- not in cart
SELECT product_title
FROM products
         LEFT OUTER JOIN cart_product cp
                         ON products.product_id = cp.products_product_id
WHERE cp.products_product_id IS NULL;

-- not in order, but in cart probably
SELECT product_title
FROM products
         LEFT OUTER JOIN cart_product ON product_id = products_product_id
WHERE products_product_id IS NULL;

-- top 10 added in cart
SELECT product_title, COUNT(products_product_id) AS in_carts
FROM cart_product,
     products
WHERE product_id = products_product_id
GROUP BY products_product_id, product_title
ORDER BY COUNT(products_product_id) DESC
LIMIT 10;

-- top 10 added in cart & order
SELECT products.product_title, count(product_id)
        FROM products JOIN cart_product
            JOIN orders ON cart_product.carts_cart_id = orders.cart_cart_id
        ON products.product_id = products_product_id
        GROUP BY products.product_title
        ORDER BY count(cart_product.products_product_id) DESC
        LIMIT 10;

-- top 5 price
SELECT users.first_name, users.last_name, carts.total
FROM carts,
     users
WHERE users.user_id = carts.users_user_id
GROUP BY users.first_name, users.last_name, carts.total
ORDER BY carts.total DESC
LIMIT 5;

-- top 5 orders
SELECT users.first_name, users.last_name, count(carts.users_user_id) as total_orders
FROM carts,
     users
WHERE users.user_id = carts.users_user_id
GROUP BY users.first_name, users.last_name, carts.users_user_id
LIMIT 5;

-- top 5 carts but no orders
SELECT users.first_name,
        CASE
        WHEN orders.order_id IS NULL THEN 0 ELSE orders.order_id END
        FROM users JOIN carts ON users.user_id = carts.users_user_id
        LEFT OUTER JOIN orders ON carts.cart_id = orders.cart_cart_id WHERE orders.cart_cart_id IS NULL
        ORDER BY users.first_name
        LIMIT 5;