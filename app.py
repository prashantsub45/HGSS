from flask import Flask, render_template, send_from_directory
import os
app = Flask(__name__, static_url_path='/static', static_folder='static')

@app.route('/')



def index():

    
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)