import pywinctl
from flask import Flask

app = Flask(__name__)


@app.route("/close")
def close_win():
    for w in pywinctl.getAllWindows():
        w.minimize()
    return "closed"


@app.route("/open")
def open_win():
    for w in pywinctl.getAllWindows():
        w.activate()
    return "opened"
