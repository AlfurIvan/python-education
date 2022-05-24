-- Task 6

create or replace function b_upd_c_price()
    returns trigger
    language plpgsql
as
$$
begin
    if new.payment_for_car = old.payment_for_car or new.payment_for_car <= 0::money then
        raise exception 'Wrong data';
    end if;
    return new;
end;
$$;

create or replace function a_upd_c_price()
    returns trigger
    language plpgsql
as
$$
begin
    if new.payment_for_car <> old.payment_for_car or new.payment_for_car > 0::money then
        raise notice 'Correct data';
    end if;
    return new;
end;
$$;

-- trig before
create trigger b_upd_c_price_trig
    before update
    on model
    for each row
execute function b_upd_c_price();

-- trig after
create trigger a_upd_c_price_trig
    before update
    on model
    for each row
execute function a_upd_c_price();

update model
set payment_for_car = 250::money
where model_id = 1;


drop trigger b_upd_c_price_trig on car_rent_db_final.public.model;
drop trigger a_upd_c_price_trig on car_rent_db_final.public.model;
drop function if exists b_upd_c_price;
drop function if exists a_upd_c_price;