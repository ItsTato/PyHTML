
# Example:
# Web server made with Flask that uses
# PyHTML to return HTML pages coded in
# the python file directly to not use
# the Flask templates and save time.

import flask

from PyHTML.pyhtml import Site, HTML, Locations

app = flask.Flask(__name__)

@app.route("/",methods=["GET"])
def index():
    Index = Site()
    Index.add_element(location=Locations.header, element=HTML.title("OwO"))
    Index.add_element(location=Locations.body, element="Hewwo!")
    Index.build()
    return Index.html

app.run(host="0.0.0.0",port="80",debug=True)

