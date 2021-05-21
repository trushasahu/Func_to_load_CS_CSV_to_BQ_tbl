##Using Composer to schedule sql queries

from airflow import DAG

from datetime import datetime, timedelta
from airflow.operators.bash_operator import BashOperator
#from airflow.operators import  PostgresOperator
#from airflow.providers.google.cloud.operators.cloud_sql import CloudSQLExecuteQueryOperator
from airflow.contrib.operators.gcp_sql_operator import CloudSqlQueryOperator

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2019, 6, 30),
    'email': ['airflow@example.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=1)
}

dag = DAG('psql-demo', catchup=False, default_args=default_args)

cloud_storage_bucket_name = 'composerdemo-bucket'

#t1 = PostgresOperator(
#    task_id='psql_insert',
#    postgres_conn_id='Postgresql_mart_conn',
#    provide_context=True,
#    sql=""" insert into data_load.item_details select item_identifier  ,item_weight,item_fat_content from data_load.bigmart_data; """,
#    dag=dag)
	
t1 = CloudSqlQueryOperator(
    task_id='psql_insert',
    gcp_cloudsql_conn_id='Postgresql_mart_conn',
    provide_context=True,
    sql=""" insert into data_load.item_details select item_identifier  ,item_weight,item_fat_content from data_load.bigmart_data; """,
    dag=dag)	


t1



----set the connection from airflow composer----

Admin-->connection-->create

conn id:  <connection id name>  e.g. Postgresql_mart_conn
Conn Type : select "Google cloud SQL" from drop down
Host  : <public id add> e.g. 35.242.162.242
Schema :<DB name>  e.g. mart
Login  :<login user> e.g. postgres
Password  : <password to connect db>
Extra  : <provide the below details>  

e.g.  {
   "database_type": "postgres",
   "project_id": "secret-cipher-303308",
   "location": "europe-west2",
   "instance": "postgresql-2",
   "use_proxy": true,
   "sql_proxy_use_tcp": false
}
