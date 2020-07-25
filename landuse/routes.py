from landuse import app
from landuse.models import User, Post
from landuse.forms import RegistrationForm, LoginForm
from flask import render_template, url_for, flash, redirect

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

# this will be the welcome page
@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html", posts=posts)


@app.route("/about")
def about():
    return render_template("about.html", posts=posts, title="About")


@app.route("/register", methods=["GET", "POST"])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f"Account created for {form.username.data}!", "success")
        return redirect(url_for("dashboard"))
    return render_template("register.html", title="Register", form=form)


@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == "l@g.co" and form.password.data == "111":
            flash(f"Successfully logged in {form.email.data}!", "success")
            return redirect(url_for("dashboard"))
        else:
            flash(f"Log in Unuccessful. Please try again.", "danger")
    return render_template("login.html", title="Login", form=form)


@app.route("/dashboard", methods=["GET", "POST"])
def dashboard():
    return render_template("dashboard.html", title="Dashboard")
