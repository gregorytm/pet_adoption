from flask import Flask, request, redirect, session, render_template, url_for, flash
from flask_debugtoolbar import DebugToolbarExtension
from flask_sqlalchemy import SQLAlchemy
from models import db, connect_db, Pet
from forms import PetForm

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///pet_adoption'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = "David-Lynch-coffee-886"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
debug = DebugToolbarExtension(app)

connect_db(app)

@app.route('/')
def home_page():
    pets=Pet.query.all()
    return render_template('home.html', pets=pets)

@app.route('/add', methods=["GET", "POST"])
def add_pet():
    form = PetForm()
    if form.validate_on_submit():
        name = form.name.data 
        species = form.species.data
        photo_url = form.photo_url.data
        age = form.age.data
        notes = form.notes.data
        
        pet = Pet(name=name, species=species, photo_url=photo_url, age=age, notes=notes)
        db.session.add(pet)
        db.session.commit()
        
        flash(f"Added {name}, age {age} to database")

        return redirect('/')
    else:
        return render_template('add.html', form=form)

@app.route('/pet/<int:id>/edit', methods=["GET", "POST"])
def edit_pet(id):
    pet=Pet.query.get_or_404(id)
    form = PetForm(obj=pet)

    if form.validate_on_submit():
        pet.name = form.name.data
        pet.species = form.species.data
        pet.photo_url = form.photo_url.data
        pet.age = form.age.data
        pet.notes = form.notes.data

        db.session.commit()
        return redirect('/')
    else:
        return render_template('edit_pet_form.html', form=form)

@app.route('/pet/<int:id>')
def show_pet(id):
    """show details about one pet"""
    pet = Pet.query.get_or_404(id)
    return render_template("details.html", pet=pet)

@app.route('/pet/<int:id>/delete')
def delete_pet(id):
    pet = Pet.query.get_or_404(id)
    db.session.delete(pet)
    db.session.commit()

    return redirect("/")