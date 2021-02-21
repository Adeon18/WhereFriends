from flask import Flask, render_template, request
import csv

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/register", methods=["POST"])
def register():
    if not request.form.get("username"):
        return render_template("failure.html")
    # file = open("registrants.csv", "a")
    # writer = csv.writer(file)
    # writer.writerow((request.form.get("name"), request.form.get("domain")))
    # file.close()
    print(request.form.get("username"))
    return render_template("success.html")

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=8000)
