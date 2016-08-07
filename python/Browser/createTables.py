import psycopg2
import sys
 
db_con = None
 
try:
 
	#Create a database session
	 
	db_con = psycopg2.connect(database='trixdiscover1', user='trixdiscover1', password='TrixDiscover1')
	print("Connection established|")

	#Create a client cursor to execute commands
	 
	cursor = db_con.cursor()
	cursor.execute("CREATE TABLE clasificacion (idClasificacion BIGSERIAL NOT NULL PRIMARY KEY, nombre TEXT, descripcion TEXT);")
	 
	#The variables placeholder must always be a %s, psycop2 will automatically convert the values to SQL literal
	 
	cursor.execute("INSERT INTO clasificacion (nombre,descripcion) VALUES (%s, %s)",("Sports", "lala"))
	 
	db_con.commit()
	 
	cursor.execute("SELECT * FROM clasificacion")

	print(cursor.fetchone())
 
except psycopg2.DatabaseError as e: 
 
	print ('Error %s' % e )
	 
	sys.exit(1)
	 
finally:
	 
	if db_con:
		db_con.close()