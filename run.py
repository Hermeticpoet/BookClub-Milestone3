from app import create_app, db
from app.auth.models import User

# We can now simply pass whatever version of the app we wish to run into the function
if __name__ == "__main__":
    flask_app = create_app("dev")
    with flask_app.app_context():
        db.create_all()
        if not User.query.filter_by(user_name="harry").first():
            User.create_user(user='harry',
                              email='harry@gmail.com',
                             password='secret')
    flask_app.run()




