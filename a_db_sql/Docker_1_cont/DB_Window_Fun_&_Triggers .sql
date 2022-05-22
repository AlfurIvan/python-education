-- TASK 1
-- Compare the price of each product n with the average
-- price of products in the category n `s product

SELECT category_title,
       product_title,
       price,
       avg(price) OVER (
           PARTITION BY p.category_id
           )
FROM products p
         LEFT JOIN categories c
                   ON p.category_id = c.category_id;

-- TASK2
---- task 2.1
-- Check if quantity of product more then 0 and return NEW or raise exception
CREATE OR REPLACE FUNCTION analyze_new_pot_user()
    RETURNS TRIGGER
AS
$$
BEGIN
    IF NEW.email IS NULL OR NEW.city IS NULL OR NEW.last_name IS NULL THEN
        RAISE EXCEPTION 'Null value in email, city or last name(';
    ELSEIF NEW IN (SELECT * FROM potential_customers) THEN
        RAISE EXCEPTION 'This potential user are already in table!';
    END IF;
end;
$$ LANGUAGE plpgsql;

-- Works for updating or inserting into the table cart_product
CREATE TRIGGER new_potential_user
    BEFORE INSERT
    ON potential_customers
    FOR EACH ROW
EXECUTE FUNCTION analyze_new_pot_user();

INSERT INTO potential_customers (first_name, last_name, middle_name, email, city)
VALUES ('eduard', 'mikhyilov', 'eduardovich', 'edic_no_pe@xhmail.com', 'uryupinsk');


SELECT *
FROM potential_customers
WHERE potential_user_id > 24;

DELETE
FROM potential_customers
WHERE potential_user_id > 25;

INSERT INTO potential_customers (first_name, last_name, middle_name, email, city)
VALUES ('eduard', 'mikhyilov', 'eduardovich', NULL, 'uryupinsk');
INSERT INTO potential_customers (first_name, last_name, middle_name, email, city)
VALUES ('eduard', 'mikhyilov', 'eduardovich', 'edic_no_pe@xhmail.com', NULL);
INSERT INTO potential_customers (first_name, last_name, middle_name, email, city)
VALUES ('eduard', NULL, 'eduardovich', 'edic_no_pe@xhmail.com', 'uryupinsk');


CREATE OR REPLACE FUNCTION analyze_upd_pot_user()
    RETURNS TRIGGER
AS
$$
BEGIN
    IF NEW = OLD THEN
        RAISE NOTICE 'SAME TO CONTAINS';
    end if;
end;
$$ LANGUAGE plpgsql;

-- Works for updating potential_users
CREATE TRIGGER new_potential_user
    BEFORE INSERT
    ON potential_customers
    FOR EACH ROW
EXECUTE FUNCTION analyze_upd_pot_user();

SELECT *
FROM potential_customers
WHERE potential_user_id > 24;

DELETE
FROM potential_customers
WHERE potential_user_id > 25;


UPDATE potential_customers
SET email ='edic_no_pe@xhmail.com'
WHERE potential_user_id = 25;
UPDATE potential_customers
SET email ='edic_no_pe@xhmail.com'
WHERE potential_user_id = 3444;