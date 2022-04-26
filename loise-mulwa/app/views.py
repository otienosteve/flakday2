from flask import render_template
from . import app

@app.route('/')
def home():
    return render_template('index.html') 

@app.route('/about')
def about():
    return render_template('about.html') 

@app.route('/facts')
def facts():
    return render_template('facts.html') 