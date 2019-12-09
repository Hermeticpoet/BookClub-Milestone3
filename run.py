from app import create_app, db
from app.auth.models import User
from sqlalchemy import exc


# We can now simply pass whatever version of the app we wish to run into the function
flask_app = create_app("prod")
with flask_app.app_context():
    db.create_all()
    try:
        if not User.query.filter_by(user_name="harry").first():
            User.create_user(user='harry', email='harry@gmail.com', password='secret')
    except exc.IntegrityError:
        flask_app.run()





