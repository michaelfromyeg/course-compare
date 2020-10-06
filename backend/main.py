from flask import Flask, jsonify
from flask_cors import CORS, cross_origin

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

app.config["DEBUG"] = True

@app.route('/', methods=["GET"])
@cross_origin()
def home():
    return jsonify(data=' hello world')

app.run()
