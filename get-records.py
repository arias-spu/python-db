from mysql.connector import MySQLConnection, Error
from dbconfig import readDBConfig


def fetchOne():
    try:
        # Connect to the Database
        dbconfig = readDBConfig()
        conn = MySQLConnection(**dbconfig)
        # Create a "cursor" this objects helps retrieve the rows using buffering
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM employees LIMIT 20")

        row = cursor.fetchone()

        # Retrieve each row
        while row is not None:
            print(row)
            row = cursor.fetchone()

    except Error as e:
        print(e)

    finally:
        cursor.close()
        conn.close()


if __name__ == '__main__':
    fetchOne()
