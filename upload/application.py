from flask import Flask, request, flash, redirect, url_for, render_template
from werkzeug.utils import secure_filename
# import PyPDF2
import os

UPLOAD_FOLDER = './upload_dest/'
ALLOWED_EXTENSIONS = {'pdf'}

application = Flask(__name__)
application.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@application.route('/', methods=['GET', 'POST'])
def upload_file():
    msg = ''
    if request.method == 'POST':
        # check if the POST request has the file part
        if 'file' not in request.files:
            msg = 'No file part'
            return render_template('upload.html', msg=msg)
        file = request.files['file']
        # if user does not select file, browser also
        # submit an empty part without filename
        if file.filename == '':
            msg = 'No file selected'
            return render_template('upload.html', msg=msg)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(
                application.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for('upload_file', filename=filename))
    return render_template('upload.html')


if __name__ == "__main__":
    application.run(debug=True)
