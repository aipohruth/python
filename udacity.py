
import psycopg2

hostname = 'localhost'
username = 'postgres'
pwd = 'blessed'
database = 'auchi'
port_id = 5432

connect = None
cursor = None
try:
    connect = psycopg2.connect(
        host = hostname,
        user = username,
        password = pwd,
        dbname = database,
        port = port_id)
 cursor = connect.cursor()
 

except Exception as error:
    print(error)
   if connect is None: connect.close()
   if cursor is None: cursor.close()
