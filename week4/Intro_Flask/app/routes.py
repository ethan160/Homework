from app.blueprints.blog import routes
from flask import jsonify, render_template, current_app as app
from app.blueprints.blog.routes import posts

"""
CREATE - POST
READ - GET
UPDATE - PUT
DELETE - DELETE
"""

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

@app.route("/users")
def get_users():
    return jsonify({"message": "This works!"})

# Profile
@app.route("/profile")
def profile():
    logged_in_user = 'Ethan'
    return render_template('profile.html', u=logged_in_user)

# blog
# @app.route("/blog")
# def blog():
#     return "This is all about the app"

# Contact
@app.route("/contact")
def contact():
    return "Get in touch with the team"


@app.route("/shop/products")
def shop_products():
    pass

@app.route("/shop/cart")
def shop_cart():
    pass


@app.route("/shop/success")
def shop_success():
    pass


@app.route("/shop/failure")
def shop_failure():
    pass


@app.route("/shop/checkout")
def shop_checkout():
    pass
