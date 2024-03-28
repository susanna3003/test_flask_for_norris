from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def index():
    current_datetime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return render_template("index.html", current_datetime=current_datetime)

@app.route('/user_greet', methods=['GET', 'POST'])
def user_greet():
    if request.method == 'POST':
        # Get form data
        name = request.form['name']
        age = request.form['age']
        dateBorn = request.form['dateBorn']
        birthPlace = request.form['birthPlace']
        lastPlace = request.form['lastPlace']
        favHobby = request.form['favHobby']

        # Store the data in a "wanted listing"
        crime_description = f"Suspect's favorite hobby is {favHobby}. Approach with caution."
        wanted_listing = {
        'Name': name,
        'Age': age,
        'Date of Birth': dateBorn,
        'Place of Birth': birthPlace,
        'Last Visited Place': lastPlace,
        'Crime Description': crime_description
        }

        # Redirect to the "Wanted" poster page with the data
        return render_template("wanted.html", wanted_listing=wanted_listing)
    else:
        # Display the form
        return render_template("user_greet.html")
  
@app.route('/wanted', methods=['POST'])
def wanted():
    return render_template("wanted.html")

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=5001, debug=True)