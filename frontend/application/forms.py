from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, DateTimeField
from wtforms.validators import DataRequired

class CreatePostForm(FlaskForm):
    title = StringField("Your Title", validators=[DataRequired()])
    text = StringField("Your Post", validators=[DataRequired()])
    author = StringField("Your Name", validators=[DataRequired()])
    datetime = DateTimeField("Date Posted")
    type = SelectField("Category", validators=[DataRequired()],
        choices=[
            ("Help", "Help"),
            ("Fun", "Fun"),
            ("Work", "Work")
        ]
    )
    submit = SubmitField("Add Post")


class CreateCommentForm(FlaskForm):
    text = StringField("Your Comment", validators=[DataRequired()])
    author = StringField("Your Name", validators=[DataRequired()])
    submit = SubmitField("Add Comment")