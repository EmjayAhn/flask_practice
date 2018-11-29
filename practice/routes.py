from flask import *
app = Flask(__name__)

@app.route("/")
def home():
    return render_template('home.html')

@app.route("/link1")
def link_1():
    return render_template('link1.html')

app.run(debug=True)
