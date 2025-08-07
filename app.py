# app.py
from flask import Flask

# Import the Blueprint from the routes module.
# Assuming your previous code is now saved in a file named 'routes.py'
from routes import app as routes_blueprint

def create_app():
    """Create and configure the Flask application."""
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'your-secret-key-here'  # You need a secret key for sessions

    # Register the Blueprint with the main application
    app.register_blueprint(routes_blueprint)

    return app

# Gunicorn will look for a callable 'app' object.
# We create it by calling our factory function.
app = create_app()

if __name__ == '__main__':
    # This block is for running the app locally with 'python app.py'
    app.run(debug=True)
