from app import create_app, db


# We can now simply pass whatever version of the app we wish to run into the function
if __name__ == "__main__":
    flask_app = create_app("dev")
    with flask_app.app_context():
        db.create_all()
    flask_app.run()



