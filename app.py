from flask import Flask, jsonify
from flask_cors import CORS

DEBUG = True

# Instantiate app
app = Flask(__name__)
app.config.from_object(__name__)

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})

# Sanity check route
@app.route('/ping', methods=['GET'])
def ping_pong():
    return jsonify('PONG!')


if __name__ == '__main__':
    app.run()
