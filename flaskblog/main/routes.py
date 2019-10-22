# -*- coding: utf-8 -*-
from flask import render_template, request, Blueprint, flash, redirect, url_for
from flaskblog.models import Post, UserAnswer
from flaskblog.posts.forms import AnswerForm
from flask_login import current_user, login_required
from flaskblog import db

main = Blueprint('main', __name__)

@main.route("/")
@main.route("/home")
def home():
    page = request.args.get('page', 1, type=int)
    posts = Post.query.order_by(Post.date_posted.desc()).paginate(page=page, per_page=5)
            
    return render_template('home.html', posts=posts)

@main.route("/home/test", methods=['GET','POST'])
@login_required
def new_test():
    page = request.args.get('page', 1, type=int)
    posts = Post.query.order_by(Post.date_posted.desc()).paginate(page=page, per_page=5)
    form = AnswerForm()
    return render_template('user_answer.html', posts=posts, form=form) 
        
        
@main.route("/home/user/results")
@login_required
def new_answers(form):
    if form.validate_on_submit():
        answers = UserAnswer(answer=form.answer.data)
        db.session.add(answers)
        db.session.commit()
        flash('Your answers have been submitted', 'success')
        return redirect(url_for('main.new_answers'))
    return render_template('user_results.html')


@main.route("/about")
def about():
    return render_template('about.html', title='About')


