# Milestone Project 3 | Book Club

## The Brief

To build a Python Flask Web app to be hosted on Heroku platform with fully functioning CRUD capabilities. Data to be housed in a database and then called or presented back to the user through Python queries.


## The Project

I have chosen to build an app for my college friends book club. A place where we could go and upload the 
various books we have read or wish to read. Given that we were all recently in college and spent so much of
our time doing referencing, the goal of this project, is to showcase that particular information that is
relevant to referencing, rather than a blog-like website where we simply review the books on show.

Users will be able to set up an account with fully functioning login in and password storage and retrieval.
Once logged in, they will then be able to upload book details with an image of the book or some corresponding
image that adheres to the sense of the book. It may not necessarily be an image of the actual book cover.

The layout of the site will be pretty basic, stylistically. The application is more of a datastore of books
in a catalogue collection with referencing information more than review, discussions. Therefore, while the
style of the application will be simple, it should also look sleek and modern. For those reasons, the colour 
scheme will be contrasting with dark and light solids. 

Once a user is logged into the application, they will also be able edit and delete records stored on the
database. This functionality will be possible for logged in users who wish to change information about a 
book that was uploaded by another user. As I previously stated, the goal of this application is more in line
a librarian's catalogue and, as such, accuracy of reference information is paramount. It is a shared collection,
database.


## Scalable Architecture

The project will be broken up into modules and then further restructured into packages. One package per 
functional component. That was, I can then simply add more packages as become needed in the future.
Packages are also available to be reused as needed. Each package is self sufficient. You can also plug 
these packages into other python applications if wanted to reuse the components or packages in other packages.


## UX

A book catalogue that can house referencable information about a variety of books in one place.
Simplistic and intuitive design and layout. Clear user prompts for site navigation, if needed.
Security of information storage, particularly email and passwords. A responsive design that allows 
for ease of use on any device and screen. 

The design of the site is largely borrowed from the Udemy course 'Scalable Web Applications with Python'.
I have also used much of the database from that course to populate my own database of books and images.


### Technologies Used

* HTML5
* CSS3
* Flask-Bootstrap (framework)
* Bootstrap4 (framework)
* Python
* Flask
* PostgreSQL 12.1
* S3 (image storage)
* Heroku
* Github
* GUnicorn (python http server)
* Git
* PyCharm (code editor)
* SQLAlchemy (ORM)
* Virtual Environment (venv)

The use of flask-bootstrap has somewhat thrown off my styles. I like the convenient use of in-built Macros
such as, Forms, which builds the forms out nicely, however, my styles are not being applied. I am not as yet
sure whether this is artifact of flask-bootstrap being more suited to Bootstrap3 and I am using Bootstrap4?
I shall continue for now but keep in mind this issue for later resolution. The easier option may just be to
use Bootstrap3 rather than 4 as my framework. If however, I can custom style the forms macros then I will
continue with my use of Bootstrap4 instead.

[GUnicorn]("https://docs.gunicorn.org/en/stable/run.html") is a python http server that is often used to push or
serve applications from local environments to hosting platforms, such as, Heroku.


### PostGreSQL Database

version: PostgreSQL 12.1 / PostGIS 3.0.0 / plv8 2.3.13. Also installed psycopg2-binary==2.8.4 in order 
to run PostGreSQL. Installed pgAdmin4 to administer PostGreSQL database. The database schema is a standard
few tables. There will be tables for Books, Publishers and Users. Each table will have an ID that functions
as the Primary Key, while also containing a Foreign Key that links the tables together. For instance, each
book will have a Primary Key - ID and this ID will used as the Foreign Key in the Publisher table so all
books produced by that publisher can be queried and returned to the user upon request.

See Design Images folder for database schema: [design-imgs](design-imgs/database)

### Issues Resolved

I did have some issues getting a clear answer from the Flask-Bootstrap documentation about how to add custom
classes to their quick_forms() object. I found some great answers however on [StackOverflow]("https://stackoverflow.com/questions/33145556/flask-bootstrap-flask-wtf-adding-class-to-submit-button")
that solved that issue. I did, however, still have to use the `!important` in my css style rules
to override the 'Flask-Bootstrap' btn style of transparent.

