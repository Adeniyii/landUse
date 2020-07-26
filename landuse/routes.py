from landuse.models import User, Post
from landuse import app, bcrypt, db, loginManager
from landuse.forms import RegistrationForm, LoginForm
from flask import render_template, url_for, flash, redirect, request
from flask_login import login_user, current_user, logout_user, login_required

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
    if current_user.is_authenticated:
        return redirect(url_for('dashboard'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashedPassword = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashedPassword)
        db.session.add(user)
        db.session.commit()
        flash(f"Your account has been created! You are now able to login", "success")
        return redirect(url_for("login"))
    return render_template("register.html", title="Register", form=form)


@app.route("/login", methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('dashboard'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            # 'args' returns a dictionary, using 'get' returns 'none' if the argument doesnt exist.
            nextPage = request.args.get('next')
            return redirect(nextPage) if nextPage else redirect(url_for("dashboard"))
        else:
            flash(f"Log in Unsuccessful. Please try again.", "danger")
    return render_template("login.html", title="Login", form=form)


@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('home'))


@app.route("/dashboard", methods=["GET", "POST"])
@login_required
def dashboard():
    return render_template("dashboard.html", title="Dashboard")


@app.route("/account", methods=["GET", "POST"])
@login_required
def account():
    return render_template("account.html", title="Account")
