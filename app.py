import wolframalpha
from flask import Flask, render_template, request

app = Flask(__name__)

# החלף ב-API key שלך
app_id = "A68RT7-RGQVY74789"
client = wolframalpha.Client(app_id)

@app.route("/mychat", methods=["GET", "POST"])
def mychat():
    if request.method == "POST":
        question = request.form["question"]
        res = client.query(question)
        answer = next(res.results).text
        return render_template("mychat.html", question=question, answer=answer)
    return render_template("mychat.html")
@app.route("/")
def home():
    return render_template("home.html")

if __name__ == "__main__":
    app.run(debug=True)
