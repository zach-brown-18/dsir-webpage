from application import app, db
from flask import render_template, url_for, redirect, request


@app.route("/", methods = ["GET"])
def home():
# Will we have a login page to restrict access to enrolled/previously enrolled DSI students?
    return 'Home Page'

@app.route("/call-db", methods = ["GET"])
def call():
# This endpoint is used to call the database and get data
    return 'Call Database'