# Code by Steven Au
# Website: Programming Languages Compare
# Reference to https://flask.palletsprojects.com/en/2.0.x/
import os
import json
import random
import requests

# Flask
import flask
from flask_cors import cross_origin

from private import private
from methods import db, route_functions as rf

# Flask initialization
app = flask.Flask(__name__, template_folder='templates')

# Required configurations
app.config['SECRET_KEY'] = "ThisIsTheSecretKey361"
app.config['CORS_HEADERS'] = 'Content-Type'


@app.route("/selection", methods=['GET', 'POST']) # Covering bases
@app.route("/", methods=['GET', 'POST'])
def main():
    """ Main page"""
    items = ['C', 'C++', 'C#', 'Dart', 'Java', 'Javascript', 'Kotlin', 'Python', 'Swift']
    concepts = ['Variables', 'For Loops', 'While Loops', 'Functions']

    # Post request to hide the items from the URL.
    if flask.request.method == 'POST':
        # Route fires when user makes a submission
        # Create a flask session of the user entries
        form_data = flask.request.form
        raw_data = json.dumps(form_data)

        # Have the user query to be the main search result
        dict_json = json.loads(raw_data)

        # Go to a different route if the user clicked on the reset button instead.
        if dict_json["formButton"] == "Reset":
            flask.session.clear()
            data = {}  # Send an empty data dictionary (Prevent errors)
            flask.flash("Previous session was cleared.")
            return flask.render_template("index.html", items=items, concepts=concepts, data=data)

        # Process the dictionary before it would be saved as a session file
        if dict_json["topic"] == "other":
            if dict_json["other"] == "":
                dict_json["other"] = "null"
            dict_json["topic"] = dict_json["other"]
        else:
            dict_json["other"] = ""

        dict_json["initialized"] = "true"

        # Then convert back
        str_data = json.dumps(dict_json)

        # Process and make a request to the YouTube API - my manipulation functions are abstracted.
        youtube_data = json.dumps(rf.RouteData().process_vid_ids(json.loads(str_data)))

        flask.session['data'] = str_data
        flask.session['youtube'] = youtube_data

        time = requests.get("https://time-microservice-04.herokuapp.com/api/time").json()
        flask.session["time"] = time[1]["unixNumberGMT"]
        return flask.redirect(flask.url_for('details'))

    try:
        data = json.loads(flask.session['data'])
        data3 = str(flask.session["time"])
        return flask.render_template('index.html', items=items, concepts=concepts, data=data, data3=data3)
    except:
        data = {}  # Send an empty data dictionary (Prevent errors)
        return flask.render_template("index.html", items=items, concepts=concepts, data=data)


@app.route("/details", methods=['GET', 'POST'])
def details():
    """ Main details route"""
    try:
        data = json.loads(flask.session['data'])
        data2 = json.loads(flask.session['youtube'])
        data3 = {
            "wikipedia1": rf.RouteData().try_passer(rf.RouteData().get_wikipedia(data["language"]), rf.RouteData().wiki_err),
            "wikipedia2": rf.RouteData().try_passer(rf.RouteData().get_wikipedia(data["language2"]), rf.RouteData().wiki_err)
        }  # Request group mate's wiki service
        data4 = {
            "Syntax1": db.DB().process_group(data["language"], data["topic"]),
            "Syntax2": db.DB().process_group(data["language2"], data["topic"])
        }  # database data

        return flask.render_template('details.html', data=data, data2=data2, data3=data3, data4=data4)
    except:
        flask.flash(rf.RouteData.selection_danger)
        return flask.redirect(flask.url_for('main'))


@app.route("/videos", methods=['GET', 'POST'])
def videos():
    """ Video route"""
    try:
        data = json.loads(flask.session['data'])
        data2 = json.loads(flask.session['youtube'])
        return flask.render_template('videos.html', data=data, data2=data2)
    except:
        flask.flash(rf.RouteData.selection_danger)
        return flask.redirect(flask.url_for('main'))


@app.route("/syntax", methods=['GET', 'POST'])
def syntax():
    """ Syntax route"""
    try:
        data = json.loads(flask.session['data'])
        data2 = {
            "Syntax1": rf.RouteData().try_passer(db.DB().process_group(data["language"], data["topic"]), rf.RouteData().syntax_err),
            "Syntax2": rf.RouteData().try_passer(db.DB().process_group(data["language2"], data["topic"]), rf.RouteData().syntax_err)
        }

        return flask.render_template('syntax.html', data=data, data2=data2)
    except:
        flask.flash(rf.RouteData.selection_danger)
        return flask.redirect(flask.url_for('main'))


@app.route("/api")
@cross_origin()
def api():
    """ Use the unsplash API for free and developer friendly images."""
    search_query = "calm"
    image_scrape = "https://api.unsplash.com/photos?query=" + search_query + private.PrivateKeys().image()

    json_api = requests.get(image_scrape).json()

    # Random selection of images
    res_random = json_api[random.randint(0, len(json_api) - 1)]
    random_image = res_random["urls"]
    res = flask.make_response(random_image, 200)  # Status 200 for the explicit OK response
    res.mimetype = "application/json"  # Set the mimetype property per the documentation

    # Export the random image url as a json object
    return res


@app.route("/api/video")
@cross_origin()
def api_youtube():
    """ Secondary route to the api videos"""
    try:
        # Similar to the above but with youtube
        data = json.loads(flask.session['data'])
        res_dict = rf.RouteData().process_vid_ids(data)
        res = flask.make_response(res_dict, 200)  # Status 200 for the explicit OK response
        res.mimetype = "application/json"  # Set the mimetype property per the documentation
        return res
    except:
        # If there isn't a session up, redirect away.
        flask.flash('You do not have access to this page. ')
        return flask.redirect(flask.url_for('main'))


@app.route("/db")
def database():
    """ Get all raw database details."""
    data = db.DB().db_get()
    return data


@app.errorhandler(404)
def page_not_found(e):
    """ Render the 404 error page"""
    return flask.render_template("404.html")


@app.errorhandler(500)
def internal_server_error(e):
    """ Render a 500 error page"""
    return flask.render_template('500.html')


if "__main__" == __name__:
    # Initialize DB
    db.DB().db_init()

    # App launcher
    port = os.environ.get("PORT", 5000)
    app.run(debug=False, host='0.0.0.0', port=port)
