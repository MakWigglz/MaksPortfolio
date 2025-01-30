from flask import Blueprint, render_template
from .database import get_finance_data

main = Blueprint('main', __name__)

@main.route('/')
def index():
    finance_data = get_finance_data()
    return render_template('index.html', finance_data=finance_data)