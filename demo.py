from sqlite3 import connect
import psycopg2

hostname = 'localhost'
username = 'postgres'
database = 'class_room'
pwd = 'blessed'
port_id = '5432'

conn = None
cur = None

try :
 conn = psycopg2.connect(
            host = hostname,
            dbname = database,
            user = username,
            password = pwd,
            port = port_id)
 cur = conn.cursor()
 cur.execute('DROP TABLE IF EXISTS staffs')
 create_script = '''
        CREATE TABLE IF NOT EXISTS staffs(
            id int PRIMARY KEY,
            name VARCHAR(40) NOT NULL,
            age int,
            salary int
        );
 '''
 cur.execute(create_script)

 insert_script = 'INSERT INTO staffs(id, name, age, salary) VALUES(%s, %s, %s, %s);'
 insert_values = [(2, 'Juliet', 43, 3500), (3, 'Alloy', 21, 1200)]
 for records in insert_values:
  cur.execute(insert_script, records)
 conn.commit()
 

 

except Exception as error:
    print(error)
finally:
    if cur is not None:
        cur.close()
    if conn is not None:
        conn.close()
