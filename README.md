# Connecting Python Program to MySQL


## Requirements
You will need to install the MySQL Connector for Python:
This [Tutorial](http://www.mysqltutorial.org/getting-started-mysql-python-connector/) is the easiest way to connect to a remote database. There are other choices, but they **assume** that you have a local database.

In general to connect to a database you need
- A database available, you will need to know:
  - The host, the address of the database
  - The user, a user to access the database
  - The password, the password for that user
  - The database, the specific database on the server that you want to access
- A connector, this is usually a library that brings the functions/modules/code necessary to connect to the specific database. This connector is specific for the programming language or tool you are using. For an overview on connectors see [MySQL Connectors](https://www.mysql.com/products/connector/)
- Your programming language or tool. In this particular example the programming language is Python.

For the specific purpose of this program you will need:
- Install [pip](https://pip.pypa.io/en/stable/installing/)
- Install the Python MySQL Connector
  - `pip install mysql-connector-python`

Optionally you can try to get all the requirements: `pip install -r requirements.txt`, it is possible that you will need to do: `sudo pip install -r requirements.txt`

## Config.ini
You will need to setup a file named `config.ini` this file is not provided in this repo.
The file should look like this:
```
[mysql]
host = yourhost
database = yourdatabase
user = youruser
password = thepasswordforthatuser
```

## About the code

- `simple.py` shows a simple way to test the connection to the database
- `dbconfig.py` shows a program to read the configuration file `config.ini`
- `simple-with-config.py` uses the `dbconfig.py` module to read the configuration file and tests the connection.
- `get-records.py` shows an example of retrieving and displaying the records of a table using a `SELECT` statement. Check the [original tutorial](http://www.mysqltutorial.org/python-mysql-query/) to see other ways to retrieve the records (`fetchall`, `fetchmany`).
- `find-record.py` asks the user for an ID and finds the employee with that ID
- `insert-record.py` inserts a record into the employee table. Notice that the ID is fixed, so you may need to change it to work for you. You may use numbers greater than 600010.
