from app import app
from flask import render_template, request, redirect, url_for, flash
from datetime import date


###
# Helper Functions
###

def format_date_joined(join_date):
    return join_date.strftime("%B, %Y")


###
# Routing for your application.
###

@app.route('/')
def home():
    """Render website's home page."""
    return render_template('home.html')


@app.route('/about/')
def about():
    """Render the website's about page."""
    return render_template('about.html', name="Tay Johnson")


@app.route('/profile')
def profile():
    user = {
        "name": "Tay Johnson",
        "username": "tayj",
        "location": "Kingston, Jamaica",
        "bio": "I love building web apps!",
        "posts": 20,
        "followers": 310,
        "following": 180,
        "joined": format_date_joined(date(2022, 9, 1))
    }

    return render_template('profile.html', user=user)


###
# The functions below should be applicable to all Flask apps.
###

@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also tell the browser not to cache the rendered page.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404