CREATE TABLE users
(
    user_id     serial primary key,
    email       varchar(255),
    password    varchar(255),
    first_name  varchar(255),
    last_name   varchar(255),
    middle_name varchar(255),
    is_staff    int,
    country     varchar(255),
    city        varchar(255),
    address     text
);

CREATE TABLE carts
(
    cart_id       serial primary key,
    users_user_id int references users (user_id),
    subtotal      decimal,
    total         decimal,
    timestamp     timestamp(2)
);

CREATE TABLE cart_product
(
    carts_cart_id       int references carts (cart_id),
    products_product_id int references products (product_id)
);

CREATE TABLE products
(
    product_id          serial primary key,
    product_title       varchar(255),
    product_description text,
    in_stock            int,
    price               float,
    slug                varchar(45),
    category_id         int references categories (category_id)
);

CREATE TABLE categories
(
    category_id          serial primary key,
    category_title       varchar(255),
    category_description text
);

CREATE TABLE orders
(
    order_id                     serial primary key,
    cart_cart_id                 int references carts (cart_id),
    order_status_order_status_id int references order_status (order_status_id),
    shipping_total               decimal,
    total                        decimal,
    created_at                   timestamp(2),
    updated_at                   timestamp(2)
);

CREATE TABLE order_status
(
    order_status_id serial primary key,
    status_name     varchar(255)
);

DROP TABLE users CASCADE;
DROP TABLE carts;
DROP TABLE categories;
DROP TABLE cart_product;
DROP TABLE order_status;
DROP TABLE orders CASCADE;
DROP TABLE products;

COPY users FROM '/usr/src/users.csv' WITH (format csv);
COPY products FROM '/usr/src/products.csv' WITH (format csv);
COPY categories FROM '/usr/src/categories.csv' WITH (format csv);
COPY order_status FROM '/usr/src/order_status.csv' WITH (format csv);
COPY carts FROM '/usr/src/carts.csv' WITH (format csv);
COPY orders FROM '/usr/src/orders.csv' WITH (format csv);
COPY cart_product FROM '/usr/src/cart_product.csv' WITH (format csv);

ALTER TABLE users
    ADD COLUMN phone_number int;

ALTER TABLE users
    ALTER COLUMN phone_number TYPE varchar(255);

UPDATE products
SET price = price * 2;