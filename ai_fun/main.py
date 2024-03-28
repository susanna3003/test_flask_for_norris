from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/user_greet')
def user_greet():
    import datetime
    current_datetime = datetime.datetime.now()
    return render_template("user_greet.html", current_datetime=current_datetime)
  
@app.route('/generate_wanted', methods=['POST'])
def generate_wanted():
    # Get form data
    name = request.form['name']
    age = request.form['age']
    dateBorn = request.form['dateBorn']
    birthPlace = request.form['birthPlace']
    lastPlace = request.form['lastPlace']
    favHobby = request.form['favHobby']

    # Generate "WANTED" listing
    crime_description = f"Suspect's favorite hobby is {favHobby}. Approach with caution."
    wanted_listing = {
        'Name': name,
        'Age': age,
        'Date of Birth': dateBorn,
        'Place of Birth': birthPlace,
        'Last Visited Place': lastPlace,
        'Crime Description': crime_description
    }

    return render_template("wanted.html", wanted_listing=wanted_listing)

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=5000)