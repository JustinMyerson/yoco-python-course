from crypt import methods
from flask import Flask
from flask import request
from rot13 import rot13

app = Flask(__name__)


@app.route("/api/encryptions/rot13", methods=["GET"])
def mumble():
    args = request.args
    plaintext = args.get("plaintext")
    return {"cyphertext": rot13(plaintext), }
