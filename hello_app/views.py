from datetime import datetime
from flask import Flask, render_template, request
from . import app
from hello_app.sign import *
import os
import base64

from Crypto.PublicKey import RSA

app.config["PRIVATE_CERT"] = RSA.import_key(base64.b64decode(os.environ.get("PRIVATE_CERT"))).export_key('PEM')
app.config["PUBLIC_CERT"] = RSA.import_key(app.config["PRIVATE_CERT"]).publickey().export_key('PEM')

@app.route("/sign")
def _sign():
    msg = str.encode(request.headers.get("msg"))
    return sign(msg, app.config["PRIVATE_CERT"])

@app.route("/verif")
def about():
    msg = str.encode(request.headers.get("msg"))
    sig64 = str.encode(request.headers.get("sig"))
    print(sig64)
    if verify(msg, sig64, app.config["PUBLIC_CERT"]):
        return "True"
    else:
        return "False"

@app.route("/pubcert")
def contact():
    return app.config["PUBLIC_CERT"]

