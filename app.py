import os
from flask import Flask
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)

app.config['SECRET_KEY'] = os.getenv("SECRET_KEY")

@app.route("/")
@app.route("/home")
def home():
    return "<h1>Home Page</h1>"

@app.route("/about")
def about():
    return "<h1>About Page</h1>"


# modules are named "__main__" when run directly with python
if __name__ == '__main__':
    app.run(debug=True)
