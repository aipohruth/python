#how to connect python to postgresql using psycopg2
import psycopg2 #importing psycopg2
import psycopg2.extras #for dictionary
#assign our parameter to a var will will later pass
hostname='localhost'
username = 'postgres'
pwd = 'blessed'
port_id = '5432'
databse = 'many'

conn = None
curr = None

try: #this error code to make us not lose our database
 conn = psycopg2.connect( #connect the psycopg2 to database
        host = hostname,
        user = username,
        password = pwd,
        dbname = databse,
        port = port_id)

 curr = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
 curr.execute('DROP TABLE IF EXISTS movie')
 create_scipt = '''CREATE TABLE movie(
                id int PRIMARY KEY,
                name VARCHAR(40),
                genre VARCHAR(10)
 );
   '''
 curr.execute(create_scipt)

 insert_script = 'INSERT INTO movie(id, name, genre) VALUES(%s, %s, %s);'
 insert_values = [(101, 'King Of Boys', 'Action'), (102, 'Banku', 'Drama'), (103, 'Ilaje', 'Play'),
                  (104, 'Glamour girls', 'Horror'), (105, 'RRR', 'Poetry')]

 for records in insert_values:

  curr.execute(insert_script, records)

  #update_script = 'UPDATE movie SET salary = salary + (salary * 0.5);'
  #curr.execute(update_script) assuming we have a salary col to increament

  delete_script = 'DELETE FROM movie WHERE id = %s'
  delete_record =(104,)
  curr.execute(delete_script, delete_record)

  curr.execute('SELECT * FROM movie')
  print(curr.fetchall()) #print to the terminal everythin in the table

  curr.execute('SELECT * FROM movie')
  for records in curr.fetchall():
   print(records[1], records[2]) #print to the terminal everythin in the table singularly 

  curr.execute('SELECT * FROM movie')
  for records in curr.fetchall():
   print(records['name'], records['genre']) #dictionary cursor


 conn.commit() #always commit to the database

 

except Exception as error:
    print(error)
if conn is None: conn.close()
if curr is None: curr.close()