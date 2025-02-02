import sqlite3
from sqlite3 import Error

def create_connection():
    try:
        conn = sqlite3.connect('customer_data.db')
        return conn
    except Error as e:
        print(e)
    return None

def query_all_customers(conn):
    cur = conn.cursor()
    cur.execute("SELECT * FROM customers")
    rows = cur.fetchall()
    return rows

def query_customers_by_country(conn, country):
    cur = conn.cursor()
    cur.execute("SELECT * FROM customers WHERE Country=?", (country,))
    rows = cur.fetchall()
    return rows

def print_customers(customers):
    for customer in customers:
        print(f"ID: {customer[0]}")
        print(f"Name: {customer[2]} {customer[3]}")
        print(f"Company: {customer[4]}")
        print(f"Country: {customer[6]}")
        print(f"Email: {customer[9]}")
        print("------------------------")

def main():
    conn = create_connection()
    if conn is not None:
        while True:
            print("\n1. View all customers")
            print("2. View customers by country")
            print("3. Exit")
            choice = input("Enter your choice (1-3): ")

            if choice == '1':
                customers = query_all_customers(conn)
                print_customers(customers)
            elif choice == '2':
                country = input("Enter country name: ")
                customers = query_customers_by_country(conn, country)
                print_customers(customers)
            elif choice == '3':
                break
            else:
                print("Invalid choice. Please try again.")

        conn.close()
    else:
        print("Error! Cannot create the database connection.")

if __name__ == '__main__':
    main()