from werkzeug.wrappers import response
from application import app
from application.forms import CreatePostForm, CreateCommentForm
from flask import render_template, request, redirect, url_for, jsonify
import requests
from os import getenv

backend = "forum-project_backend:5000"


@app.route('/', methods=['GET'])
@app.route('/home', methods=['GET'])
def home():
    posts = requests.get(f"http://{backend}/read/allPosts").json()["posts"]
    comments = requests.get(f"http://{backend}/read/allPosts").json()
    return render_template('index.html', title="Home", posts=posts)

@app.route('/create/post', methods=['GET','POST'])
def create_post():
    form = CreatePostForm()

    json = requests.get(f"http://{backend}/read/allPosts").json()

    json["posts"]

    if request.method == "POST":
        response = requests.post(
            f"http://{backend}/create/post",
            json={
                "title": form.title.data,
                "post_text": form.post_text.data,
                "author": form.author.data,
                "date_posted": form.datetime.data,
                "category": form.category.data
            }
        )
        app.logger.info(f"Response: {response.text}")
        return redirect(url_for("home"))
  
    return render_template("create_post.html", title="Add Post", form=form)

@app.route('/create/comment', methods=['GET','POST'])
def create_comment():
    form = CreateCommentForm()

    json = requests.get(f"http://{backend}/read/allPosts").json()
    for post in json["posts"]:
        form.posts.choices.append((post["id"], post["title"], post["text"]))

    if request.method == "POST":
        response = requests.post(
            f"http://{backend}/create/comment/{form.posts.data}",
            json={
                "comment": form.comment.data
            }
        )
        app.logger.info(f"Response: {response.comment}")
        return redirect(url_for("home"))

    return render_template("create_comment.html", title="Add Comment", form=form)

@app.route('/update/posts', methods=['GET','POST'])
def update_post(id):
    form = CreatePostForm()
    post = requests.get(f"http://{backend}/update/posts").json()

    if request.method == "POST":
        response = requests.put(f"http://{backend}/update/posts",json={"text": form.post_text.data})
        return redirect(url_for('home'))

    return render_template('update_post.html', post=post, form=form)

# @app.route('/delete/task/<int:id>')
# def delete_task(id):
#     response = requests.delete(f"http://{backend}/delete/task/{id}")
#     return redirect(url_for('home'))