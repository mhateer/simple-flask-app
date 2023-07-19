# Import the necessary modules
from flask import Flask

# Create a Flask application instance
app = Flask(__name__)

# Define a route for the home page
@app.route('/')
def home():
    return 'Hello, welcome to the Simple Flask Application!'

# Define a route for a custom page
@app.route('/custom')
def custom_page():
    return 'This is a custom page!'

# Run the application if this script is executed directly
if __name__ == '__main__':
    app.run(debug=True)
