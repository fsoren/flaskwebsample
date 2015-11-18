__author__ = 'gptctb'

from flask import Flask, render_template
from flask.ext.script import Manager
from flask.ext.bootstrap import Bootstrap

app = Flask(__name__)
manager = Manager(app)
bootstrap = Bootstrap(app)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/user/<username>')
def user(username):
    return render_template('user.html', username=username)


@app.errorhandler(404)
def page_not_find():
    return render_template('404.html'), 400


@app.errorhandler(500)
def internal_server_error():
    return render_template('500.html'), 500

if __name__ == '__main__':
    app.run(debug=True)
