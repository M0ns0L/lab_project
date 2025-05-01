import mqsql.connector 
import pandas as pd
from flash import Flask, render_template, request, redirect

connection = mysql.connector.connect(
    host="localhost",
    user="your_username",  # MySQL username
    password="your_password",  # MySQL password
    database="school_db"
)

def home():
    return render_template('index.html')
