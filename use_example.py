
# Example:
# Web server made with Flask that uses
# PyHTML to return HTML pages coded in
# the python file directly to not use
# the Flask templates and save time.

import flask

from pyhtml import Locations, HTML  # To add stuff that is dynamic like usernames
                                    # or navbars, for example.

from sites.index import Index       # Import the actual site.

app = flask.Flask(__name__)

@app.route("/",methods=["GET"])
def index():
	Index.add_element(Locations.BODY, element="<p>You are ItsTato!</p>")
	return Index.html

app.run(host="0.0.0.0",port="80",debug=True)
