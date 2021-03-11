from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField
from wtforms.validators import Required

class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.',validators = [Required()])
    submit = SubmitField('Submit')
    
class BlogForm(FlaskForm):
    blog_title = TextAreaField('Title for your blog',validators=[(Required())])
    blog_description = TextAreaField('Summary of your blog', validators=[(Required())])
    blog_source = TextAreaField('Source for your blog information',validators=[(Required())])
    submit = SubmitField('Post Blog')