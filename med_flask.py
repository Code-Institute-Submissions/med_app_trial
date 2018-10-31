from flask import Flask, render_template, request, redirect, url_for 
import os
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

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
        
        
        
        
@app.route("/meds/<med_id>/delete", methods=["POST"])
def delete_med():
    med_id = request.form['med_id']
    mongo.db["Medications"].remove({"_id":ObjectId(med_id)})
    return redirect(url_for("get_meds"))
    
    
    
@app.route('/meds/Medications/<med_id>/edit', methods=["GET", "POST"])
def edit_med(med_id):
    if request.method=="POST":
        form_values = request.form.to_dict()
        form_values["Day"]= request.form.getlist("Day")
        form_values["Time"]= request.form.getlist("Time")
        
        
        mongo.db["Medications"].update({"_id": ObjectId(med_id)}, form_values)
        
        the_med =  mongo.db["Medications"].find_one({"_id": ObjectId(med_id)})
        
        return render_template('editmed.html', med=the_med)




















if __name__ == "__main__":
        app.run(host=os.getenv('IP', '0.0.0.0'), port=int(os.getenv('PORT', 8080)), debug=True)