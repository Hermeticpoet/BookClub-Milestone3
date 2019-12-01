from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime


app = Flask(__name__)


app.config.update(
    SECRET_KEY="topsecret",
    SQLALCHEMY_DATABASE_URI="postgresql://postgres:topsecret@localhost/catalog_db",
    SQLALCHEMY_TRACK_MODIFICATIONS=False
)

db = SQLAlchemy(app)


@app.route('/')
def hello_world():
    return 'Hello Cunts!!'


class Publication(db.Model):
    __tablename__ = "publication"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)

    def __init__(self, id, name):
        self.id = id
        self.name = name

    def __repr__(self):
        return "The id is {}, Name is {}".format(self.id, self.name)


class Book(db.Model):
    __tablename__ = "book"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False, index=True)  # Adding index aids in speeding up retrieval from DB
    author = db.Column(db.String(50), nullable=False)
    avg_rating = db.Column(db.Float)
    format = db.Column(db.String(50))
    image = db.Column(db.String(100), unique=True)  # Path to the image, not actual image itself
    num_pages = db.Column(db.Integer)
    pub_date = db.Column(db.DateTime, default=datetime.utcnow())

    # Relationship
    pub_id = db.Column(db.Integer, db.ForeignKey("publication.id"))

    def __init__(self, title, author, avg_rating, format, image, num_pages, pub_id):

        self.title = title
        self.author = author
        self.avg_rating = avg_rating
        self.format = format
        self.image = image
        self.num_pages = num_pages
        self.pub_id = pub_id

    def __repr__(self):
        return "{} by {}".format(self.title, self.author)



if __name__ == '__main__':
    db.create_all()
    app.run()
