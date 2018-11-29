from flask import *
app = Flask(__name__)

@app.route("/")
def home():
    return render_template('home.html')

@app.route("/link1")
def link_1():
    return render_template('link1.html')

@app.route("/user/<username>")
def user(username):
    return render_template('user.html', name=username)

@app.route("/people")
def people():
    people = {
    "user_name1": 20,
    "user_name2": 30
    }
    return jsonify(people)



app.run(debug=True)
