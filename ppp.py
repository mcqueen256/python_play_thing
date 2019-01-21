import os
from flask import Flask, flash, request, redirect, url_for
from werkzeug.utils import secure_filename
app = Flask(__name__)

# File upload from this tutorial:
#    http://flask.pocoo.org/docs/1.0/patterns/fileuploads/
UPLOAD_FOLDER = './uploaded_files/'
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/upload', methods=['GET', 'POST'])
def uploaded_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        # submit an empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for('uploaded_file',
                                    filename=filename))
    return '''
    <!doctype html>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <form method=post enctype=multipart/form-data>
      <input type=file name=file>
      <input type=submit value=Upload>
    </form>
    '''


# Rest of the server

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