There was a problem with the bottom publisher id links not working early on as well. The cursor pointer was not working
and so you could not click on the links. If I opened the code, I could see that the links were there and they were 
clickable. I eventually realised that the footer was collapsing over the bottom of the book container element and so
the links could not be reached. Therefore, I simply added a couple of break tags after the publisher id within
the display books home page and this created better spacing for all the items, as well as correcting for the
issue with the footer blocking the final items links.

### Images

The svg images where taken from a free to use site: [flaticon](https://www.flaticon.com/). 
The images are stored locally in the static folder in the img directory. I will attempt
to set up S3 for storing user uploaded images but if that is not possible then
I will stick with the local folder storage and come back to the set up of S3 at
a later date.

### Features Left to Implement

I had originally began building an 'add_publisher' page with its corresponding routes and classes but time
constraints have meant that I have not been able to do so at this moment. This is something that I will look
to implement at a future date. 

The avg_ratings is a nice enough points score but I would possibly look at making this a checkbox type feature
that user can select or choose a specific icon for a more visual affect. This is not certain as the current
style is more in keeping with the sleek minimalist, librarian-esque UI of the application.

Although I had never really intended to create any kind of Blog Post, review section, I have thought about
a basic summary or more in keeping with the essence of the application, a referencing summary, rather than
a standard review. 


### Deployment

On the Heroku main page click "create new app". Choose a name and server host destination. Then after the app is created, click on resources and type in "postgreSQL" to create a database on the platform for your app. Heroku will automatically then generate all the necessaries for you. When the database is created, you can then click on its link to check out what has been created. From there, is you click the "settings" tab, you further see the credentials for your newly created database. This is information needed to now created the environment variables for your own application. The URI in here is a temporary address, as is stated at the top of the page. For this reason, we must import the "os" into our "dev.py" file - this will not be the "os" for our local machine but the "os" for Heroku. Then, using the `os.environ` dictionary we can tell Heroku to get the ever-changing current database URL when the application is running on the platform.

### Apologies

Unfortunately, due to time constraints with my new job and difficulty experienced during the course. I was unable to complete the material in full. Therefore, given these constraints, I ran into some issues with uploading my database to Heroku. I attempted to do this using AWS S3 Buckets and through the use of a pg_dump file. Both attempts failed and I was not able to resolve the issue in the given time frame. I have had no options at this late stage but to upload my final projects before the deadline closes. I apologize for the unfinished work but I have had no other options available at this time, an extension had already been granted! 

I have included the pg_dump file AND teh dump.sql file that I also attempted to upload to Heroku. These of course contain my database and all its data...

Kind Regards,
Kevin Walton


#### Credits

Assistance for this project was provided by Code Institute tutor Michael. I also borrowed heavily from a number of online tutorials, including Michael Schafer's [Flask Web App Tutorial series](https://www.youtube.com/watch?v=MwZwr5Tvyxo&t=37s), Anthony Herbert from [Pretty Printed](https://www.youtube.com/watch?v=EnJKHVEzHFw), Udemy courses [Python Flask Web Apps](https://www.udemy.com/course/python-flask-beginners/)
by Frank Anemaet and [Python Flask for Beginners](https://www.udemy.com/course/python-flask-beginners/) by Ioannis Giftakis. 

The documentation used throughout this project was invaluable. Those include; [Flask]("https://flask.palletsprojects.com/en/1.1.x/"), [Flask-Login]("https://flask-login.readthedocs.io/en/latest/"),
[Bootstrap4]("https://getbootstrap.com/docs/4.0/getting-started/introduction/"), [Jinja2]("https://jinja.palletsprojects.com/en/2.10.x/") and [Flask-SQLAlchemy]("https://flask-sqlalchemy.palletsprojects.com/en/2.x/"),
[Custom Errors]("https://flask.palletsprojects.com/en/1.1.x/patterns/errorpages/").
