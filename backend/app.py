import os
from flask import Flask, jsonify, flash, request, redirect, url_for
from flask_cors import CORS, cross_origin
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = './uploads'
ALLOWED_EXTENSIONS = {'.ical', '.txt'}

app = Flask(__name__)
CORS(app, support_credentials=True)
app.config['CORS_HEADERS'] = 'Content-Type'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['DEBUG'] = True

@app.route('/', methods=["GET"])
@cross_origin(origin='*')
def home():
    return jsonify(data=' hello world')

@app.route('/schedule', methods=['POST'])
@cross_origin(origin='*')
def upload_file():
    print(request.files)
    if 'file' not in request.files:
        print('here')
        return jsonify(status=500), 500
    file = request.files['file']
    print(file.filename)
    # if uploaded_file.filename != '':
    #     print(uploaded_file.filename)
    #     uploaded_file.save(uploaded_file.filename)
    return jsonify(status=200), 200


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

app.run()