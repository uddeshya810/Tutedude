# Create a form on the frontend , when submitted , insert data into MongoDB Atlas. Upon successfull submission , the user should be redirected to another page displaying the massage "Data Submitted Successfully". If there's an error during submission , display the error on the same page without redirection.
import os
from flask import Flask, render_template, request, redirect
from pymongo import MongoClient
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

client = MongoClient(os.getenv("MONGO_URI"))
# Connect MongoDB

db = client["university"]
students = db["students"]

# Show form
@app.route("/")
def home():
    return render_template("index.html")


# Save form data
@app.route("/submit", methods=["POST"])
def submit():
    try:
        data = {
            "roll_no": request.form.get("roll_no"),
            "enrollment_no": request.form.get("enrollment_no"),
            "name": request.form.get("name"),
            "student_id": request.form.get("student_id"),
            "department": request.form.get("department"),
            "year": request.form.get("year")
        }

        students.insert_one(data)

        return redirect("/success")

    except Exception as e:
        return render_template("index.html", error=str(e))

#To view data stored in Database
from flask import jsonify

@app.route("/view")
def view():
    data = list(students.find({}, {"_id":0}))
    return jsonify(data)

# Success page
@app.route("/success")
def success():
    return render_template("success.html")


if __name__ == "__main__":
    app.run(debug=True)