from flask import Flask, request, render_template, redirect, url_for

app = Flask(__name__)

def get_user_info_from_terminal():
    """Gets user info via the input() function in the terminal."""
    user_data = {}
    user_data['name'] = input("Enter your name: ")
    user_data['phone'] = input("enter your phone number: ")
    while True:
        try:
            user_data['age'] = int(input("Enter your age: "))
            if user_data['age'] >= 0:
                break
            else:
                print("Age cannot be negative, unless you owe God years")
        except ValueError:
            print("invalid input. Enter a number for age")
    user_data['gender'] = input("Enter your gender: ")
    while True:
        political_view = input("Are you MAGA or Anti-American?").strip().upper()
        if political_view in ["MAGA", "Anti-American"]:
            user_data['political view'] = political_view
            break
        else:
            print("invalid input")
    return user_data

user_info = get_user_info_from_terminal()

@app.route('/')
def display_user_info():
    return render_template('user_info.html', user=user_info)

if __name__ == '__main__':
    app.run(debug=True)
        
