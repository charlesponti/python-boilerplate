import json
import os

from flask import Flask
from app.config import Config

app = Flask(__name__)

app.config.from_object(Config())

print("cats")

@app.route("/", methods=["GET"])
def index(*args, **kwargs):
    print(args)
    print(kwargs)
    return json.dumps([])


@app.route("/", methods=["POST"])
def objects(*args, **kwargs):
    print(args)
    print(kwargs)
    return json.dumps({"name": "foobar"})


if __name__ == "__main__":
    app.run("localhost", 8000)
