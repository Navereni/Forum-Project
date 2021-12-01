from application import db

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(160), nullable=False)
    author = db.Column(db.String(15), nullable=False)
    date_posted = db.Column(db.DateTime), nullable=False)
    category = db.Column(db.String(10), nullable=False)
    department = db.Column(db.String(15), nullable=False)

    comments = db.relationship('Comments', backref='posts')

class Comment(db.Model):
    id = id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(160), nullable=False)
    author = db.Column(db.String(15), nullable=False)
    date_posted = db.Column(db.DateTime), nullable=False)
    post_id = db.Column(db.Integer, db.ForeignKey('post.id'))