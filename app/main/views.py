from flask import render_template,request,redirect,url_for,abort
from . import main
from flask_login import login_required
from ..models import User

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

@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username = uname).first()
    
    if user is None:
        abort(404)
        
    return render_template('profile/profile.html', user = user)