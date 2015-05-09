from flask import Flask, request, render_template, redirect, url_for, send_from_directory
from werkzeug import secure_filename
import os

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'images'
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])


def make_json_list(arg_list):
    template = '[{}],'
    list_without_quotes = ''.join(
        template.format(i) for i in arg_list
    )
    return "'" + list_without_quotes + "'"


@app.route('/popular', methods=['GET', 'POST'])
def popular():
    if request.method == 'POST':

        time_frame = request.form['time']
        start      = request.form['start']
        end        = request.form['end']

        # Jsonify db output
        return "TEST 1 2 3"

    return render_template('top.html')


@app.route('/new', methods=['GET', 'POST'])
def new():
    if request.method == 'POST':

        time_frame = request.form['time']
        start      = request.form['start']

        return "TEST 4 5 6"

    return "NEW DOT HTML"


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['file']
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for('uploaded_file',
                                    filename=filename))
    return '''
    <!doctype html>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <form action="" method=post enctype=multipart/form-data>
      <p><input type=file name=file>
         <input type=submit value=Upload>
    </form>
    '''


@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'],
                               filename)


if __name__ == '__main__':
    app.run(debug=True)
