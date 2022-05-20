BEGIN ISOLATION LEVEL SERIALIZABLE;
INSERT INTO cart_product (carts_cart_id, products_product_id)
VALUES (465, 500),
       (456, 54);
SAVEPOINT set_prod;
UPDATE cart_product
SET products_product_id = '45'
WHERE carts_cart_id = '456';
DELETE
FROM cart_product
WHERE carts_cart_id = '456';
SAVEPOINT DEL;
INSERT INTO cart_product (carts_cart_id, products_product_id)
VALUES (465, 487);
SELECT *
FROM cart_product;
ROLLBACK;
COMMIT;
END;