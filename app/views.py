from flask import render_template
from app import app


#Views
@app.route('/')
def index():
    '''
    view root page function that returns the index page and its
    data
    '''
    title = 'Home - Welcome to Douglas Samphan Blog Spot.'
    
    return render_template('index.html',title = title)