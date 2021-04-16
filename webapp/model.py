from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Post(db.Model):
    __tablename__ = 'post'
    id = db.Column(db.Integer, primary_key=True)
    group_id = db.Column(db.Float(), unique=True, nullable=True)
    date = db.Column(db.DateTime, nullable=True)
    name = db.Column(db.String, nullable=True)
    description = db.Column(db.String, nullable=True)
    vk_unique_id = db.Column(db.String, nullable=True)
    # Values after parsing
    price = db.Column(db.Float(), unique=True, nullable=True)
    rooms = db.Column(db.Float(), unique=True, nullable=True)
    neighbours = db.Column(db.Integer(), unique=True, nullable=True)
    is_parcing_successfull = db.Column(db.Boolean(), nullable=True)
    is_rent_room = db.Column(db.Boolean(), nullable=True)

    def __repr__(self):
        return '<Post: {} {}>'.format(self.vk_unique_id, self.description)
