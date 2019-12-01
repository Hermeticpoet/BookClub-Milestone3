from flask import Flask
from flask_sqlalchemy import SQLAlchemy




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



if __name__ == '__main__':
    db.create_all()
    app.run()
