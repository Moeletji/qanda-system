# -*- coding: utf-8 -*-
from flask import (render_template, url_for, flash,
                   redirect, request, abort, Blueprint)
from flask_login import current_user, login_required
from flaskblog import db
from flaskblog.models import Post, UserAnswer
from flaskblog.posts.forms import PostForm, AnswerForm
    
posts = Blueprint('posts', __name__)

@posts.route("/posts/new", methods=['GET','POST'])
@login_required
def new_post():
    form = PostForm()
    if form.validate_on_submit():
        post = Post(title=form.title.data, content=form.content.data, question_type=form.question_type.data, author=current_user)
        db.session.add(post)
        db.session.commit()
        flash('Your question has been created!', 'success')
        return redirect(url_for('main.home'))
    return render_template('create_post.html', title='Post New Question',
                           form=form, legend="Post New Question")  
    
@posts.route("/posts/<int:post_id>")
def post(post_id):
    post = Post.query.get_or_404(post_id)
    return render_template('post.html', title=post.title, post=post)

@posts.route("/posts/<int:post_id>/update", methods=['GET','POST'])
@login_required
def update_post(post_id):
    post = Post.query.get_or_404(post_id)
    if post.author != current_user:
        abort(403)
    form = PostForm()
    if form.validate_on_submit():
        post.title = form.title.data
        post.content = form.content.data
        post.question_type = form.question_type.data
        db.session.commit()
        flash('Your question has been updated!', 'success')
        return redirect(url_for('posts.post', post_id=post.id))
    elif request.method == 'GET':
        form.title.data = post.title
        form.content.data = post.content
        form.question_type.data = post.question_type
    return render_template('create_post.html', title='Update Question',
                           form=form, legend="Update Question")
    
@posts.route("/posts/<int:post_id>/delete", methods=['POST'])
@login_required
def delete_post(post_id):
    post = Post.query.get_or_404(post_id)
    if post.author != current_user:
        abort(403)
    db.session.delete(post) 
    db.session.commit()
    flash('Your question has been deleted!', 'success')
    return redirect(url_for('main.home'))

