#############requirements.txt################

# This file tells Python which modules it needs to import
#############requirement.txt######### in cloud function
SQLAlchemy==1.3.12      
# If your database is MySQL, uncomment the following line:
#PyMySQL==0.9.3
# If your database is PostgreSQL, uncomment the following line:
pg8000==1.13.2

	
############main.py################   in cloud function

# This file contains all the code used in the codelab. 
import sqlalchemy

# Depending on which database you are using, you'll set some variables differently. 
# In this code we are inserting only one field with one value. 
# Feel free to change the insert statement as needed for your own table's requirements.

# Uncomment and set the following variables depending on your specific instance and database:
connection_name = "secret-cipher-303308:asia-south1:postgresql-1"
#table_name = ""
#table_field = ""
#table_field_value = ""
db_name = "mart"
db_user = "postgres"
db_password = "newpass1"

# If your database is MySQL, uncomment the following two lines:
#driver_name = 'mysql+pymysql'
#query_string = dict({"unix_socket": "/cloudsql/{}".format(connection_name)})

# If your database is PostgreSQL, uncomment the following two lines:
driver_name = 'postgres+pg8000'
query_string =  dict({"unix_sock": "/cloudsql/{}/.s.PGSQL.5432".format(connection_name)})

# If the type of your table_field value is a string, surround it with double quotes.

def insert(request):
    request_json = request.get_json()
    stmt = sqlalchemy.text('insert into data_load.item_details select item_identifier  ,item_weight,item_fat_content from data_load.bigmart_data')
    
    db = sqlalchemy.create_engine(
      sqlalchemy.engine.url.URL(
        drivername=driver_name,
        username=db_user,
        password=db_password,
        database=db_name,
        query=query_string,
      ),
      pool_size=5,
      max_overflow=2,
      pool_timeout=30,
      pool_recycle=1800
    )
    try:
        with db.connect() as conn:
            conn.execute(stmt)
    except Exception as e:
        return 'Error: {}'.format(str(e))
    return 'ok'