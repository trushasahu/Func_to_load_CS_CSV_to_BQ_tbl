create or replace procedure load_item_data_wop()
as $$
begin
    insert into data_load.item_details select item_identifier  ,item_weight,item_fat_content from data_load.bigmart_data;
end;
$$
language plpgsql;



#!/bin/sh
DATABASE=mart
USERNAME=postgres
HOSTNAME=127.0.0.1
export PGPASSWORD=newpass1

psql -h $HOSTNAME -U $USERNAME $DATABASE << EOF
call data_load.load_item_data(0);
EOF



create or replace procedure load_item_data(inout v_out integer)
as $$
begin
	v_out = 0;	
    insert into data_load.item_details select item_identifier  ,item_weight,item_fat_content from data_load.bigmart_data;
    return;
exception 
	when others then
	v_out = 1;
	rollback;
	raise notice '% %', SQLERRM, SQLSTATE;
	return;
end;
$$
language plpgsql;


#!/bin/sh
DATABASE=mart
USERNAME=postgres
HOSTNAME=127.0.0.1
export PGPASSWORD=newpass1

x=`psql -h $HOSTNAME -U $USERNAME $DATABASE << EOF
call data_load.load_item_data(0);
EOF`

echo "Return Value : ${x}"
y=`echo $x|awk -F' ' '{print $3}'`

if [ ${y} = 0 ]; then
        echo "Yes"
else echo "No"
fi


