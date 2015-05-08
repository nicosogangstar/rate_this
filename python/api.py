from flask import Flask, request

app = Flask(__name__)


def make_json_list(arg_list):
    template = '[{}],'
    list_without_quotes = ''.join(
        template.format(i) for i in arg_list
    )
    return "'" + list_without_quotes + "'"


@app.route('/popular', methods=['POST'])
def popular():
    start      = request.form[]
    end        = request.form[]
    time_frame = request.form[]

    return "QUERY RESULTS"

@app.route('/new', methods=['POST'])
def new():
    start = request.form[]
    end   = request.form[]

    return "QUERY RESULT"


if __name__ == '__main__':
    app.run(debug=True)
