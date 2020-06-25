# -*- coding: utf-8 -*-

from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_mars

app = Flask(__name__)

# Use flask_pymongo to set up mongo connection
app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_db"
mongo = PyMongo(app)
# Or set inline
 #mongo = PyMongo(app, uri="mongodb://localhost:27017/mars_db")


@app.route("/")
def index():
   mars_info = mongo.db.mars_info.find_one()
   print(mars_info)
   return render_template("index.html", mars_info=mars_info)

@app.route("/scrape")
def scrape():
    mars_info= mongo.db.mars_info
    mars_data = scrape_mars.scrape_info()
    mars_info.update({}, mars_data, upsert=True)
    return redirect("/", code=302)


if __name__ == "__main__":
   app.run(debug=True)

