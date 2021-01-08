import os
from flask import Flask, redirect, url_for, jsonify
from flask_cors import CORS, cross_origin

from controllers.user import User

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

app.config["DEBUG"] = True

USERS = []

@app.route('/', methods=["GET"])
def home():
    '''
    Show that the API is live
    '''
    return "The API is up and running!"

@app.route("/login", methods=["GET", "POST"])
def login():
    return "login"

@app.route("/signup", methods=["GET", "POST"])
def signup():
    return "signup"

@app.route("/user", methods=["GET", "POST"])
def user():
    '''
    GET - get a user's public information
    POST - create a new user
    '''
    return "user"

@app.route("/users", methods=["GET"])
def users():
    '''
    GET - get all / a certain # of users
    '''
    return "users"

@app.route("/schedule", methods=["GET", "POST"])
def schedule():
    '''
    GET /schedule - return a user's schedule
    POST /schedule - upload a user's schedule
    '''
    return "schedule"

@app.route("/classmates", methods=["GET"])
def classmates():
    '''
    GET /classmates - get a user's classmates
    '''
    return "classmates"

def _test():
    '''
    Build test users and experiment with functionality
    '''
    test_directory = './data'
    for i, filename in enumerate(os.listdir(test_directory)):
        if filename.endswith(".ics"):
            new_user: 'User' = User(f"{i}th", "Doe", f"{i}@{i}.com", str(i), [])
            new_user.add_courses(f"{test_directory}/{filename}")
            USERS.append(new_user)
    
    for user in USERS:
        print("== USER ==")
        print(user)
        user.print_courses()
        print()

    print(USERS[0].classmates(USERS[1:]))
    
if __name__ == '__main__':
    app.run(debug=True)
    # _test()