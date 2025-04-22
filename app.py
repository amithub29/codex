from flask import Flask

app = Flask(__name__)


@app.route("/", methods=["GET"])
def index():
    return "<h1>Coming Soon<h1/>\n", 200


@app.route("/version", methods=["GET"])
def version():
    version = "v0.0.1"
    print(version)
    return version, 200


if __name__ == "__main__":
    app.run(host="localhost", port="5500", debug=True)
