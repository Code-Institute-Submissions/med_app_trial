from flask import Flask, render_template, request, redirect, url_for 
import os
from flask_pymongo import PyMongo

app = Flask(__name__)


app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")

mongo = PyMongo(app)

def get_category_names():
    categories = []
    for category in mongo.db.collection_names():
        if not category.startswith("system."):
            categories.append(category)
    return categories


@app.route("/")
def show_meds():
    print(request.method)
    
    
    return render_template("base.html")
    
    
@app.route("/add_medication", methods=["GET", "POST"])
def add_medication():
    if request.method=="POST":
        form_values = request.form.to_dict()
        form_values["Course_complete"] = "Course_complete" in form_values
        
        category = form_values["category_name"]
        mongo.db[category].insert_one(form_values)
        return redirect(url_for("get_tasks_by_category", category=form_values["category_name"]))
    else:
        categories = get_category_names()
        
        
        
        
        return render_template("add_medication.html")



















if __name__ == "__main__":
        app.run(host=os.getenv('IP', '0.0.0.0'), port=int(os.getenv('PORT', 8080)), debug=True)