from flask import Flask, render_template, request
import json


app = Flask(__name__)


@app.route('/home')
def mainScreen():
    if request.method == "POST":
        if request.div[""]:
            pass
    return render_template('mainWithVideo.html')

@app.route('/about')
def mainScreen():
    return render_template('mainWithVideo.html')

@app.route('/settings')
def mainScreen():
    return render_template('mainWithVideo.html')\

# FLKASLKASLKALSKKL FLASH USE FLASH