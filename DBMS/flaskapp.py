from flask import Flask, render_template, request , url_for , send_from_directory , send_file , flash, redirect
from forms import RegistrationForm, LoginForm
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
Bootstrap(app)
db = SQLAlchemy(app)

app.config['SECRET_KEY'] = 'df518855fc0230ff5d0d20cf1035bdab'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////C:/Users/Pratyush/Desktop/DBMS/users.db'


@app.route("/")
def home():
    return render_template("sampleabout.html")



@app.route("/about")
def about():
    return render_template("sampleabout.html")



@app.route("/register", methods = ["GET","POST"])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        print("form hogaya")
        return "<h1>"+form.username.data+" "+form.email.data+" "+form.password.data+"</h1>"
    return render_template("sampleregister.html", title = 'Register', form = form)  



@app.route("/login", methods = ['GET', 'POST'])
def login():
    form = LoginForm()
    print("Executing...")
    if form.validate_on_submit():
        print("Form was submitted.")
        if form.email.data == 'mpratyush2008@gmail.com' and form.password.data == 'hello':
            print("Form was validated!")
            flash('You have been logged in!', 'success')
            return "you have logged in!"
        else:
            print(form.errors)
    return render_template("login.html", title = 'Login', form = form)  



@app.route("/booking", methods = ['GET','POST'])
def booking():
    return render_template("booking.html", title = "Booking")


if __name__ == "__main__":
    app.run(debug = True)