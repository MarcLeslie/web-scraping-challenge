from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_mars #Moving scrape mars to the outside folder makes this be recognized but it causes problems with it running#

# Create an instance of Flask
app = Flask(__name__)

# Use PyMongo to establish Mongo connection
mongo = PyMongo(app, uri="mongodb://localhost:27017/mars_db")


# Route to render index.html template using data from Mongo
@app.route("/")
def home():

    # Find one record of data from the mongo database
    mars_data = mongo.db.collection.find_one()

    # Return template and data
    return render_template("index.html", mars=mars_data)


# Route that will trigger the scrape function
@app.route("/scrape")
def scrape():

    # Run the scrape function
    mars_data = scrape_mars.scrape_all_pages()

    # Update the Mongo database using update and upsert=True
    mongo.db.collection.update({}, mars_data, upsert=True)

    # Redirect back to home page/route
    return redirect("/", code=302)
    
    
# THIS MUST BE AT THE END TO CLOSE IT
if __name__ == "__main__":
    app.run(debug=True)
