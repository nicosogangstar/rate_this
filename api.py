from flask import Flask, request, render_template

app = Flask(__name__)


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


'''
def get_data(name):
    return request.form[name]

@app.route('/popular', methods=['POST'])
def popular():
    start      = get_data('start')
    end        = get_data('end')
    time_frame = get_data('time')

    return "QUERY RESULTS"


@app.route('/new', methods=['POST'])
def new():
    start      = get_data('start')
    end        = get_data('end')

    return "QUERY RESULT"
'''

if __name__ == '__main__':
    app.run(debug=True)
