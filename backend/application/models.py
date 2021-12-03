from application import db
from datetime import datetime

class Posts(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(30), nullable=False)
    post_text = db.Column(db.String(160), nullable=False)
    author = db.Column(db.String(15), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.now())
    category = db.Column(db.String(10), nullable=False)

    comments = db.relationship('Comments', backref='posts')

class Comments(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    comment = db.Column(db.String(160), nullable=False)
    comment_author = db.Column(db.String(15), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.now())
    post_id = db.Column(db.Integer, db.ForeignKey('posts.id'))