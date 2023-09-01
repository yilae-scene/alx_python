"""
a simple basic server creation with a route to the one page
"""
from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def index():
    return "Hello HBNB!"
@app.route("/hbnb", strict_slashes=False)
def index():
    return "HBNB!"


if __name__ == "__main__":
    # web application must be listening on 0.0.0.0, port 5000

    app.run(debug=True, host="0.0.0.0")
