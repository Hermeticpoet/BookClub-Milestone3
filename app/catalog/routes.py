from app.catalog import main
from app import db
from app.catalog.models import Book, Publication
from flask import render_template, flash, request, redirect, url_for
from flask_login import login_required
from app.catalog.forms import EditBookForm


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
