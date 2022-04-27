from flask import Flask, render_template
from app import app

@app.route('/')
def index():
    name = 'Joy'
    return render_template('index.html', name = name)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/project')
def project():
    ls = ['JoJo Pizza', 'Delani Studio', 'Akan Reveal', 'Quotes', ' Portfolio ']
    return render_template('project.html', names= ls)
