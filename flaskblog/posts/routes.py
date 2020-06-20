from flask import Blueprint, redirect, flash, render_template, request, url_for, abort
from flaskblog import db
from flaskblog.models import Post
from flaskblog.posts.forms import PostForm
from flask_login import current_user, login_required

posts = Blueprint('posts', __name__)


@posts.route('/post/new', methods=['Get', 'Post'])
@login_required
def new_post():
    form = PostForm()
    if form.validate_on_submit():
        the_post = Post(title=form.title.data, content=form.content.data, author=current_user)
        db.session.add(the_post)
        db.session.commit()
        flash('Post has been created', 'success')
        return redirect(url_for('main.home'))
    return render_template('create_post.html', title='New Post', form=form,
                           legend='New Post')


@posts.route('/post/<int:post_id>')
def post(post_id):
    the_post = Post.query.get_or_404(post_id)
    return render_template('post.html', title=the_post.title, post=the_post)


@posts.route('/post/<int:post_id>/update', methods=['Get', 'Post'])
@login_required
def update_post(post_id):
    the_post = Post.query.get_or_404(post_id)
    if the_post.author != current_user:
        abort(403)
    form = PostForm()
    if form.validate_on_submit():
        the_post.title = form.title.data
        the_post.content = form.content.data
        db.session.commit()
        flash('Your post has been updated!', 'success')
        return redirect(url_for('posts.post', post_id=the_post.id))
    elif request.method == 'GET':
        form.title.data = the_post.title
        form.content.data = the_post.content
    return render_template('create_post.html', title='Update Post', form=form,
                           legend='Update Post')


@posts.route('/post/<int:post_id>/delete', methods=['Post'])
@login_required
def delete_post(post_id):
    the_post = Post.query.get_or_404(post_id)
    if the_post.author != current_user:
        abort(403)
    db.session.delete(the_post)
    db.session.commit()
    flash('Your post has been deleted!', 'success')
    return redirect(url_for('main.home'))
