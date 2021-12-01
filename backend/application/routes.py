from application import app, db
from application.models import Tasks
from flask import render_template, request, redirect, url_for, Response, jsonify

@app.route('/create/post', methods=['POST'])
def create_post():
    package = request.json
    new_task = Tasks(description=package["description"])
    db.session.add(new_task)
    db.session.commit()
    return Response(f"Added task with description {new_task.description}", mimetype='text/plain')

@app.route('/create/comment/<int:post_id>', methods=['POST'])
def create_comment(post_id):
    json = request.json
    new_comment = Comments(
        text = json['text'],
        author = json['author'],
        date_posted = json['date_posted'],
        post_id = post_id
    )
    db.session.add(new.comments)
    db.session.commit()
    return f"Added: {new_comment.text} to the post."

@app.route('/read/allPosts', methods=['GET'])
def read_all_posts():
    all_posts = Posts.query.all()
   json = {"posts": []}
   for post in all_posts:
       comment = []
       for comment in post.comments:
           comments.append(
               {
                   "id": comment.id,
                   "text": comment.text,
                   "author": comment.author,
                   "date_posted": comment.date_posted,
                   "post_id": comment.posts_id,
               }
           )
        json["posts"].append(
            {
                "id": post.id,
                "text": post.text,
                "author": post.author,
                "date_posted": post.date_posted,
                "category": post.category,
                "department": post.department
            }
        )



# @app.route('/update/post/<int:id>', methods=['PUT'])
# def update_task(id):
#     package = request.json
#     task = Tasks.query.get(id)

#     post.description = package['description']
#     db.session.commit()
#     return Response(f"Updated task (ID: {id}) with description {task.description}", mimetype='text/plain')

# @app.route('/delete/post/<int:id>', methods=['DELETE'])
# def delete_task(id):
#     post = Posts.query.get(id)
#     db.session.delete(task)
#     db.session.commit()
#     return Response(f"Task (ID: {id}) has been DELETED!", mimetype='text/plain')
    