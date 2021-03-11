from flask import render_template,request,redirect,url_for,abort
from . import main
from flask_login import login_required
from ..models import User
from .forms import UpdateProfile,BlogForm
from .. import db,photos

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

@main.route('/user/<uname>/update',methods = ['GET','POST'])
@login_required
def update_profile(uname):
    user = User.query.filter_by(username = uname).first()
    if user is None:
        abort(404)
        
    form = UpdateProfile()
    
    if form.validate_on_submit():
        user.bio = form.bio.data
        
        db.session.add(user)
        db.session.commit()
        
        return redirect(url_for('.profile',uname = user.username))
    
    return render_template('profile/update.html',form = form)

@main.route('/user/<uname>/update/pic',methods = ['POST'])
@login_required
def update_pic(uname):
    user = User.query.filter_by(username = uname).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profil_pic_path = path
        db.session.commit()
        
    return redirect(url_for('main.profile',uname = uname))

@main.route('/blog')
def blog():
    '''
    vie function that returns the blog page and its data
    '''
    
    return render_template('blog.html')

@main.route('/blog/new<title>',methods = ['GET','POST'])
@login_required
def new_blog(title):
    form = BlogForm
    
    if form.validate_on_submit():
        blog_title = form.title.data
        blog_description = form.description.data
        blog_source = form.source.data
        
        #updated new blog instance
        new_blog = Blog(blog_title=blog_title,blog_description=blog_description,blog_source=blog_source)
        
        #save blog method
        new_blog.save_blog()
        return redirect(url_for('.blog',blog_title=blog_title))
    
    return render_template('new_blog.html',blog_form = form)

