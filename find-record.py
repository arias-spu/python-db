from mysql.connector import MySQLConnection, Error
from dbconfig import readDBConfig


def findEmployee(id):
    try:
        # Connect to the Database
        dbconfig = readDBConfig()
        conn = MySQLConnection(**dbconfig)
        # Create a "cursor" this objects helps retrieve the rows using buffering
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM employees WHERE emp_no = " + id)
        row = cursor.fetchone()
        return row


    except Error as e:
        print(e)

    finally:
        cursor.close()
        conn.close()


if __name__ == '__main__':
    id = raw_input("Enter the ID of the employee you want to find: ")
    employee = findEmployee(id)
    if employee is None:
        print("Not Found")
    else:
        print(employee)
