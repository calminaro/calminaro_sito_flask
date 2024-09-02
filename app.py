from flask import Flask, render_template
import secrets

app = Flask(__name__)
app.config['SECRET_KEY'] = secrets.token_hex()

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

if __name__ == "__main__":
    #Porta specificata per Docker
    app.run(port=8000, host="0.0.0.0")
