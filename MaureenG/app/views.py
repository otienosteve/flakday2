from app import app
from flask import render_template

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/products')
def products():
    return render_template('products.html')

@app.route('/contacts')
def contacts():
    return render_template('contacts.html')


if __name__=='__main__':
    app.run(debug=True)