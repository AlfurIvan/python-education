----Task 4 functions

-- returns table witch contains info about current rent
create or replace function get_cust_rent_price(id int)
    returns table
            (
                customer_id   int,
                first_name    varchar,
                last_name     varchar,
                rental_id     int,
                car_no        int,
                rental_date   timestamp,
                rental_period int,
                price         money
            )
    language plpgsql
as
$$
begin
    return query
        select c.customer_id,
               c.first_name,
               c.last_name,
               r.rental_id,
               r.car_no,
               r.rental_date,
               r.rental_period,
               p.price
        from customer c
                 join rental r on c.customer_id = r.customer_id and r.rental_id = id
                 join payment p on r.rental_id = p.payment_id and p.payment_id = id;
end;
$$;
select *
from get_cust_rent_price(188);
DROP FUNCTION get_cust_rent_price(integer);


---return rents sum
create or replace function rent_sum(cust_id int)
    returns integer
    language plpgsql
as
$$
declare
    id  record;
    sum money;
begin
    for id in (select customer_id, price
               from rental r
                        join car on car.car_id = r.car_no
                        join payment p on r.rental_id = p.payment_id
               where customer_id = cust_id)
        loop
            sum = sum + id.price;
        end loop;
    return sum;
end;
$$;

select *
from rent_sum(118);
drop function rent_sum;


--
create or replace function cust_rents(cust_id int)
    returns text
    language plpgsql as
$$
declare
    cust_r_id int = 0; -- zero, start
    record    record;
    cursor_ cursor (f_id int) for select c.customer_id
                                  from customer c
                                           left join rental r on c.customer_id = r.customer_id
                                  where c.customer_id = cust_id; -- cursor
begin
    open cursor_(cust_id);
    loop
        fetch cursor_ into record;
        exit when not found;
        cust_r_id = cust_r_id + 1;
    end loop;
    close cursor_;
    return cust_r_id;
end;
$$;
-- check result
select *
from get_all_rent_customer(customers_id := 4)