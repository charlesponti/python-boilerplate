import json

from app import app


@app.route("/")
def index():
    return "Hello from Flask in a container!"

@app.route("/cats")
def cats():
    return json.dumps({"message": "foobar"})
