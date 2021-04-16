from flask import Flask
from webapp.model import db


def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('config.py')
    db.init_app(app)
    # all_posts = Post.query.all()
    # print(all_posts)
    return app
