"""
Replacement for RUSA ACP brevet time calculator
(see https://rusa.org/octime_acp.html)

"""

import flask
from flask import Flask, redirect, url_for, request, render_template
import arrow  # Replacement for datetime, based on moment.js
import acp_times  # Brevet time calculations
import config
import math

import logging
import os
from pymongo import MongoClient


###
# Globals
###
app = flask.Flask(__name__)
_list=[]

###
# Pages
###
client = MongoClient("db", 27017)
db = client.tododb

@app.route("/")
@app.route("/index")
def index():
    _items = db.tododb.find()
    items = [item for item in _items]
    return flask.render_template('calc.html',items=items)


@app.errorhandler(404)
def page_not_found(error):
    flask.session['linkback'] = flask.url_for("index")
    return flask.render_template('404.html'), 404


###############
#
# AJAX request handlers
#   These return JSON, rather than rendering pages.
#
###############

@app.route("/_calc_times")
def _calc_times():
    """
    Calculates open/close times from miles, using rules
    described at https://rusa.org/octime_alg.html.
    Expects one URL-encoded argument, the number of miles.
    """
    km = request.args.get('km', 999, type=float)


    # FIXME: These probably aren't the right open and close times
    # and brevets may be longer than 200km
    distance_ = request.args.get('data_dis', '', type= int)
    date_ = request.args.get('data_date', '', type= str)
    time_ = request.args.get('data_time', '', type= str)
    time_format= date_ + 'T' + time_+':00.000000-08:00'
    time_arrow = arrow.get(time_format)

    open_time = acp_times.open_time(km, distance_, time_arrow)
    close_time = acp_times.close_time(km, distance_, time_arrow)
    #assert(acp_times.open_time(2000,200,time_arrow) == "Wrong")
    #assert(acp_times.open_time(34,200,time_arrow) ==time_arrow.shift(hours=+1).isoformat())
    #assert(acp_times.close_time(15, 600,time_arrow) == time_arrow.shift(hours=+1).isoformat())
    result = {"open": open_time, "close": close_time}
    n_result = {"open": 'open time: '+ open_time, "close": 'close time: '+ close_time}
    _list.append(n_result)
    return flask.jsonify(result=result)


@app.route("/_submit", methods = ['POST'])
def _submit():

    if ( len(_list) == 0):
        return render_template('404.html')
    for i in _list:
        db.tododb.insert_one(i)
    
    while (_list != []):
        _list.pop()
    
    return redirect(url_for('index'))


@app.route("/_display", methods = ['POST'])
def _display():

    _items = db.tododb.find()
    items = [item for item in _items]

    return render_template('display.html', items=items)




#############


if __name__ == "__main__":
    app.run(port=5000, host="0.0.0.0")
