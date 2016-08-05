#!/usr/bin/python2.4
#
# Small script to show PostgreSQL and Pyscopg together
#

import psycopg2
import sys
 
db_con = None

try:
	#Create a database session
    conn = psycopg2.connect("dbname='TrixDiscover' user='trixDiscover' host='localhost' password='root'")
    print "conexion establecida"
    cur = conn.cursor()
    cur.execute("""SELECT id,password from auth_user""")
    rows = cur.fetchall()
    
    print "\nShow me the databases:\n"
    for row in rows:
    	print " ", row[0], row[1]
    print"holi"
except:
    print "I am unable to connect to the database"
