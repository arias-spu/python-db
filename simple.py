# Import the functions to connect to the server
import mysql.connector
from mysql.connector import Error

# Define a function to connect to the database (just the test)
def connect():
	conn = None
	try:
        # This is the function call that actually connects to the database
        conn = mysql.connector.connect(host='yourhost', database='employees', user='youruser', password='yourpassword')
		if conn.is_connected():
			print('Connected!')
	except Error as e:
		print(e)
	finally:
		if conn is not None and conn.is_connected():
			conn.close()

# Calling the function connect to see that everything is working
# If the program outputs Connected then you're ready!
connect()
