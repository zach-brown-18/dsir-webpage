from application import app, db
from planning import read_data
from flask import render_template, url_for, redirect, request

# Here is a global variable!
mask_list = []



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
    if 'clicked' in request.args.keys():
        if request.args['clicked'] != '':
            if request.args['clicked'] in mask_list:
                mask_list.remove(request.args['clicked'])
            else:
                mask_list.append(request.args['clicked'])

    my_tags = ''
    for t in read_data.df['MAIN PAGE BRANCHES'].unique():
        if t in mask_list:
            path = f"parent.location='/template_practice?clicked={t}'"
            my_tags += f'<input class="tagMask" type=button onClick="{path}" value="{t}">\n'
        else:
            path = f"parent.location='/template_practice?clicked={t}'"
            my_tags += f'<input class="tagShow" type=button onClick="{path}" value="{t}">\n'
        
    my_resources = ''
    for _, row in read_data.df.iterrows():
        if row['MAIN PAGE BRANCHES'] not in mask_list:
            page_desc = row["PAGE DESCRIPTION"]
            my_resources += f'<div class="resDiv">{page_desc}</div>\n'
    
    return render_template("resource_template.html", tags=my_tags, resources=my_resources)

    