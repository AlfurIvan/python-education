ANALYSE products;
ANALYSE cart_product;

EXPLAIN (ANALYSE ,BUFFERS )
SELECT product_title
FROM products
         LEFT OUTER JOIN cart_product ON product_id = products_product_id
WHERE products_product_id IS NULL;
SET enable_seqscan TO off;
SET enable_seqscan TO on;

-- no ind, seqs off
    -- Hash Anti Join  (cost=486.55..898.73 rows=258 width=12) (actual time=3.441..5.818 rows=258 loops=1)
    --   Hash Cond: (products.product_id = cart_product.products_product_id)
    -- "  Buffers: shared hit=115, temp read=27 written=27"
    --   ->  Index Scan using products_pkey on products  (cost=0.28..293.45 rows=4000 width=16) (actual time=0.005..0.765 rows=4000 loops=1)
    --         Buffers: shared hit=79
    --   ->  Hash  (cost=305.84..305.84 rows=10995 width=4) (actual time=3.340..3.340 rows=10995 loops=1)
    --         Buckets: 16384  Batches: 2  Memory Usage: 318kB
    -- "        Buffers: shared hit=36, temp written=16"
    --         ->  Index Only Scan using cart_product_carts_cart_id_products_product_id_idx2 on cart_product  (cost=0.29..305.84 rows=10995 width=4) (actual time=0.013..1.446 rows=10995 loops=1)
    --               Heap Fetches: 599
    --               Buffers: shared hit=36
    -- Planning:
    --   Buffers: shared hit=18
    -- Planning Time: 0.142 ms
    -- Execution Time: 5.852 ms

-- no ind, seqs off
    -- Hash Anti Join  (cost=339.39..603.39 rows=258 width=12) (actual time=3.552..6.375 rows=258 loops=1)
    --   Hash Cond: (products.product_id = cart_product.products_product_id)
    -- "  Buffers: shared hit=154, temp read=27 written=27"
    --   ->  Seq Scan on products  (cost=0.00..145.00 rows=4000 width=16) (actual time=0.008..0.700 rows=4000 loops=1)
    --         Buffers: shared hit=105
    --   ->  Hash  (cost=158.95..158.95 rows=10995 width=4) (actual time=3.490..3.491 rows=10995 loops=1)
    --         Buckets: 16384  Batches: 2  Memory Usage: 318kB
    -- "        Buffers: shared hit=49, temp written=16"
    --         ->  Seq Scan on cart_product  (cost=0.00..158.95 rows=10995 width=4) (actual time=0.003..1.253 rows=10995 loops=1)
    --               Buffers: shared hit=49
    -- Planning:
    --   Buffers: shared hit=22
    -- Planning Time: 0.188 ms
    -- Execution Time: 6.413 ms

CREATE INDEX ON products(product_id);
CREATE INDEX ON cart_product(products_product_id);

-- + ind, seqs off
    -- Merge Anti Join  (cost=0.57..662.10 rows=258 width=12) (actual time=0.036..3.944 rows=258 loops=1)
    --   Merge Cond: (products.product_id = cart_product.products_product_id)
    --   Buffers: shared hit=457 read=28
    --   ->  Index Scan using products_product_id_idx on products  (cost=0.28..245.45 rows=4000 width=16) (actual time=0.007..0.915 rows=4000 loops=1)
    --         Buffers: shared hit=58 read=9
    --   ->  Index Only Scan using cart_product_products_product_id_idx on cart_product  (cost=0.29..269.21 rows=10995 width=4) (actual time=0.010..1.583 rows=10994 loops=1)
    --         Heap Fetches: 599
    --         Buffers: shared hit=399 read=19
    -- Planning:
    --   Buffers: shared hit=28 read=8
    -- Planning Time: 0.379 ms
    -- Execution Time: 3.980 ms

-- + ind, seqs on
    -- Hash Anti Join  (cost=339.39..603.39 rows=258 width=12) (actual time=4.962..8.882 rows=258 loops=1)
    --   Hash Cond: (products.product_id = cart_product.products_product_id)
    -- "  Buffers: shared hit=154, temp read=27 written=27"
    --   ->  Seq Scan on products  (cost=0.00..145.00 rows=4000 width=16) (actual time=0.009..0.866 rows=4000 loops=1)
    --         Buffers: shared hit=105
    --   ->  Hash  (cost=158.95..158.95 rows=10995 width=4) (actual time=4.888..4.890 rows=10995 loops=1)
    --         Buckets: 16384  Batches: 2  Memory Usage: 318kB
    -- "        Buffers: shared hit=49, temp written=16"
    --         ->  Seq Scan on cart_product  (cost=0.00..158.95 rows=10995 width=4) (actual time=0.005..1.714 rows=10995 loops=1)
    --               Buffers: shared hit=49
    -- Planning:
    --   Buffers: shared hit=28 read=8
    -- Planning Time: 0.599 ms
    -- Execution Time: 8.942 ms

DROP INDEX cart_product_carts_cart_id_products_product_id_idx1;
DROP INDEX cart_product_carts_cart_id_products_product_id_idx2;
