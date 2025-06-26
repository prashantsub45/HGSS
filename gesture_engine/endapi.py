from flask import Flask, jsonify, request
from flask_cors import CORS
import csv
import pandas as pd
import json

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Flag to track if the API has already been sent
api_sent = False

# Function to play the track
def csv_to_json(csv_file_path):
    with open(csv_file_path, 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        data_list = [row for row in csv_reader]

    json_data = json.dumps(data_list, indent=2)
    return json_data

# API endpoint to play the track
@app.route('/okay', methods=['GET', 'POST'])
def index():
    global api_sent  # Declare global variable
    
    if request.method == 'GET':
        csv_path = 'C:/Users/ASUS/Desktop/Final minor project/minorProject/gesture_engine/try.csv'

        # Call the function to convert CSV to JSON
        json_data = csv_to_json(csv_path)
        df=pd.read_csv(csv_path)
        df["comm"]="none"
        df.to_csv(csv_path)

        response = jsonify(json.loads(json_data))


        return response
    elif request.method == 'POST':
        if not api_sent:  # Check if API has not been sent yet
            # Handle the POST request
            # Access POST request data using request.json or request.form
            # Perform necessary actions based on the received data
            # Return appropriate response

            # Example:
            received_data = request.json
            success_value = received_data.get('success') 
            print(success_value)
            if success_value:
                json_data = {"comm": ""}
            else:
                json_data = {"comm": "failure"}  # Or any other desired value

            # Return a JSON response
            api_sent = True  # Set flag to indicate API has been sent
            return jsonify(json_data)
        else:
            return jsonify({"message": "API already sent"})

if __name__ == '__main__':
    app.run(debug=True, port=4000)
