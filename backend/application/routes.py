from application import app, db
from application.models import Posts, Comments
from flask import render_template, request, redirect, url_for, Response, jsonify

@app.route('/create/post', methods=['POST'])
def create_post():
    json = request.json
    new_post = Posts(
        title = json["title"],
        date_posted = json["date_posted"],
    )
    db.session.add(new_post)
    db.session.commit()
    return f"Post '{new_post.title}' has been added"

@app.route('/create/comment', methods=['POST'])
def create_comment():
    json = request.json
    new_comment = Comments(
        comment = json['comment'],
        post_id = post_id
     ) 
    db.session.add(new_comment)
    db.session.commit()
    return f"Added comment: {new_comment.comment} to the post."

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
                   "comment": comment.content,
                   "comment_id": comment.comment_id,
                }
            )
        json["posts"].append(
            {
                "id": post.id,
                "title": post.title,
                "date_posted": post.date_posted,
            }
        )
    return jsonify(json)



# @app.route('/update/posts', methods=['PUT'])
# def update_post(id):
#     json = request.json
#     post = Posts.query.get(id)

#     post.text = json['text']
#     db.session.commit()
#     return Response(f"Updated post (ID: {id}) with description {post.post_text}", mimetype='text/plain')

# @app.route('/delete/post/<int:id>', methods=['DELETE'])
# def delete_task(id):
#     post = Posts.query.get(id)
#     db.session.delete(task)
#     db.session.commit()
#     return Response(f"Task (ID: {id}) has been DELETED!", mimetype='text/plain')
    