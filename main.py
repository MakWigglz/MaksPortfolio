import csv
import sqlite3

conn = sqlite3.connect('customer_data.db')
cursor = conn.cursor()

cursor.execute('''
      CREATE TABLE IF NOT EXISTS customers (
          id INTEGER PRIMARY KEY,
          Customer_Id TEXT,
          First_Name TEXT,
          Last_Name TEXT,
          Company TEXT,
          City TEXT,
          Country TEXT,
          Phone_1 TEXT,
          Phone_2 TEXT,
          Email TEXT,
          Subscription_Date TEXT,
          Website TEXT
)   
''')
# open the CSV file
with open('customers-100.csv', 'r') as f:
    # create a csv reader object 
    reader = csv.DictReader(f)
    
    # iterate over each row in the CSV file
    for row in reader:
        # insert the data into the customers table
        cursor.execute('''
            INSERT INTO customers (
                Customer_Id, First_Name, Last_Name, Company, City, Country, Phone_1, Phone_2, Email, Subscription_Date, Website
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?) 
        ''', (
            row['Customer Id'], row['First Name'], row['Last Name'], row['Company'], row['City'], row['Country'], row['Phone 1'], row['Phone 2'], row['Email'], row['Subscription Date'], row['Website']
            
        ))
# Commit the changes and close the connection
conn.commit()
conn.close()
                       