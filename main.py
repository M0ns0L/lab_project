import mqsql.connector 
import pandas as pd
from flask import Flask, render_template, request, redirect
app = Flask(__name__)
@app.route("/")
connection = mysql.connector.connect(
    host="localhost",
    user="your_username",  # MySQL username
    password="your_password",  # MySQL password
    database="school_db"
)

def home_page():
    return render_template("index.html")
app.run(debug=True)
