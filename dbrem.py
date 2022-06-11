import sqlite3

#Connecting to sqlite
conn = sqlite3.connect('db.sqlite3')

#Creating a cursor object using the cursor() method
cursor = conn.cursor()

#Doping EMPLOYEE table if already exists
cursor.execute('''CREATE TABLE statement (
	id INTEGER NOT NULL, 
	text VARCHAR(255), 
	search_text VARCHAR(255) DEFAULT '' NOT NULL, 
	conversation VARCHAR(32) DEFAULT '' NOT NULL, 
	created_at DATETIME DEFAULT (CURRENT_TIMESTAMP), 
	in_response_to VARCHAR(255), 
	search_in_response_to VARCHAR(255) DEFAULT '' NOT NULL, 
	persona VARCHAR(50) DEFAULT '' NOT NULL, 
	PRIMARY KEY (id)
)''')
print("Table dropped... ")

#Commit your changes in the database
conn.commit()

#Closing the connection
conn.close()