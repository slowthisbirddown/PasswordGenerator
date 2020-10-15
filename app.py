##
from flask import Flask
import PasswordGenerator

app = Flask(__name__)

@app.route('/')
def hello_world():
    return "Hey Adam"

@app.route('/<int:length>')    
def generate_password(length):
    pg = PasswordGenerator.PasswordGenerator()
    return pg.generate_password(length)
    