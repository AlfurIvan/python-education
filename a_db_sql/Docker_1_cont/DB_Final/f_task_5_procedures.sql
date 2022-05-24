-- Task5 Procedures

--proc to change payment for model
create or replace procedure change_car_fee(id int, new_fee money)
    language plpgsql
as
$$
declare
    old_fee money;
begin
    select payment_for_car into old_fee from model where model_id = id;
    update model
    set payment_for_car = new_fee
    where model_id = id;
    if new_fee > 0::money and new_fee != old_fee then
        commit;
    else
        rollback;
    end if;
end;
$$;

call change_car_fee(12, 2::money);
select *
from model
where model_id = 12;



-- proc
create or replace procedure add_new_car(mod_id int, man_id int, mod_name varchar, fee money, num_car varchar)
    language plpgsql
as
$$
begin
    If man_id NOT In (1,2,3) then
        raise notice 'no such manufacturer';
        rollback;
    end if;
    If mod_id <= 15 then
        raise notice 'override';
        rollback;
    end if;

    insert into model(model_id,manufacturer_id, model_name, payment_for_car)
    values (mod_id, man_id, mod_name, fee);
    insert into car(car_id, model_id, car_no)
    values (mod_id, mod_id, num_car);

end;
$$;
-- check result
call add_new_car(16, 1, 'Model 1 X', 237::money, '13455');
select *
from model
where model_id = 16;
drop procedure if exists add_new_car(mod_id int, man_id int, mod_name varchar, fee money, num_car varchar);