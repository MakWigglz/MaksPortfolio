from flask import Flask
from .database import get_db_connection, insert_finance_data, get_finance_data
from .finance_operations import start_background_tasks

def create_app():
    app = Flask(__name__)

    # You can add configuration settings here
    app.config['SECRET_KEY'] = 'your-secret-key'  # Replace with a real secret key

    # Initialize the database
    with app.app_context():
        db = get_db_connection()
        db.close()

    # Start background tasks
    start_background_tasks()

    # Import and register blueprints here
    from .routes import main
    app.register_blueprint(main)

    return app