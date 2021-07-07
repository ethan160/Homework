from flask import jsonify, render_template, url_for
from .import bp as app

posts = [
    {
        'id': 1,
        'body': 'This is the first blog post',
        'author': 'Licas L',
        'timestamp': '10-12-2020',
        'items': {
                'health': 10,
                'mana': 5
        }
    },

    {
        'id': 2,
        'body': 'This is the second blog post',
        'author': 'Ethan J',
        'timestamp': '10-25-2020',
        'items': {
                'health': 10,
                'mana': 5
        }
    },

    {
        'id': 3,
        'body': 'This is the third blog post',
        'author': "Cool E",
        'timestamp': '10-23-2020',
        'items': {
                'health': 10,
                'mana': 10
        }
    }
]


@app.route('/')
def home():
    context = {
        'posts': posts
    }
    return render_template('home.html', **context)

@app.route('/profile')
def profile():
    logged_in_user = 'Ethan'
    return render_template('profile.html', u=logged_in_user)


@app.route('/contact')
def contact():
    return "This is the contact page."
