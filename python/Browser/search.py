import psycopg2
import sys
 
db_con = None
cursor= None

def searchActividad(actUser):
	try:
		#Create a database session
		print actUser;
		db_con = psycopg2.connect(database='trixdiscover1', user='trixdiscover1', password='TrixDiscover1')
		print("Connection established|")
		#Create a client cursor to execute commands
		cursor = db_con.cursor() 
		sql = "SELECT idClasificacion,nombre FROM clasificacion"
		
		# Ejecutamos el comando y buscamos dentro de la tabla Clasificacion la clasificacion que el usuario escribio
		cursor.execute("SELECT idClasificacion,nombre FROM clasificacion WHERE nombre= %s or nombre=%s",(actUser,actUser))
		# Obtenemos todos los registros en una lista de listas
		resultados = cursor.fetchall()
		for registro in resultados:
			idClasificacion = registro[0]
			nomClasificacion= registro[1]
			# Imprimimos los resultados obtenidos
			print "idClasificacion=%s, nomClasificacion=%s" % (idClasificacion,nomClasificacion)
			#despues buscamos la categoria de esa clasificacion para despues saber la actividad 
			cursor.execute("SELECT idCategoria,nombre FROM categoria WHERE idClasificacion= %s or idClasificacion=%s",(idClasificacion,idClasificacion))
			resultados2 = cursor.fetchall()
			for registro2 in resultados2:
				idCategoria = registro2[0]
				nomCategoria= registro2[1]
				# Imprimimos los resultados obtenidos
				print "idCategoria=%s, nombreCategoria=%s" % (idClasificacion,nomCategoria)
				#Ahora comparamos el id de categoria dentor de la tabla actividad
				cursor.execute("SELECT idActividad, nombre, descripcion, disponibilidad, duracion,idPrestador, costo, divisa FROM actividad WHERE idCategoria= %s or idCategoria=%s",(idCategoria,idCategoria))
				resultados3 = cursor.fetchall()
				for registro3 in resultados3:
					idActividad = registro3[0] 
					nomActividad = registro3[1] 
					descripcion = registro3[2]
					disponibilidad= registro3[3]
					duracion= registro3[4]
					idPrestador= registro3[5]
					costo= registro3[6]
					divisa= registro3[7]
					# Imprimimos los resultados obtenidos
					print "idActividad=%s, nombreActividad=%s, descripcion=%s, disponibilidad=%s, duracion=%s, idPrestador=%s, costo=%s, divisa=%s" % (idActividad,nomActividad,descripcion,disponibilidad,duracion,idPrestador,costo,divisa)
					

			

	except psycopg2.DatabaseError as e: 
		print ('Error %s' % e )
		sys.exit(1)
	finally:
		if db_con:
			db_con.close()
	return 

searchActividad("Sports")


