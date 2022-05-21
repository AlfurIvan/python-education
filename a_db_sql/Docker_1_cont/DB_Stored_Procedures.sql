-- TASK1 Function to make shipping_total = 0 where argument city = x

CREATE OR REPLACE FUNCTION set_shipping_total(x VARCHAR(255))
    RETURNS INT
    LANGUAGE plpgsql
AS
$$
DECLARE
    orders_total_E INT;
    re             RECORD;
BEGIN
    FOR re IN (SELECT * FROM order_view)
        LOOP
            IF re.city = x
            THEN
                UPDATE orders
                SET shipping_total = 0
                WHERE order_id = re.order_id;
            END IF;
        END LOOP;

    SELECT SUM(shipping_total)
    INTO orders_total_E
    FROM orders;
    RETURN orders_total_E;
END;
$$;

CREATE OR REPLACE VIEW order_view AS
SELECT city, o.order_id, o.shipping_total
FROM users
         INNER JOIN carts c
                    ON users.user_id = c.users_user_id
         INNER JOIN orders o
                    ON c.cart_id = o.cart_cart_id;

DROP VIEW order_view;

SELECT SUM(shipping_total)
FROM orders;

SELECT set_shipping_total('city 5');


-- TASK2
--task 2.1 seller

CALL release(what_product := 3, how_much := 5);
DROP PROCEDURE release(id_product INT, count_product INT);
SELECT *
FROM products
WHERE product_id = 3;

CREATE OR REPLACE PROCEDURE release(what_product INT, how_much INT)
    LANGUAGE plpgsql
AS
$$
DECLARE
    product_stock INT = NULL;
    new_amount    INT = NULL;
BEGIN
    SELECT in_stock
    INTO product_stock
    FROM products
    WHERE product_id = what_product;

    IF product_stock IS NULL THEN -- This is product?
        RAISE EXCEPTION 'Not found';
    END IF;

    UPDATE products-- amount -= ...
    SET in_stock = in_stock - how_much
    WHERE product_id = what_product;

    SELECT in_stock -- new am
    INTO new_amount
    FROM products
    WHERE product_id = what_product;

    IF new_amount >= 0 THEN -- too much or not too much
        COMMIT ;
    ELSE
        ROLLBACK ;
    END IF;
    IF new_amount < 0 THEN
        RAISE 'Not enough items';
    END IF;
END;
$$;


-- task 2.2 updater proc

DROP procedure if exists update_order_status(ord_id orders.order_id%type);
CALL update_order_status(1);

CREATE OR REPLACE PROCEDURE update_order_status(
    ord_id orders.order_id%TYPE
)
    language plpgsql
AS
$$
DECLARE
    curr_stat_id orders.order_status_order_status_id%TYPE;
BEGIN
    -- Curr stat is?
    SELECT order_status_order_status_id
    INTO curr_stat_id
    FROM orders
    WHERE order_id = ord_id;

    -- Status check
    IF curr_stat_id = 0 THEN
        UPDATE orders
        SET order_status_order_status_id = 5,
            updated_at                   = date(now())
        WHERE order_id = ord_id;
        COMMIT;
    ELSEIF curr_stat_id = 5 THEN
        RAISE EXCEPTION 'Cannot update closed order';
    ELSEIF curr_stat_id = 4 THEN
        RAISE EXCEPTION 'Cannot update finished order';
    ELSE
        UPDATE orders
        SET order_status_order_status_id = curr_stat_id + 1,
            updated_at                   = date(now())
        WHERE order_id = ord_id;
        COMMIT;
    END IF;

END
$$;

-- task 2.3 WEEEE renamer

DROP PROCEDURE IF EXISTS change_last_name(f_user_id INT,
                                             n_f_name VARCHAR(255),
                                             n_l_name VARCHAR(255),
                                             n_m_name VARCHAR(255));
CALL change_last_name(f_user_id := '1', n_f_name := 'gleb',n_l_name := 'glebovich',n_m_name := 'glebov');
SELECT first_name, last_name, middle_name
FROM users
WHERE first_name = 'gleb';

CREATE OR REPLACE PROCEDURE change_last_name(f_user_id INT,
                                             n_f_name VARCHAR(255),
                                             n_l_name VARCHAR(255),
                                             n_m_name VARCHAR(255))
    LANGUAGE plpgsql
AS
$$
DECLARE
    prev_f_n VARCHAR(255);
    prev_l_n VARCHAR(255);
    prev_m_n VARCHAR(255);
BEGIN
    -- get user password --
    SELECT first_name, last_name, middle_name
    INTO prev_f_n, prev_l_n, prev_m_n
    FROM users
    WHERE user_id = f_user_id;

    -- check new password --
    IF prev_f_n = n_f_name THEN
        RAISE 'First names are same';
    ELSEIF prev_l_n = n_l_name THEN
        RAISE 'Last names are same';
    ELSEIF prev_m_n = n_m_name THEN
        RAISE 'Middle names are same';
    end if;

    UPDATE users
    SET first_name = n_f_name, last_name = n_l_name, middle_name = n_m_name
    WHERE user_id = f_user_id;
END;
$$;
