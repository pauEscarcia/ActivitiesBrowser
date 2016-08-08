import psycopg2
import sys
 
db_con = None
 
try:
 
	#Create a database session
	 
	db_con = psycopg2.connect(database='trixdiscover1', user='trixdiscover1', password='TrixDiscover1')
	print("Connection established|")

	#Create a client cursor to execute commands
	 
	cursor = db_con.cursor()
	#cursor.execute("CREATE TABLE clasificacion (idClasificacion BIGSERIAL NOT NULL PRIMARY KEY, nombre TEXT, descripcion TEXT);")
	#cursor.execute("CREATE TABLE categoria (idCategoria BIGSERIAL NOT NULL PRIMARY KEY, nombre TEXT, descripcion TEXT, idClasificacion BIGINT REFERENCES clasificacion(idClasificacion))")
	cursor.execute("CREATE TABLE prestador (idPrestador BIGSERIAL NOT NULL PRIMARY KEY, fecha date, nomOrganizacion TEXT,direccion TEXT, gerente TEXT, email TEXT, pagina TEXT, facebook TEXT, youtube TEXT, whatsapp TEXT, instagram TEXT, twitter TEXT, tumblr TEXT, telEmpresa TEXT, telCel Text, lat TEXT, long TEXT)") 
	#The variables placeholder must always be a %s, psycop2 will automatically convert the values to SQL literal
	 
	#cursor.execute("INSERT INTO clasificacion (nombre,descripcion) VALUES (%s, %s)",("Sports", "lala"))
	#cursor.execute("INSERT INTO categoria (nombre,descripcion,idClasificacion) VALUES (%s, %s, %s)",("hola","uno",1))
	cursor.execute("INSERT INTO prestador (fecha,nomOrganizacion,direccion,gerente,email,pagina,facebook,youtube,whatsapp,instagram,twitter,tumblr,telEmpresa,telCel,lat,long) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",('2016-07-25','Ally Cat Sailing Adventures','Calle Marina en La Cruz de Huanacaxtle','Juan Perez','allycatsailing@gmail.com','http://allycatsailing.com','facebook','youtube','whatsapp','instagram','twitter','tumblr','3221364230','23432245','207.507.862','-1.053.807.937'))
	db_con.commit()
	 
	cursor.execute("SELECT * FROM prestador")

	print(cursor.fetchone())
 
except psycopg2.DatabaseError as e: 
 
	print ('Error %s' % e )
	 
	sys.exit(1)
	 
finally:
	 
	if db_con:
		db_con.close()