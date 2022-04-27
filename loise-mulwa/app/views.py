from flask import render_template
from . import app

@app.route('/')
def home():
    return render_template('index.html') 

@app.route('/about')
def about():
    return render_template('about.html') 

@app.route('/gallery')
def gallery():
    return render_template('gallery.html') 