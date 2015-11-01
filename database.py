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
