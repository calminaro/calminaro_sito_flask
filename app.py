from flask import Flask, render_template, send_file
import json

with open("credenziali.json", "r") as f:
    cr = json.load(f)

app = Flask(__name__)
app.config['SECRET_KEY'] = cr["secret_key"]

@app.route("/")
def homepage():
    return render_template("index.html")

@app.route("/live_python")
def live_python():
    return render_template("pyscript.html")

@app.route("/whatsapp_sender")
def whatsapp_sender():
    return render_template("whatsapp.html")

@app.route("/password_generator")
def password_generator():
    return render_template("password_generator.html")

@app.route("/aggiorna_debian.sh")
def aggiorna_debian():
    return send_file("/home/calminaro/mysite/static/auto_aggiorna.sh")

@app.route("/hash.py")
def hash():
    return send_file("/home/calminaro/mysite/static/hash.py")

if __name__ == "__main__":
    #Porta specificata per Docker
    app.run(port=8000, host="0.0.0.0")
