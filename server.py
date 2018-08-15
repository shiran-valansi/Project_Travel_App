"""TravelApp"""

from jinja2 import StrictUndefined

from flask import Flask, request, jsonify, render_template, redirect, flash, session
from flask_debugtoolbar import DebugToolbarExtension

from model import connect_to_db, db, User, Pinpoint
# import model

import os 

app = Flask(__name__)

# Required to use Flask sessions and the debug toolbar
app.secret_key = "ABC"

# Normally, if you use an undefined variable in Jinja2, it fails silently.
# This is horrible. Fix this so that, instead, it raises an error.
app.jinja_env.undefined = StrictUndefined



@app.route('/')
def index():
    """Homepage."""

    return render_template("maptry.html", key=os.environ['GOOGLE_API_KEY'])


@app.route('/search')
def index2():
    """testing search box."""

    return render_template("search_box.html", key=os.environ['GOOGLE_API_KEY'])



@app.route('/login')
def login_page():
    return render_template("login.html")



@app.route('/register', methods=["GET"])
def show_regestration_form():
    """Show registration form for new users"""
    return render_template("register.html")


@app.route("/register", methods=["POST"])
def process_new_user():
    fname = request.form.get("fname")
    lname = request.form.get("lname")
    email = request.form.get("email")
    password = request.form.get("password")

    # query the db for user email
    check_email = User.query.filter(User.email==email).first()
    # check_email = True when there's a record. 

    if not check_email:
        new_user = User(fname=fname, lname=lname, email=email, password=password)
        db.session.add(new_user)
        db.session.commit()
        flash("You're now registered!")
    else:
        flash("You've already registered, please login")


    return render_template(menu.html)

@app.route("/add-pinpoint", methods=['POST'])
def add_latlng():
    print("inn add_latlng")
    # latlng= request.form.get("latlng")
    pp_name= request.form.get("ppName")

    # lat = latlng.split(",")[0][1:]
    # lng = latlng.split(",")[1][:-1]


    # new_pinpoint=Pinpoint(pp_name=pp_name, lat=lat, lng=lng)
    new_pinpoint=Pinpoint(pp_name=pp_name)
    db.session.add(new_pinpoint)
    db.session.commit()


    return "got latlng and pinpoint"

if __name__ == "__main__":
    # We have to set debug=True here, since it has to be True at the point
    # that we invoke the DebugToolbarExtension
    app.debug = True

    connect_to_db(app)

    # Use the DebugToolbar
    DebugToolbarExtension(app)

    app.run(host="0.0.0.0", port="5001")
