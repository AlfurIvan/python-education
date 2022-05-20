BEGIN TRANSACTION ISOLATION LEVEL REPEATABLE READ;

INSERT INTO order_status(order_status_id, status_name)
VALUES (6, 'KHIROSIMA');
UPDATE order_status
SET status_name='KHIROSIMA'
WHERE order_status_id = 6;
DELETE
FROM order_status
WHERE order_status_id = 6;

ROLLBACK;
COMMIT;


BEGIN TRANSACTION ISOLATION LEVEL REPEATABLE READ;

SELECT *
FROM potential_customers
ORDER BY potential_user_id DESC;
INSERT INTO potential_customers(first_name,
                                last_name,
                                middle_name,
                                email,
                                city)
VALUES ('boris',
        'boris',
        'borisovich',
        'borya1337@chmail.com',
        'Mukhosransk');
UPDATE potential_customers
SET city='NOMukhosransk'
WHERE first_name = 'boris';
ROLLBACK;
DELETE
FROM potential_customers
WHERE city = 'NOMukhosransk';

COMMIT;
