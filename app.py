##
from flask import Flask, render_template
import PasswordGenerator

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/<int:length>')    
def generate_password(length):
    pg = PasswordGenerator.PasswordGenerator()
    return pg.generate_password(length)
    