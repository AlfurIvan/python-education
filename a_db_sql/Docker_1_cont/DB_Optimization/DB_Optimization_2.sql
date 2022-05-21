-- top 5 orders
ANALYZE users;
ANALYZE carts;
ANALYZE orders;

SET enable_seqscan TO off;
SET enable_seqscan TO on;
EXPLAIN (ANALYZE, BUFFERS) SELECT users.first_name, users.last_name, count(carts.users_user_id) as total_orders
FROM carts,
     users
WHERE users.user_id = carts.users_user_id
GROUP BY users.first_name, users.last_name, carts.users_user_id
LIMIT 5;


-- -ind
    -- Limit  (cost=188.76..188.81 rows=5 width=41) (actual time=5.257..5.262 rows=5 loops=1)
    --   Buffers: shared hit=76
    --   ->  HashAggregate  (cost=188.76..208.76 rows=2000 width=41) (actual time=5.255..5.258 rows=5 loops=1)
    -- "        Group Key: users.first_name, users.last_name, carts.users_user_id"
    --         Batches: 1  Memory Usage: 337kB
    --         Buffers: shared hit=76
    --         ->  Hash Join  (cost=128.50..168.76 rows=2000 width=33) (actual time=2.317..3.841 rows=2000 loops=1)
    --               Hash Cond: (carts.users_user_id = users.user_id)
    --               Buffers: shared hit=76
    --               ->  Seq Scan on carts  (cost=0.00..35.00 rows=2000 width=4) (actual time=0.008..0.293 rows=2000 loops=1)
    --                     Buffers: shared hit=15
    --               ->  Hash  (cost=91.00..91.00 rows=3000 width=33) (actual time=2.299..2.299 rows=3000 loops=1)
    --                     Buckets: 4096  Batches: 1  Memory Usage: 231kB
    --                     Buffers: shared hit=61
    --                     ->  Seq Scan on users  (cost=0.00..91.00 rows=3000 width=33) (actual time=0.007..1.121 rows=3000 loops=1)
    --                           Buffers: shared hit=61
    -- Planning:
    --   Buffers: shared hit=5
    -- Planning Time: 0.274 ms
    -- Execution Time: 5.324 ms

CREATE INDEX ON orders(cart_cart_id);
CREATE INDEX ON users(user_id, email, first_name, middle_name, last_name);

DROP INDEX IF EXISTS orders_cart_cart_id_idx;
DROP INDEX IF EXISTS users_user_id_email_first_name_middle_name_last_name_idx;

-- +ind
    -- Limit  (cost=188.76..188.81 rows=5 width=41) (actual time=3.263..3.267 rows=5 loops=1)
    --   Buffers: shared hit=76
    --   ->  HashAggregate  (cost=188.76..208.76 rows=2000 width=41) (actual time=3.262..3.265 rows=5 loops=1)
    -- "        Group Key: users.first_name, users.last_name, carts.users_user_id"
    --         Batches: 1  Memory Usage: 337kB
    --         Buffers: shared hit=76
    --         ->  Hash Join  (cost=128.50..168.76 rows=2000 width=33) (actual time=1.352..2.327 rows=2000 loops=1)
    --               Hash Cond: (carts.users_user_id = users.user_id)
    --               Buffers: shared hit=76
    --               ->  Seq Scan on carts  (cost=0.00..35.00 rows=2000 width=4) (actual time=0.010..0.190 rows=2000 loops=1)
    --                     Buffers: shared hit=15
    --               ->  Hash  (cost=91.00..91.00 rows=3000 width=33) (actual time=1.323..1.323 rows=3000 loops=1)
    --                     Buckets: 4096  Batches: 1  Memory Usage: 231kB
    --                     Buffers: shared hit=61
    --                     ->  Seq Scan on users  (cost=0.00..91.00 rows=3000 width=33) (actual time=0.012..0.671 rows=3000 loops=1)
    --                           Buffers: shared hit=61
    -- Planning:
    --   Buffers: shared hit=43 read=3
    -- Planning Time: 0.327 ms
    -- Execution Time: 3.307 ms

SET WORK_MEM TO '512kB';

    -- Limit  (cost=10000000354.19..10000000354.30 rows=5 width=41) (actual time=133.535..133.539 rows=5 loops=1)
    --   Buffers: shared hit=86
    --   ->  GroupAggregate  (cost=10000000354.19..10000000399.19 rows=2000 width=41) (actual time=7.541..7.544 rows=5 loops=1)
    -- "        Group Key: users.first_name, users.last_name, carts.users_user_id"
    --         Buffers: shared hit=86
    --         ->  Sort  (cost=10000000354.19..10000000359.19 rows=2000 width=33) (actual time=7.535..7.536 rows=6 loops=1)
    -- "              Sort Key: users.first_name, users.last_name, carts.users_user_id"
    --               Sort Method: quicksort  Memory: 205kB
    --               Buffers: shared hit=86
    --               ->  Hash Join  (cost=10000000060.28..10000000244.53 rows=2000 width=33) (actual time=0.427..1.448 rows=2000 loops=1)
    --                     Hash Cond: (users.user_id = carts.users_user_id)
    --                     Buffers: shared hit=86
    --                     ->  Index Scan using users_pkey on users  (cost=0.28..153.28 rows=3000 width=33) (actual time=0.013..0.459 rows=3000 loops=1)
    --                           Buffers: shared hit=71
    --                     ->  Hash  (cost=10000000035.00..10000000035.00 rows=2000 width=4) (actual time=0.409..0.409 rows=2000 loops=1)
    --                           Buckets: 2048  Batches: 1  Memory Usage: 87kB
    --                           Buffers: shared hit=15
    --                           ->  Seq Scan on carts  (cost=10000000000.00..10000000035.00 rows=2000 width=4) (actual time=0.007..0.162 rows=2000 loops=1)
    --                                 Buffers: shared hit=15
    -- Planning:
    --   Buffers: shared hit=5
    -- Planning Time: 0.607 ms
    -- JIT:
    --   Functions: 17
    -- "  Options: Inlining true, Optimization true, Expressions true, Deforming true"
    -- "  Timing: Generation 4.308 ms, Inlining 12.620 ms, Optimization 72.007 ms, Emission 41.201 ms, Total 130.137 ms"
    -- Execution Time: 137.965 ms