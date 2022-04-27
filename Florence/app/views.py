from flask import render_template
from app import app


@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/services')
def services():
    ls=['To serve','To Inform','To Debunk the Myths','A cocktail of All information']
    return render_template('services.html',values=ls)