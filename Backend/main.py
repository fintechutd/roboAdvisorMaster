from flask import Flask, render_template
from flask_cors import CORS

app = Flask(__name__, template_folder='templates', static_folder='static')

@app.route('/')
def home():
    return "Welcome to FinTech UTD's Spring 2024 Project: Robo-Advisor Platform"

@app.route('/loginPage')
def login():
    return render_template("index.html")

@app.route('/register')
def register():
    return render_template("register.html")

