from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, DateTimeField
from wtforms.validators import DataRequired

class CreatePostForm(FlaskForm):
    title = StringField("Your Post", validators=[DataRequired()])
    datetime = DateTimeField("Date Posted")
    submit = SubmitField("Add Post")


class CreateCommentForm(FlaskForm):
    comment = StringField("Your Comment", validators=[DataRequired()])
    posts = SelectField("Posts", validators=[DataRequired()], choices=[])
    submit = SubmitField("Add Comment")