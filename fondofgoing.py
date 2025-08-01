
from flask import Flask, render_template

app = Flask(__name__)
from flask_bootstrap import Bootstrap5
Bootstrap5(app)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/about/')
def about():
    return 'This is the about page'

@app.route('/contact_us/')
def contact_us():
    return render_template("contact_us.html")

if __name__ == "__main__":
    app.run(debug=True)

    # test privacykjkjh