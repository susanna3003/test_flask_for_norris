from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")

@app.route('/user_greet')
def user_greet():
    import datetime
    current_datetime = datetime.datetime.now()
    return f"Hello! Current date and time is {current_datetime}"
  
if __name__ == '__main__':
  app.run(host='0.0.0.0', port=80)
