import sqlite3
from sqlite3 import Error
import csv

def create_connection():
    try:
        conn = sqlite3.connect('customer_data.db')
        return conn
    except Error as e:
        print(e)
    return None

# ... (keep the imports and create_connection function as is)

def init_db():
    conn = create_connection()
    if conn is not None:
        try:
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

            # Insert data into the customers table
            with open('/Users/amakki/Documents/Coding-Design/GitHub/emptyforGithubClones/Maksportfolio/MaksPortfolio/MaksPortfolio/CorporateFinance/data/customers-100.csv', 'r') as f:
                reader = csv.DictReader(f)
                for row in reader:
                    cursor.execute('''
                        INSERT INTO customers (
                            Customer_Id, First_Name, Last_Name, Company, City, Country, Phone_1, Phone_2, Email, Subscription_Date, Website
                        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                    ''', (
                        row['Customer Id'], row['First Name'], row['Last Name'], row['Company'], row['City'], row['Country'], row['Phone 1'], row['Phone 2'], row['Email'], row['Subscription Date'], row['Website']
                    ))

            conn.commit()
            print("Database initialized successfully.")
        except Error as e:
            print(e)
        finally:
            conn.close()
    else:
        print("Error! Cannot create the database connection.")

if __name__ == '__main__':
    init_db()
