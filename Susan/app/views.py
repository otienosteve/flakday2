from flask import render_template
from app import app

# Views
@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    return render_template('index.html')

@app.route('/')
def contact():

    '''
    View root page function that returns the contact page and its data
    '''
    return render_template('contact.html')
  
@app.route('/')
def about():

    '''
    View root page function that returns the about page and its data
    '''
    return render_template('about.html')