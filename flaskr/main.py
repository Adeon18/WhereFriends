'''
This is the main script that runs a web application
'''
from flask import Flask, render_template, request
import csv

from map_handler import *
from twitter_api_handler import *

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/register", methods=["POST"])
def register():
    if not request.form.get("username") or not request.form.get("bearer_token"):
        return render_template("failure.html")

    data = pull_data(request.form.get("username"),\
                     request.form.get("bearer_token"))

    if data == False:
        return render_template("failure.html")
    # Create the map
    load_map(find_coords(extract_data(data)))
    
    return render_template("Friends.html")


if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=8000)
