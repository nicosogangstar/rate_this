from flask import Flask, request

app = Flask(__name__)


def make_json_list(arg_list):
    template = '[{}],'
    list_without_quotes = ''.join(
        template.format(i) for i in arg_list
    )
    return "'" + list_without_quotes + "'"


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


if __name__ == '__main__':
    app.run(debug=True)
