from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

###models for pet###

class Pet(db.Model):
    __tablename__="pets"

    def __repr__(self):
        u = self
        return f"<pets id={u.id} name={u.name} species = {u.species} age = {u.age} notes = {u.notes} available = {u.available} pic = {u.image_url}>"
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text, nullable = False, unique=True)
    species = db.Column(db.Text, nullable = False)
    photo_url = db.Column(db.Text, nullable = True)
    age = db.Column(db.Integer, nullable=True)
    notes = db.Column(db.Text, nullable=True)
    available = db.Column(db.Boolean, default=True,)

def connect_db(app):
    db.app = app
    db.init_app(app)
