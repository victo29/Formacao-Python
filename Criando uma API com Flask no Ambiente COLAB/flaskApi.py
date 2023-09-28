from flask import *
from flask_ngrok import run_with_ngrok



app = Flask(__name__)

@app.route('/index')
def home():
    return "Hello World"

run_with_ngrok(app)
app.run()


