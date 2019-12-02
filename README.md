# Milestone Project 3 | Book Club

## Scalable Architecture

One package per functionality. We can now simply add more packages as needed.
Packages are also available to be reused as needed. Each package is self sufficient.
You can plug in these packages into other python applications if wanted to reuse
again in another project.

## Technologies Used

* HTML5
* CSS3
* Flask-Bootstrap (framework)
* Python
* Flask
* PostgreSQL 12.1
* S3 (image storage)
* Heroku
* Github
* Git
* PyCharm (code editor)
* SQLAlchemy (ORM)
* Virtual Environment (venv)

## PostGreSQL Database

version: PostgreSQL 12.1 / PostGIS 3.0.0 / plv8 2.3.13
Also installed psycopg2-binary==2.8.4 in order to run PostGreSQL
Installed pgAdmin4 to administer PostGreSQL database.

### Images

The svg images where taken from a free to use site: [flaticon](https://www.flaticon.com/)
The images are stored locally in the static folder in the img directory. I will attempt
to set up S3 for storing user uploaded images but if that is not possible then
I will stick with the local folder storage and come back to the set up of S3 at
a later date.

#### Credits

Assistance for this project was provided by Code Institute tutor Michael. I also
borrowed heavily from a number of online tutorials, including Michael Schafer's
[Flask Web App Tutorial series](https://www.youtube.com/watch?v=MwZwr5Tvyxo&t=37s), Anthony Herbert from [Pretty Printed](https://www.youtube.com/watch?v=EnJKHVEzHFw), Udemy courses [Python Flask Web Apps](https://www.udemy.com/course/python-flask-beginners/)
by Frank Anemaet and [Python Flask for Beginners](https://www.udemy.com/course/python-flask-beginners/) by 
Ioannis Giftakis. 
