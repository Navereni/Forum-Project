from werkzeug.wrappers import response
from application import app
from application.forms import CreatePostForm
from flask import render_template, request, redirect, url_for, jsonify
import requests

backend_host = "forum-project_backend:5000"

@app.route('/', methods=['GET'])
@app.route('/home', methods=['GET'])
def home():
    posts = requests.get(f"http://{backend}/read/allPosts").json()["posts"]
    return render_template('index.html', title="Home", posts=posts)

# @app.route('/create/post', methods=['GET','POST'])
# def create_post():
#     form = CreatePostForm()

#     if request.method == "POST":
#         response = request.post(
#             f"http://{backend}create/post",
#             json={
#                 "name"
#             }
#         )
  

# @app.route('/update/task/<int:id>', methods=['GET','POST'])
# def update_task(id):
#     form = TaskForm()
#     task = requests.get(f"http://{backend_host}/read/task/{id}").json()

#     if request.method == "POST":
#         response = requests.put(f"http://{backend_host}/update/task/{id}",json={"description": form.description.data})
#         return redirect(url_for('home'))

#     return render_template('update_task.html', task=task, form=form)

# @app.route('/delete/task/<int:id>')
# def delete_task(id):
#     response = requests.delete(f"http://{backend_host}/delete/task/{id}")
#     return redirect(url_for('home'))