from flask import Flask, render_template, request, redirect, url_for 
import os
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)


app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
COLLECTION_NAME = "Meds"

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
        category = form_values["category_name"]
        mongo.db[category].insert_one(form_values)
        return redirect("/meds")
    else:
        categories = []
        for category in mongo.db.collection_names():
            if not category.startswith("system."):
                categories.append(category)
        
        return render_template("add_medication.html", categories=categories)


















if __name__ == "__main__":
        app.run(host=os.getenv('IP', '0.0.0.0'), port=int(os.getenv('PORT', 8080)), debug=True)