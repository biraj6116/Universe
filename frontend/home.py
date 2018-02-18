from flask import render_template
from .app import frontend_app


@frontend_app.route('/')
def index():
    return render_template('index.html')


@frontend_app.route('/sample_page')
def sample_page():
    return render_template('sample_page.html')

@frontend_app.route('/page_sample')
def page_sample():
    return render_template('page_sample.html')

