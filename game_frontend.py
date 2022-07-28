#frontend made with Flask and Flask Login

from flask import Flask, render_template, url_for, request, session, redirect
import sqlite3 
from game_database import users_data, create_user, login_user_db

#init Flask 
app = Flask(__name__)
app.secret_key = "?pު?U???`????ZG??/m??"


#code
@app.route("/")
def home():
    username = ''
    try:
        username = session['username']
    except:
        pass
    return render_template("index.html", username=username)

@app.route("/player/<name>")
def player(name):
    stringreturn = str(users_data(name))
    return stringreturn

@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        error = False
        
        if not username:
            error = "Please enter an username"
        elif not password:
            error = "Please enter an password"
        else:
            error = login_user_db(username, password)
            if error == "Successfully signed in :)":
                session['username'] = username
                return redirect(url_for('home'))

        return render_template("login.html", error=error)        
            

    else:
        return render_template("login.html")

@app.route("/logout")
def logout():
    session.pop('username', None)
    return redirect(url_for('home'))

@app.route("/register", methods=["POST", "GET"])
def register():
    if request.method == "POST":
        username = request.form["username"]
        email = request.form["email"]
        password = request.form["password"]

        error = None

        if not username:
            error = "Please enter an username"
        elif not email:
            error = "Please enter an email"
        elif not password:
            error = "Please enter an password"
        elif len(password) < 8:
            error = "Your password must be above 8 characters"
        else:
            try:
                create_user(username, email, password)
                error = "Registration successfull. Please login"
            except:
                error = "Username or email is already used"
        
        return render_template("register.html", error= error)
        
    else:
        return render_template("register.html")

@app.route("/privacy-policy")
def privacy_policy():
    return render_template("privacy-policy.html")

@app.route("/terms-and-conditions")
def terms_and_conditions():
    return render_template("terms-and-conditions.html")


if __name__ == "__main__":
    app.run()