# app.py
import os
from flask import Flask

# Create Flask application
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, JYOTHISH !!!'

@app.route('/health')
def health_check():
    return {'status': 'healthy', 'message': 'Flask app is running!'}

if __name__ == '__main__':
    # Get port from environment variable (Render will set this)
    # port = int(os.environ.get('PORT', 5000))

    app.run(host='0.0.0.0', port=5000, debug=False)
