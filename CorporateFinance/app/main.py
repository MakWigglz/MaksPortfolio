from app import create_app
from finance_operations import start_background_tasks

app = create_app()

if __name__ == "__main__":
    start_background_tasks()
    app.run(host='0.0.0.0', port=5000)