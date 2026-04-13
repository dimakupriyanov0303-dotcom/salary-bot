from flask import Flask, send_from_directory

app = Flask(__name__, static_folder="webapp")

@app.route("/")
def home():
    return send_from_directory("webapp", "index.html")

app.run(host="0.0.0.0", port=5000)