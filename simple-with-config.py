# From: http://www.mysqltutorial.org/python-connecting-mysql-databases/

from mysql.connector import MySQLConnection, Error
from dbconfig import readDBConfig


def connect():
    """ Connect to MySQL database """

    db_config = readDBConfig()
    conn = None
    try:
        print('Connecting to MySQL database...')
        conn = MySQLConnection(**db_config)

        if conn.is_connected():
            print('Connection established.')
        else:
            print('Connection failed.')

    except Error as error:
        print(error)

    finally:
        if conn is not None and conn.is_connected():
            conn.close()
            print('Connection closed.')


if __name__ == '__main__':
    connect()
