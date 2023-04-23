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
        YourPercent = (perBP + perChol + perSex + perAge + perTree)/5
        Yp = round(YourPercent[0], 2)
        Yp1 = int(Yp)
        FinalPercent = Yp
        
        if Yp1 >= 50:
            x = "There is a good chance you have heart disease and should probably see a doctor to check if you do have heart disease. If you did have heart disease, the specific type/s you would probably have is/are: "
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
        u = "Having heart disease is not the end of the world. With the right course of action (see a doctor to discuss this), heart disease and it's effects can be kept at a minimum. (REMEMBER THAT A DOCTOR'S WORD IS MORE IMPORTANT THAN THIS PROGRAM'S.) " 
        if bp > 119:
            u += "You have high blood pressure. Some ways to lower your blood pressure is by exercising regularly, reducing sodium in diet, eating healthier, quit smoking and alcohol, and reducing stress. "   
        if Chol > 239:
            u += "Your total cholesterol value is too high. Some ways to lower cholesterol is reducing/removing saturated and trans fats from diet, increasing physical activity, losing weight, and quiting smoking and alcohol."
        elif Chol > 199:
            u += "Your total cholesterol value is borderline high.  Some ways to lower cholesterol is reducing/removing saturated and trans fats from diet, increasing physical activity, losing weight, quiting smoking and alcohol, and possibly medication."  
        return render_template('result.html', FinalPercent = FinalPercent, Type = x, Help = u)
    else: 
        return render_template('predictor.html')

app.run(host='0.0.0.0', port=2784)

