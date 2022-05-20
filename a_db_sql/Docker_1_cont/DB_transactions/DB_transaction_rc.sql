BEGIN TRANSACTION ISOLATION LEVEL READ COMMITTED;

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

DELETE
FROM potential_customers
WHERE first_name = 'boris';

UPDATE potential_customers
SET first_name = 'KHIROSIMA'
WHERE last_name = 'last_name1';

ROLLBACK;
COMMIT;


BEGIN;

SELECT *
FROM order_status
ORDER BY order_status_id;

INSERT INTO order_status
VALUES (6, 'I want to play');

UPDATE order_status
SET status_name = 'I`m just playing'
WHERE status_name = 'I want to play';

DELETE
FROM order_status
WHERE status_name = 'I`m just playing';

ROLLBACK;
COMMIT;