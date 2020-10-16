from flask import Flask, render_template, request, flash, redirect
import PasswordGenerator

app = Flask(__name__)
app.secret_key = "380n70f4"

@app.route('/', methods=["GET", "POST"])
def index():
    if request.method == 'POST':
        try:
            length = int(request.form['length'])
            pg = PasswordGenerator.PasswordGenerator()
            password = pg.generate_password(length)
            flash(password)
            return redirect("/")
        except:
            # TODO Flask Flash an error message
            return "Length is not an integer."
    else:
        return render_template('index.html')

@app.route('/<int:length>')
def generate_password(length):
    pg = PasswordGenerator.PasswordGenerator()
    return pg.generate_password(length)
