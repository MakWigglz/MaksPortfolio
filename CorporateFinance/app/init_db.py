import sqlite3
import csv
from database import get_db_connection, insert_finance_data

def create_database():
    conn = get_db_connection()
    with open('sql/corporateFinance.sql', 'r') as sql_file:
        sql_script = sql_file.read()
    conn.executescript(sql_script)
    conn.close()

def import_customer_data():
    conn = get_db_connection()
    with open('data/customers-100.csv', 'r') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            insert_finance_data(
                None, None, None, None,
                row['Index'], row['Customer Id'], row['First Name'], row['Last Name'],
                row['Company'], row['City'], row['Country'], row['Phone 1'],
                row['Phone 2'], row['Email'], row['Subscription Date'], row['Website']
            )
    conn.close()

def import_financial_data():
    conn = get_db_connection()
    with open('data/financial_data.csv', 'r') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            insert_finance_data(
                row['Date'], row['Revenue'], row['Expense'], row['Profit'],
                None, None, None, None, None, None, None, None, None, None, None, None
            )
    conn.close()

if __name__ == "__main__":
    create_database()
    import_customer_data()
    import_financial_data()