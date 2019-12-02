from app import create_app


# We can now simply pass whatever version of the app we wish to run into the function
if __name__ == "__main__":
    flask_app = create_app("dev")
    flask_app.run()

