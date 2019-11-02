from flask import Flask, render_template, request , url_for , send_from_directory , send_file , flash, redirect
from forms import RegistrationForm, LoginForm
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from random import randint


app = Flask(__name__)
Bootstrap(app)
app.config['SECRET_KEY'] = 'df518855fc0230ff5d0d20cf1035bdab'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///C:/Users/Pratyush/Desktop/DBMS/users.db'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(20), unique = True, nullable = False)
    email = db.Column(db.String(120), unique = True, nullable = False)
    password = db.Column(db.String(80), nullable = False)


@app.route("/")
def home():
    return render_template("home.html")



@app.route("/about")
def about():
    return render_template("sampleabout.html")


@app.route("/register", methods = ["GET","POST"])
def register():
    form = RegistrationForm()
    if request.method == "POST":
        if form.validate_on_submit():
            print("voila")
            new_user = User(username = form.username.data, email = form.email.data, password = form.password.data)
            db.session.add(new_user)
            db.session.commit()
        flash(f"Account Successfully Created for {form.username.data}",'success')
        return redirect("/login")
        
            
    elif request.method == "GET":
        return render_template("registration.html", title = 'Register', form = form) 



@app.route("/login", methods = ['GET', 'POST'])
def login():
    form = LoginForm()
    print("Executing...")
    if form.validate_on_submit():
        print("Form was submitted.")
        if form.email.data == 'mpratyush2016@gmail.com' and form.password.data == 'hello':
            print("Form was validated!")
            flash('You have been logged in!', 'success')
            return redirect("/booking")

        else:
            print(form.errors)
    return render_template("login.html", title = 'Login', form = form)  



@app.route("/booking", methods = ['GET','POST'])
def booking():
    return render_template("booking.html", title = "Booking")


if __name__ == "__main__":
    app.run(debug = True)
