from flask import Flask
from flask import render_template
from flask import request
import json
import requests
import secrets


app = Flask(__name__)

# セッション情報を暗号化するためのキー設定
app.secret_key = secrets.token_urlsafe(32)


@app.route("/")
def hello():
    return render_template("index.html")


##
@app.route("/post", methods=["GET", "POST"])
def post_image():
    if request.form["animal"] == "cat":
        r = requests.get("https://api.thecatapi.com/v1/images/search")
        outimage = json.loads(r.text)[0]["url"]

    elif request.form["animal"] == "dog":
        r = requests.get("https://dog.ceo/api/breeds/image/random")
        outimage = json.loads(r.text)["message"]

    elif request.form["animal"] == "fox":
        r = requests.get("https://randomfox.ca/floof/")
        outimage = json.loads(r.text)["image"]

    return render_template("post.html", outimage=outimage)


##
if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8000, debug=True)
