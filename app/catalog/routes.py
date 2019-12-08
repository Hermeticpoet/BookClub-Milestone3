from app.catalog import main
from app import db
from app.catalog.models import Book, Publication
from flask import render_template, flash, request, redirect, url_for
from flask_login import login_required
from app.catalog.forms import EditBookForm, CreateBookForm


@main.route("/")
def display_books():
    books = Book.query.all()
    return render_template("home.html", books=books)


"""
Any decorators that take an id variable must have that variable
passed to the function as well. For example, both publisher_id
and book_id must be placed in the route, inside <> angle brackets,
while then being passed to the functions as arguments too.
"""
@main.route("/display/publisher/<publisher_id>")
def display_publisher(publisher_id):
    publisher = Publication.query.filter_by(id=publisher_id).first()
    publisher_books = Book.query.filter_by(pub_id=publisher.id).all()
    return render_template("publisher.html", publisher=publisher, publisher_books=publisher_books)


@main.route("/book/delete/<book_id>", methods=["GET", "POST"])
@login_required
def delete_book(book_id):
    book = Book.query.get(book_id)
    if request.method == "POST":
        db.session.delete(book)
        db.session.commit()
        flash("Book deleted successfully")
        return redirect(url_for("main.display_books"))
    return render_template("delete_book.html", book=book, book_id=book.id)


@main.route("/book/edit/<book_id>", methods=["GET", "POST"])
@login_required
def edit_book(book_id):
    book = Book.query.get(book_id)
    form = EditBookForm(obj=book)
    if form.validate_on_submit():
        book.title = form.title.data
        book.author = form.author.data
        book.format = form.format.data
        book.num_pages = form.num_pages.data
        db.session.add(book)
        db.session.commit()
        flash("Book Updated Successfully")
        return redirect(url_for("main.display_books"))
    return render_template("edit_book.html", form=form, book=book)


'''
In order to create a book, we need a pub_id because book cannot exist without a publisher. User must be
logged in to use this functionality - `@login_required`. If the user makes a GET request then the create_book
html page will display with an empty form. However, if it is a POST request, after details have been filled
in the form fields, then each of the data fields are passed to their corresponding fields within the database
in order to create a new record. Once this has been done successfully, the user will get a success message
and then they will be redirected to the publisher's page with their new record visible to them.
'''
@main.route("/create/book/<pub_id>", methods=["GET", "POST"])
@login_required
def create_book(pub_id):
    form = CreateBookForm()
    form.pub_id.data = pub_id  # pre-populates this ID
    if form.validate_on_submit():
        book = Book(title=form.title.data, author=form.author.data, avg_rating=form.avg_rating.data,
                    book_format=form.format.data, image=form.image_url.data, num_pages=form.num_pages.data,
                    pub_id=form.pub_id.data)
        db.session.add(book)
        db.session.commit()
        flash("Book Added Successfully")
        return redirect(url_for("main.display_publisher", publisher_id=pub_id))
    return render_template("create_book.html", form=form, pub_id=pub_id)
