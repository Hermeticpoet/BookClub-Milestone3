from flask import render_template, request, flash, redirect, url_for
from flask_login import login_user, logout_user
from app.auth.forms import RegistrationForm, LoginForm
from app.auth import authentication as at
from app.catalog import main
from app.auth.models import User

'''
Both of these functions are using objects imported from the "app.auth.forms" module.
They each include our validate_on_submit method to check if the user or their email
and password already exists. The registration form will then create the user if one 
does not already exist. It uses the data from the corresponding form fields to do so.
A flash message is used in both functions to notify the user if their registration or
login has been successful or something went wrong. They then redirect or render the
correct page for the user to move forward. The log_user_in function also makes use
of the check_password method to test the user is entering a correct password. Once a 
user is logged in, they are redirected to the main home page. However, if anything
has failed, they will simply be returned to the login page they are on to attempt to
log in once again.
'''
@at.route("/register", methods=["GET", "POST"])
def register_user():
    form = RegistrationForm()
    if form.validate_on_submit():
        User.create_user(
            user=form.name.data,
            email=form.email.data,
            password=form.password.data)
        flash("Registration Successful")
        return redirect(url_for("authentication.log_user_in"))
    return render_template("registration.html", form=form)


@at.route("/login", methods=["GET", "POST"])
def log_user_in():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(user_email=form.email.data).first()
        if not user or not user.check_password(form.password.data):
            flash("Invalid Credentials. Please try again.")
            return redirect(url_for("authentication.log_user_in"))

        login_user(user, form.stay_logged_in.data)
        return redirect(url_for("main.display_books"))

    return render_template("login.html", form=form)
