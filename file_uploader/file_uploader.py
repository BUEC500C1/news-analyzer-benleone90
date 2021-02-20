from flask import Flask, request, flash, redirect, url_for, render_template
from werkzeug.utils import secure_filename
import os

UPLOAD_FOLDER = './upload_dir/'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'doc', 'docx', 'odt'}

template_dir = os.path.abspath('../templates')
app = Flask(__name__, template_folder=template_dir)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # check if the POST request has the file part
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
            return redirect(url_for('upload_file', filename=filename))
    return render_template('upload.html')


if __name__ == "__main__":
    app.run(debug=True)
