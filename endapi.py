import time
from flask import Flask, jsonify
import csv
import json
app = Flask(__name__)

# # Function to play the track
def csv_to_json(csv_file_path):
    with open(csv_file_path, 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        data_list = [row for row in csv_reader]

    json_data = json.dumps(data_list, indent=2)
    return json_data
# API endpoint to play the track
@app.route('/')
def index():
    csv_path = 'C:\\Users\\ASUS\\Desktop\\opencv\\try.csv'

    # Call the function to convert CSV to JSON
    json_data = csv_to_json(csv_path)

    return jsonify(json.loads(json_data))
    
if __name__ == '__main__':
    app.run(debug=True)
