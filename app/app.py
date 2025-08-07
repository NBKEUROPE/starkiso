# app.py
from flask import Flask
from iso_server.server import start_iso_server
from app.routes import app as flask_app

# Create the main Flask application instance
app = Flask(__name__)
# Set a secret key for session management
app.secret_key = 'blackrock-secret'

# Register the Blueprint from app/routes.py
app.register_blueprint(flask_app)

if __name__ == '__main__':
    # This block is for local development only.
    # Gunicorn will not run this part.
    start_iso_server()
    app.run(debug=True, host='0.0.0.0', port=5000)
