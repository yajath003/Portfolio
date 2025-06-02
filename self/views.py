from flask import Blueprint, render_template, redirect, session, request, url_for, flash
from werkzeug.utils import secure_filename


from application import db

self_app = Blueprint('self_app', __name__)


@self_app.route('/')
def index():
    return render_template('index.html')


@self_app.route('/projects')
def projects():
    return render_template('projects.html')


@self_app.route('/skills')
def skills():
    return render_template('skills.html')


@self_app.route('/certification')
def certification():
    return render_template('certification.html')


@self_app.route('/work')
def work():
    return render_template('work.html')


if __name__ == '__main__':
    app.run(debug=True)


