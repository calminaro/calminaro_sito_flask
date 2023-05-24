from flask import Flask, render_template, request, redirect, send_file, url_for

app = Flask(__name__)

@app.route("/")
def homepage():
    return render_template("index.html")

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404
