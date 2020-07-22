import os
from dotenv import load_dotenv
from flask import Flask, render_template, url_for

load_dotenv()
app = Flask(__name__)

app.config['SECRET_KEY'] = os.getenv("SECRET_KEY")


posts = [
    {
        "author": "James Bond",
        "title": "Chronicles of 007",
        "content": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.",
        "date_posted": "July 21, 2020"
    },
    {
        "author": "Rononoa Zoro",
        "title": "Benefits of sake",
        "content": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.",
        "date_posted": "December 21, 2049"
    }
]


@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html", posts=posts)

@app.route("/about")
def about():
    return render_template("about.html", posts=posts, title="About")


# modules are named "__main__" when run directly with python
if __name__ == '__main__':
    app.run(debug=True)
