from flask import Flask, render_template, request
import joblib

app = Flask(__name__)

model = joblib.load("placement_model.pkl")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():

    cgpa = float(request.form["cgpa"])
    iq = float(request.form["iq"])
    profile = float(request.form["profile_score"])
    internship = int(request.form["internship"])
    communication = int(request.form["communication"])
    projects = int(request.form["projects"])
    aptitude = int(request.form["aptitude"])

    prediction = model.predict([[cgpa, iq, profile,
                                 internship,
                                 communication,
                                 projects,
                                 aptitude]])

    if prediction[0] == 1:
        result = "Congratulations! You are likely to get placed."
    else:
        result = "Placement chance is low."

    return render_template("index.html", prediction=result)

if __name__ == "__main__":
    app.run(debug=True)