from flask import Flask, render_template, request
from functions import *

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/contact')
def contact():
    return render_template("contact.html")



@app.route('/predictor', methods=['GET', 'POST'])
def predictor():
    if request.method == "POST":
        Age = int(request.form['age'])
        Chol = int(request.form['chol'])
        gender = request.form["gender"]

        if gender == "male":
            Sex = int(1)
        else:
            Sex = int(0)

        Cp = int(request.form['cp'])
        bp = int(request.form['bp'])

        perBP = lrbp(bp)
        perChol = lrchol(Chol)
        perSex = lrsex(Sex)
        perAge = lrage(Age)
        perTree = dtree(*(Cp, Age, Sex, bp, Chol))
        YourPercent = (perBP + perBP + perChol + perChol + perSex + perAge + perTree)/7
        Yp = round(YourPercent[0], 2)
        Yp1 = int(Yp)
        FinalPercent = Yp
        
        if Yp1 >= 50:
            x = "There is a good chance you have heart disease. If you did have heart disease, the specific type/s you would probably have is/are: "
        else:
            x = "You probably don't have heart disease. But if you did have heart disease, the specific type/s you would probably have is/are: "
        if Cp == 1:
            x += "Cardiac Ischemia or Heart Failure"
        elif Cp == 2:
            x += "Arrhythmia and/or Gastroesophageal Reflux (Not a heart disease but still causes chest discomfort)"
        elif bp > 140:
            x += "Hypertensive Heart Disease"
        elif Chol > 239:
            x += 'Coronary Heart Disease, Aortic Valve Disease, or Atherosclerotic Cardiovascular Disease'
        elif Cp == 0:
            x += "Coronary Heart Disease"
        else:
            x += "Coronary Heart Disease with No Symptoms"

                    
        return render_template('result.html', FinalPercent = FinalPercent, Type = x)
    else: 
        return render_template('predictor.html')

app.run(host='0.0.0.0', port=2784)

