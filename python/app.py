from flask import Flask

app = Flask(__name__)


def make_json_list(arg_list):
    template = '[{}],'
    list_without_quotes = ''.join(
        template.format(i) for i in arg_list
    )
    return "'" + list_without_quotes + "'"

# print(make_json_list([1,2,3,4]))


@app.route('/')
def home():
    return "Home Page"


@app.route('/popular/<time_frame>')
def popular(time_frame=None):
    return "Time Frame"


if __name__ == '__main__':
    app.run(debug=True)
