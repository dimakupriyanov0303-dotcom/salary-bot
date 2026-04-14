from flask import Flask, send_from_directory
import os

app = Flask(__name__, static_folder="webapp")

@app.route("/")
def home():
    return send_from_directory("webapp", "index.html")

@app.route("/<path:path>")
def static_files(path):
    return send_from_directory("webapp", path)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
