from flask import Flask, request, jsonify

app = Flask(__name__) 
from flask_cors import CORS

CORS(app, resources={r"/*": {"origins": "http://127.0.0.1:5500"}})

import util

@app.route('/get_location_names')
def get_location_names():
    response = jsonify({
        'locations': util.get_location_names()
    })
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response
 

@app.route('/predict_home_price', methods = ['POST'])
def predict_home_price():
    total_sqft = float(request.form['total_sqft'])
    location = request.form['location']
    bhk = int(request.form['bhk'])
    bath = int(request.form['bath'])

    response = jsonify({
        'estimated_price': util.get_estimated_price(location, total_sqft, bhk, bath)
    })

    return response


if __name__ == "__main__":
    print("Starting Flask server")
    util.load_artifacts()
    print(get_location_names)
    app.run()