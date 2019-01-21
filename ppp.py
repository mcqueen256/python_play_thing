from flask import Flask
app = Flask(__name__)

@app.route("/")
def index():
    with open('./elpis-gui/build/index.html', 'r') as fin:
        return fin.read()

@app.route("/static/js/<file>")
def js(file):
    with open('./elpis-gui/build/static/js/'+file, 'r') as fin:
        return fin.read()

@app.route("/static/css/<file>")
def css(file):
    with open('./elpis-gui/build/static/css/'+file, 'r') as fin:
        return fin.read()

@app.route("/<file>")
def root(file):
    with open('./elpis-gui/build/'+file, 'r') as fin:
        return fin.read()


