from flask import jsonify, render_template, url_for
from .import bp as app


@app.route('/users')
def get_users():
    return jsonify({'message': 'This works!'})


@app.route('/profile')
def profile():
    logged_in_user = 'Matt'
    return render_template('profile.html', u=logged_in_user)


@app.route('/contact')
def contact():
    return "This is the contact page."
