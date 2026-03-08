# Create a flask applicationon /api. When this route ia accessed return , it return a JSON list. The data should be stored in backend file,read from it, and send ad a response.
from flask import Flask
from flask import jsonify

app = Flask(__name__)

@app.route("/api")
def home():
    with open("name.txt" , "r") as file:
        data = file.read()
        names = [name.strip() for name in data.split(",")]
        return jsonify({"students":names})

@app.route("/")
def dataEntry():
    with open("name.txt" , "w") as file:
        file.write("\nUddeshya , Ram , Sujana , Akhilesh , Sonu ")
        return " Backend File Created and Information Successfully Added."    
    
if __name__ == "__main__":
    app.run(debug=True)
    