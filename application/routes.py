from application import app, db
from planning import read_data
from flask import render_template, url_for, redirect, request


@app.route("/", methods = ["GET"])
def home():
# Will we have a login page to restrict access to enrolled/previously enrolled DSI students?
    return 'Home Page'

@app.route("/call-db", methods = ["GET"])
def call():
# This endpoint is used to call the database and get data
    return 'Call Database'

@app.route("/template_practice")
def practice():

    my_tags = ''
    for t in read_data.df['MAIN PAGE BRANCHES'].unique():
        my_tags += f'<div class="tagDiv">{t}</div>\n'
        
    my_resources = ''
    for r in read_data.df['PAGE DESCRIPTION']:
        my_resources += f'<div class="resDiv">{r}</div>\n'
    
    return render_template("resource_template.html", tags=my_tags, resources=my_resources)

    