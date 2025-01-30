import sqlite3
from threading import Lock

db_lock = Lock()

def get_db_connection():
    conn = sqlite3.connect('finance.db')
    conn.row_factory = sqlite3.Row
    return conn

def get_finance_data():
    with db_lock:
        conn = get_db_connection()
        finance_data = conn.execute('SELECT * FROM corporateFinance').fetchall()
        conn.close()
    return finance_data

def insert_finance_data(date, revenue, expense, profit, customer_index, customer_id, first_name, last_name, company, city, country, phone1, phone2, email, subscription_date, website):
    with db_lock:
        conn = get_db_connection()
        conn.execute('''
            INSERT INTO corporateFinance 
            (Date, Revenue, Expense, Profit, CustomerIndex, CustomerId, FirstName, LastName, Company, City, Country, Phone1, Phone2, Email, SubscriptionDate, Website) 
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', (date, revenue, expense, profit, customer_index, customer_id, first_name, last_name, company, city, country, phone1, phone2, email, subscription_date, website))
        conn.commit()
        conn.close()