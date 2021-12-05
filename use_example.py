
# Example:
# Web server made with Flask that uses
# PyHTML to return HTML pages coded in
# the python file directly to not use
# the Flask templates and save time.

import flask

import pyhtml as _

app = flask.Flask(__name__)

@app.route("/",methods=["GET"])
def index():
    return _.HTML(code=f"""
{_.Head.open()}
{_.Head.title(title="Some Site")}
{_.Head.close()}

{_.Body.open()}
{_.Body.h1("Welcome!")}
{_.Body.a(content=_.Body.button(content="Open Google =>"),href="https://google.com/")}
{_.Body.a(content=_.Body.button(content="Open Discord =>"),href="https://discord.com/app")}
{_.Body.close()}
    """
    )

app.run(host="0.0.0.0",port="80",debug=True)

