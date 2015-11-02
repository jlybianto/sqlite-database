# The sqlite3 model is used to work with the SQLite database.
# The pandas package is used to fetch and store data in a DataFrame.
import sqlite3 as lite
import pandas as pd

# Data to be inserted through the use of tuples.
cities = (
	('New York City', 'NY'),
	('Boston', 'MA'),
	('Chicago', 'IL'),
	('Miami', 'FL'),
	('Dallas', 'TX'),
	('Seattle', 'WA'),
	('Portland', 'OR'),
	('San Francisco', 'CA'),
	('Los Angeles', 'CA'),
	('Washington', 'DC'),
	('Houston', 'TX'),
	('Las Vegas', 'NV'),
	('Atlanta', 'GA')
)

weather = (
	('New York City', 2013, 'July', 'January', 62),
	('Boston', 2013, 'July', 'January', 59),
	('Chicago', 2013, 'July', 'January', 59),
	('Miami', 2013, 'August', 'January', 84),
	('Dallas', 2013, 'July', 'January', 77),
	('Seattle', 2013, 'July', 'January', 61),
	('Portland', 2013, 'July', 'December', 63),
	('San Francisco', 2013, 'September', 'December', 64),
	('Los Angeles', 2013, 'September', 'December', 75),
	('Washington', 2013, 'July', 'January', 70),
	('Houston', 2013, 'July', 'January', 80),
	('Las Vegas', 2013, 'July', 'December', 80),
	('Atlanta', 2013, 'July', 'January', 70)
)

# Connect to the database. The "connect()" method returns a connection object.
con = lite.connect('getting_started.db')

with con:
	cur = con.cursor()

# Drop currently existing tables.
	cur.execute("DROP TABLE IF EXISTS cities")
	cur.execute("DROP TABLE IF EXISTS weather")
	
# Create the tables.
	cur.execute("CREATE TABLE cities (name text, state text)")
	cur.execute("CREATE TABLE weather (city text, year integer, warm_month text, cold_month text, average_high integer)")

# Insert rows of data by passing tuples through the "execute()" method.
	cur.executemany("INSERT INTO cities VALUES(?,?)", cities)
	cur.executemany("INSERT INTO weather VALUES(?,?,?,?,?)", weather)

# Join the tables and select cities with specific month.
	cur.execute("SELECT name, state FROM cities INNER JOIN weather ON name = city WHERE warm_month = 'July'")