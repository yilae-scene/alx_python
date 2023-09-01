"""
a simple basic server creation with a route to the one page
"""
from flask import Flask
from markupsafe import escape

app = Flask(__name__)

# the home page route


@app.route("/", strict_slashes=False)
def index():
    """
    this is a function that has a single slash and 
    is usually reserved for home directory 
    """
    return "Hello HBNB!"

# add another route


@app.route("/hbnb", strict_slashes=False)
def sub_route():
    " this will route to subroute of hbnb"
    return "HBNB"


@app.route("/c/<variable_name>", strict_slashes=False)
def c_is(variable_name):
    name = variable_name.split("_")
    new_name = ' '.join(name)
    return ("C {}".format(escape(new_name)))


@app.route("/python/", defaults={"variable_name": "is cool"})
@app.route("/python/<variable_name>", strict_slashes=False)
# use is_Cool as default variable else use the user_input
def python_is(variable_name):
    name = variable_name.split("_")
    new_name = ' '.join(name)
    return ("Python {}".format(escape(new_name)))


@app.route("/number/<int:n>", strict_slashes=False)
def number_page(n):
    return ("{} is a number".format(n))


if __name__ == "__main__":
    # web application must be listening on 0.0.0.0, port 5000
    app.run(debug=True, host="0.0.0.0")
