from flask import Flask, request, render_template, redirect, url_for, send_from_directory
import os
from dbreader import fetch_data
import pymysql
import time
import datetime

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'images'
ALLOWED_EXTENSIONS = ('png', 'jpg', 'jpeg', 'gif')


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
        start = request.form['start']
        end = request.form['end']

        # Jsonify db output
        return make_json_list(fetch_data('upvotes'), 0, 100)

    return render_template('top.html')


@app.route('/new', methods=['GET', 'POST'])
def new():
    if request.method == 'POST':

        time_frame = request.form['time']
        start = request.form['start']

        return make_json_list(fetch_data('timestamp', '2000-03-26 00:00:01', '2003-03-26 00:00:01'))

    return "NEW DOT HTML"

# (rows + 1) + ".jpg"

def file_extension(filename):
    return filename.rsplit('.', 1)[1]


def allowed_file(filename):
    return '.' in filename and \
        file_extension(filename) in ALLOWED_EXTENSIONS


@app.route('/upload', methods=['GET', 'POST'])
def upload_file():

    invalid_format = None

    if request.method == 'POST':

        file = request.files['file']
        filename = file.filename
        new_filename = None

        con = pymysql.connect(host='localhost', user='root', passwd='iloveyeeting', db='ratemybitches')

        with con:
                cur = con.cursor()
                cur.execute("USE ratemybitches")
                cur.execute("SELECT COUNT(*) FROM img")
                rows = cur.fetchone()
                cur.execute("INSERT INTO img (id, extension, time, upvotes) VALUES (" + str(rows[0]+1) + ", \'." + file_extension(filename=filename) + "\', \'" + str(datetime.datetime.fromtimestamp(int(time.time()))) + "\', 0)")
                # So that if no file is given the server doesnt throw an error
                try:
                    new_filename = \
                        str(rows[0] + 1) + '.' + file_extension(filename=filename)
                except IndexError:
                    return render_template(
                        'upload.html',
                        error="Please upload a file"
                    )


        invalid_format = \
            True if not allowed_file(filename=filename) else False

        if file and not invalid_format:

            file.save(
                os.path.join(
                    app.config['UPLOAD_FOLDER'], new_filename
                )
            )

            return redirect(
                url_for('uploaded_file', filename=new_filename)
            )

    return render_template(
        'upload.html',
        error="Invalid file format" if invalid_format else None
    )


@app.route('/uploads/<filename>')
def uploaded_file(filename):

    return send_from_directory(
        app.config['UPLOAD_FOLDER'], filename
    )


if __name__ == '__main__':
    app.run(debug=True)
