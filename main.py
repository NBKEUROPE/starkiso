from flask import Flask
from iso_server.server import start_iso_server
from app.py import app as flask_app

app = Flask(__name__)
app.secret_key = 'blackrock-secret'

# Mount Flask blueprint
app.register_blueprint(flask_app)

if __name__ == '__main__':
    start_iso_server()  # ISO TCP Server
    app.run(debug=True, host='0.0.0.0', port=5000)
