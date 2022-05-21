ANALYZE products;
ANALYZE orders;
ANALYZE cart_product;

-- Opt1 top 10 added in cart
SET enable_seqscan TO off;
SET enable_seqscan TO on;
EXPLAIN (ANALYZE, BUFFERS)
SELECT product_title, COUNT(products_product_id) AS in_carts
FROM cart_product,
     products
WHERE product_id = products_product_id
GROUP BY products_product_id, product_title
ORDER BY COUNT(products_product_id) DESC
LIMIT 10;
-- seqscan off no ind
    -- Limit  (cost=1108.19..1108.22 rows=10 width=24) (actual time=12.960..12.965 rows=10 loops=1)
    --   Buffers: shared hit=115
    --   ->  Sort  (cost=1108.19..1135.68 rows=10995 width=24) (actual time=12.959..12.962 rows=10 loops=1)
    --         Sort Key: (count(cart_product.products_product_id)) DESC
    --         Sort Method: top-N heapsort  Memory: 26kB
    --         Buffers: shared hit=115
    --         ->  HashAggregate  (cost=760.65..870.60 rows=10995 width=24) (actual time=11.662..12.375 rows=3742 loops=1)
    -- "              Group Key: cart_product.products_product_id, products.product_title"
    --               Batches: 1  Memory Usage: 913kB
    --               Buffers: shared hit=115
    --               ->  Hash Join  (cost=343.74..678.18 rows=10995 width=16) (actual time=1.898..7.171 rows=10995 loops=1)
    --                     Hash Cond: (cart_product.products_product_id = products.product_id)
    --                     Buffers: shared hit=115
    --                     ->  Index Only Scan using cart_product_carts_cart_id_products_product_id_idx1 on cart_product  (cost=0.29..305.84 rows=10995 width=4) (actual time=0.017..1.600 rows=10995 loops=1)
    --                           Heap Fetches: 599
    --                           Buffers: shared hit=36
    --                     ->  Hash  (cost=293.45..293.45 rows=4000 width=16) (actual time=1.851..1.852 rows=4000 loops=1)
    --                           Buckets: 4096  Batches: 1  Memory Usage: 232kB
    --                           Buffers: shared hit=79
    --                           ->  Index Scan using products_pkey on products  (cost=0.28..293.45 rows=4000 width=16) (actual time=0.006..0.986 rows=4000 loops=1)
    --                                 Buffers: shared hit=79
    -- Planning:
    --   Buffers: shared hit=20
    -- Planning Time: 0.229 ms
    -- Execution Time: 13.032 ms

CREATE INDEX ON cart_product (carts_cart_id, products_product_id);
CREATE INDEX ON orders (cart_cart_id, order_status_order_status_id);

DROP INDEX IF EXISTS orders_cart_cart_id_order_status_order_status_id_idx;
DROP INDEX IF EXISTS cart_product_carts_cart_id_products_product_id_idx;

    -- Limit  (cost=812.86..812.88 rows=10 width=24) (actual time=13.642..13.646 rows=10 loops=1)
    --   Buffers: shared hit=154
    --   ->  Sort  (cost=812.86..840.34 rows=10995 width=24) (actual time=13.641..13.643 rows=10 loops=1)
    --         Sort Key: (count(cart_product.products_product_id)) DESC
    --         Sort Method: top-N heapsort  Memory: 26kB
    --         Buffers: shared hit=154
    --         ->  HashAggregate  (cost=465.31..575.26 rows=10995 width=24) (actual time=12.197..13.023 rows=3742 loops=1)
    -- "              Group Key: cart_product.products_product_id, products.product_title"
    --               Batches: 1  Memory Usage: 913kB
    --               Buffers: shared hit=154
    --               ->  Hash Join  (cost=195.00..382.85 rows=10995 width=16) (actual time=1.482..7.311 rows=10995 loops=1)
    --                     Hash Cond: (cart_product.products_product_id = products.product_id)
    --                     Buffers: shared hit=154
    --                     ->  Seq Scan on cart_product  (cost=0.00..158.95 rows=10995 width=4) (actual time=0.005..1.220 rows=10995 loops=1)
    --                           Buffers: shared hit=49
    --                     ->  Hash  (cost=145.00..145.00 rows=4000 width=16) (actual time=1.471..1.471 rows=4000 loops=1)
    --                           Buckets: 4096  Batches: 1  Memory Usage: 232kB
    --                           Buffers: shared hit=105
    --                           ->  Seq Scan on products  (cost=0.00..145.00 rows=4000 width=16) (actual time=0.003..0.693 rows=4000 loops=1)
    --                                 Buffers: shared hit=105
    -- Planning:
    --   Buffers: shared hit=6
    -- Planning Time: 0.196 ms
    -- Execution Time: 13.719 ms

