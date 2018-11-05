from flask import Flask, render_template, request, redirect, url_for 
import os
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
import datetime
import calendar

app = Flask(__name__)


app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
COLLECTION_NAME = "Medications"

mongo = PyMongo(app)


    
    
def get_category_names():
    categories = []
    for category in mongo.db.collection_names():
        if not category.startswith("system."):
            categories.append(category)
    return categories
    
def get_date():
    now=datetime.datetime.now()
    return (now.strftime("%Y-%m-%d %H:%M:%S"))


def get_today():
    t = datetime.datetime.today()
    return calendar.day_name[t.weekday()]

    
def get_time_of_day():
    t = datetime.datetime.today()
    h= t.hour
    if h<=11 and h>=0:
        return "Morning"
    if h>11 and h<=14:
        return "Afternoon"
    if h>15 and h<=18:
        return "Evening"
    else:
            return "Night"
    
    


    
@app.route("/meds")
def get_meds():
    meds = mongo.db["Medications"].find()
    
    return render_template("meds.html", meds=meds)

    
    
    
    
@app.route("/add_medication", methods=["GET", "POST"])
def add_meds():
    if request.method=="POST":
        form_values = request.form.to_dict()
        form_values["Day"]= request.form.getlist("Day")
        form_values["Time"]= request.form.getlist("Time")
        
        mongo.db["Medications"].insert_one(form_values)
        return redirect(url_for("get_meds"))
    else:
        
        
        return render_template("add_medication.html")
        
        
        
        
@app.route('/meds/Medications/<med_id>/delete', methods=["GET","POST"])
def delete_med(med_id):
    
    
    
    mongo.db["Medications"].remove({"_id":ObjectId(med_id)})
    return redirect(url_for("get_meds"))
    
    
    
@app.route('/meds/Medications/<med_id>/edit', methods=["GET", "POST"])
def editmed(med_id):
    if request.method=="POST":
        form_values = request.form.to_dict()
        form_values["Day"]= request.form.getlist("Day")
        form_values["Time"]= request.form.getlist("Time")
        mongo.db["Medications"].update({"_id": ObjectId(med_id)}, form_values)
        
        
        return redirect(url_for("get_meds"))
    else:
        
        the_med =  mongo.db["Medications"].find_one({"_id": ObjectId(med_id)})
        
        return render_template('editmed.html', med=the_med)
        
@app.route('/trial')
def get_meds_for_week():
    meds = mongo.db["Medications"].find()
    days=['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    weekly = {}
    for day in days:
        weekly[day] = {
            "Morning" : [(i['Medication_Name'],i['Dose']) for i in mongo.db.Medications.find({"Day": day, "Time": "Morning" })],
            "Afternoon" : [(i['Medication_Name'],i['Dose']) for i in mongo.db.Medications.find({"Day": day, "Time": "Afternoon" })],
            "Evening" : [(i['Medication_Name'],i['Dose']) for i in mongo.db.Medications.find({"Day": day, "Time": "Evening" })],
            "Night" : [(i['Medication_Name'],i['Dose']) for i in mongo.db.Medications.find({"Day": day, "Time": "Night" })],
        }
    print(weekly)
    
    return render_template("trial.html", weekly=weekly )
    
    
        
@app.route('/now')
def current_meds():
    day = get_today()
    time_of_day = get_time_of_day()
    meds = mongo.db.Medications.find({"Day": day, "Time": time_of_day })
    return render_template("Now.html", day=day, time_of_day=time_of_day, date= get_date(), meds=meds)
    

@app.route('/trial')
def trial():
    meds = mongo.db["Medications"].find()
    days=['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    weekly = {}
    for day in days:
        weekly[day] = {
            "Morning" : [i['Medication_Name'] for i in mongo.db.Medications.find({"Day": day, "Time": "Morning" })],
            "Afternoon" : [i['Medication_Name'] for i in mongo.db.Medications.find({"Day": day, "Time": "Afternoon" })],
            "Evening" : [i['Medication_Name'] for i in mongo.db.Medications.find({"Day": day, "Time": "Evening" })],
            "Night" : [i['Medication_Name'] for i in mongo.db.Medications.find({"Day": day, "Time": "Night" })],
        }
    print(weekly)
    return render_template("trial.html",weekly=weekly)

@app.route('/')
def get_home():
    return render_template('home.html')
    
    




















if __name__ == "__main__":
        app.run(host=os.getenv('IP', '0.0.0.0'), port=int(os.getenv('PORT', 8080)), debug=True)