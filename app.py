from flask import Flask, render_template, request, redirect, url_for, jsonify
from pymongo import MongoClient
import json

app = Flask(__name__)

# -------- MongoDB Atlas Connection --------
MONGO_URI = "mongodb+srv://Reshma_kdm28:R1e2s3h4u@cluster0.l9qecdr.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

client = MongoClient(MONGO_URI)
db = client["flaskDB"]
collection = db["users"]

# -------- API Route --------
@app.route("/api")
def api():
    try:
        with open("data.json", "r") as file:
            data = json.load(file)
        return jsonify(data)
    except Exception as e:
        return jsonify({"error": str(e)})

# -------- Home Page --------
@app.route("/")
def form():
    return render_template("form.html")

# -------- Submit Form --------
@app.route("/submit", methods=["POST"])
def submit():
    try:
        name = request.form["name"]
        email = request.form["email"]

        collection.insert_one({
            "name": name,
            "email": email
        })

        return redirect(url_for("success"))

    except Exception as e:
        return render_template("form.html", error=str(e))

# -------- Success Page --------
@app.route("/success")
def success():
    return render_template("success.html")

if __name__ == "__main__":
    app.run(debug=True)
