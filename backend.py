from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def predictor():
    return render_template("predictor.html")

@app.route("/hdp", methods=["POST"])
def hdp():
    if request.method == "POST":
        age = request.form.get(age)
        print(request.form[])
        print(request.form['gender'])
    return 'Hello ' + request.form['age']