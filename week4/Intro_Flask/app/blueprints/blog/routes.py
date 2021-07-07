from flask import render_template, url_for
from .import bp as app
# from app.blueprints.blog.routes import posts



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


# @app.route('/')
# def home():
#     context = {
#         'posts': posts
#     }
#     return render_template('home.html', **context)


@app.route('/blog/<int:id>')
def get_post(id):
    for p in posts:
        if p['id'] == id:
            post = p
            break

    context = {
        'p': post
    }
    return render_template('blog-single.html', **context)

