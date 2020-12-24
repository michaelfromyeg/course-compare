import os
from flask import Flask, jsonify
from flask_cors import CORS, cross_origin

from user import User

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

app.config["DEBUG"] = True

USERS = []
COURSE_LIST = []

@app.route('/', methods=["GET"])
@cross_origin()
def home():
    return jsonify(data=' hello world') 

def _test():
    '''
    Build test users and experiment with functionality
    '''
    test_directory = './data'
    for i, filename in enumerate(os.listdir(test_directory)):
        if filename.endswith(".ics"):
            new_user: 'User' = User(f"{i}@{i}.com", str(i), [])
            new_user.add_courses(f"{test_directory}/{filename}")
            USERS.append(new_user)
    
    for user in USERS:
        print("== USER ==")
        print(user)
        user.print_courses()
        print()

    print(USERS[0].classmates(USERS[1:]))
    
app.run()

if __name__ == '__main__':
    _test()