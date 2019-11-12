from mysql.connector import MySQLConnection, Error
from dbconfig import readDBConfig



def insertEmployee(empNo, birthDate, firstName, lastName, gender, hireDate):
    query = "INSERT INTO employees (emp_no, birth_date, first_name, last_name, gender, hire_date) " \
            "VALUES(%s,%s,%s,%s,%s,%s)"
    args = (empNo, birthDate, firstName, lastName, gender, hireDate)

    try:
        db_config = readDBConfig()
        conn = MySQLConnection(**db_config)

        cursor = conn.cursor()
        cursor.execute(query, args)

        conn.commit()
    except Error as error:
        print(error)

    finally:
        cursor.close()
        conn.close()

def main():
   insertEmployee('22', '1940-10-16', 'Han', 'Solo', 'M', '1985-01-01')

if __name__ == '__main__':
    main()
