import mqsql.connector 
import pandas as pd
from flask import Flask, render_template, SQLAlchemy, request, redirect


app = Flask(__name__)
app.config[SQLALCHEMY_DATABASE_URI] = mysql://username:password@server/db
db = SQLAlchemy(app)

connection = mysql.connector.connect(
    host="localhost",
    user="your_username",  # MySQL username
    password="your_password",  # MySQL password
    database="school_db"
)

@app.route("/home/")
def home_page():
    return render_template("index.html")

@app.route("/start_practical/")
def start_prac():
    return render_template("start_prac.html")

@app.route("/student_record/")
def student_record():
    return render_template("student_record.html")


app.run(debug=True, port = 80)