SET WORK_MEM  TO '512kB'
-- +ind
    -- Limit  (cost=1873.70..1873.72 rows=10 width=24) (actual time=21.631..21.636 rows=10 loops=1)
    -- "  Buffers: shared hit=115, temp read=40 written=40"
    --   ->  Sort  (cost=1873.70..1901.18 rows=10995 width=24) (actual time=21.630..21.633 rows=10 loops=1)
    --         Sort Key: (count(cart_product.products_product_id)) DESC
    --         Sort Method: top-N heapsort  Memory: 26kB
    -- "        Buffers: shared hit=115, temp read=40 written=40"
    --         ->  GroupAggregate  (cost=1416.20..1636.10 rows=10995 width=24) (actual time=14.223..20.706 rows=3742 loops=1)
    -- "              Group Key: cart_product.products_product_id, products.product_title"
    -- "              Buffers: shared hit=115, temp read=40 written=40"
    --               ->  Sort  (cost=1416.20..1443.69 rows=10995 width=16) (actual time=14.210..16.216 rows=10995 loops=1)
    -- "                    Sort Key: cart_product.products_product_id, products.product_title"
    --                     Sort Method: external merge  Disk: 320kB
    -- "                    Buffers: shared hit=115, temp read=40 written=40"
    --                     ->  Hash Join  (cost=343.74..678.18 rows=10995 width=16) (actual time=2.334..8.110 rows=10995 loops=1)
    --                           Hash Cond: (cart_product.products_product_id = products.product_id)
    --                           Buffers: shared hit=115
    --                           ->  Index Only Scan using cart_product_carts_cart_id_products_product_id_idx2 on cart_product  (cost=0.29..305.84 rows=10995 width=4) (actual time=0.015..2.002 rows=10995 loops=1)
    --                                 Heap Fetches: 599
    --                                 Buffers: shared hit=36
    --                           ->  Hash  (cost=293.45..293.45 rows=4000 width=16) (actual time=2.311..2.312 rows=4000 loops=1)
    --                                 Buckets: 4096  Batches: 1  Memory Usage: 232kB
    --                                 Buffers: shared hit=79
    --                                 ->  Index Scan using products_pkey on products  (cost=0.28..293.45 rows=4000 width=16) (actual time=0.006..1.324 rows=4000 loops=1)
    --                                       Buffers: shared hit=79
    -- Planning:
    --   Buffers: shared hit=27
    -- Planning Time: 0.311 ms
    -- Execution Time: 21.807 ms

-- -ind
    -- Limit  (cost=1578.36..1578.38 rows=10 width=24) (actual time=14.266..14.270 rows=10 loops=1)
    -- "  Buffers: shared hit=154, temp read=41 written=43"
    --   ->  Sort  (cost=1578.36..1605.85 rows=10995 width=24) (actual time=14.264..14.267 rows=10 loops=1)
    --         Sort Key: (count(cart_product.products_product_id)) DESC
    --         Sort Method: top-N heapsort  Memory: 26kB
    -- "        Buffers: shared hit=154, temp read=41 written=43"
    --         ->  GroupAggregate  (cost=1120.86..1340.76 rows=10995 width=24) (actual time=9.017..13.700 rows=3742 loops=1)
    -- "              Group Key: cart_product.products_product_id, products.product_title"
    -- "              Buffers: shared hit=154, temp read=41 written=43"
    --               ->  Sort  (cost=1120.86..1148.35 rows=10995 width=16) (actual time=9.008..10.545 rows=10995 loops=1)
    -- "                    Sort Key: cart_product.products_product_id, products.product_title"
    --                     Sort Method: external merge  Disk: 328kB
    -- "                    Buffers: shared hit=154, temp read=41 written=43"
    --                     ->  Hash Join  (cost=195.00..382.85 rows=10995 width=16) (actual time=1.106..5.142 rows=10995 loops=1)
    --                           Hash Cond: (cart_product.products_product_id = products.product_id)
    --                           Buffers: shared hit=154
    --                           ->  Seq Scan on cart_product  (cost=0.00..158.95 rows=10995 width=4) (actual time=0.004..0.795 rows=10995 loops=1)
    --                                 Buffers: shared hit=49
    --                           ->  Hash  (cost=145.00..145.00 rows=4000 width=16) (actual time=1.096..1.097 rows=4000 loops=1)
    --                                 Buckets: 4096  Batches: 1  Memory Usage: 232kB
    --                                 Buffers: shared hit=105
    --                                 ->  Seq Scan on products  (cost=0.00..145.00 rows=4000 width=16) (actual time=0.003..0.499 rows=4000 loops=1)
    --                                       Buffers: shared hit=105
    -- Planning:
    --   Buffers: shared hit=19
    -- Planning Time: 0.183 ms
    -- Execution Time: 14.424 ms