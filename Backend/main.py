from flask import Flask, render_template
from flask_cors import CORS

app = Flask(__name__, template_folder='templates', static_folder='static')
CORS(app)

@app.route('/')
def login():
    return render_template("/templates/index.html")

@app.route('/register')
def register():
    return render_template("register.html")

if __name__ == "__main__":
    app.run(debug=True)


