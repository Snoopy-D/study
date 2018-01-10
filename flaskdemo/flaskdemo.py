from flask import Flask, url_for

app = Flask(__name__)


@app.route('/')
def hello_world():
    print url_for('main_page')
    return 'Hello World!'


@app.route('/main')
def main_page():
    return 'This is main page!'


@app.route('/user/<uname>')
def user(uname):
    return '%s\'s profile' % uname


if __name__ == '__main__':
    app.run()
