from flask import Flask, jsonify
from flask_cors import CORS
app = Flask(__name__) 
CORS(app)

@app.route('/vl') 
def hello(): 
	return "{flam: 2, rayon: 4}"

@app.route('/flammes')
def flammes():
    flammes = [{'rayon': 1, 'intensite': 1, 'coord': [45.7412, 4.836]}, {'rayon': 2, 'intensite': 1, 'coord': [45.744, 4.863]}]
    return jsonify(flammes)

if __name__ == "__main__": 
	app.run(host ='0.0.0.0', port = 5001, debug = True) 