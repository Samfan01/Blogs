from flask import render_template
from . import main


#Views
@main.route('/')
def index():
    '''
    view root page function that returns the index page and its
    data
    '''
    title = 'Home - Welcome to Douglas Samphan Blog Spot.'
    
    return render_template('index.html',title = title)

@main.route('/my_story')
def my_story():
    '''
    view root page function that returns the my_story page and its data
    '''
    title = "Blogers' Life Story."
    return render_template('my_story.html',title = title)