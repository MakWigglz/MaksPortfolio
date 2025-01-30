import threading
import time
from database import insert_finance_data, get_finance_data

def background_task():
    while True:
        # Perform some background finance operations
        # For example, let's add a recurring expense every hour
        insert_finance_data('2023-01-01', 0, 100, -100, None, None, None, None, None, None, None, None, None, None, None, None)
        time.sleep(3600)  # Sleep for 1 hour

def data_analysis_task():
    while True:
        # Perform data analysis on the finance data
        finance_data = get_finance_data()
        # Perform your analysis here
        # For example, calculate total revenue and expenses
        total_revenue = sum(row['Revenue'] for row in finance_data)
        total_expenses = sum(row['Expense'] for row in finance_data)
        print(f"Total Revenue: {total_revenue}, Total Expenses: {total_expenses}")
        time.sleep(3600)  # Perform analysis every hour

def start_background_tasks():
    threading.Thread(target=background_task, daemon=True).start()
    threading.Thread(target=data_analysis_task, daemon=True).start()