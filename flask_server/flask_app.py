from flask import Flask

flask_app = Flask(__name__)

@flask_app.route('/')
def home():
    return 'Hello world'

@flask_app.route('/firstFilter')
def firstFilter():
    return 'Hello world 2'

@flask_app.route('/secondFilter')
def secondFilter():
    return 'Hello world 3'

if __name__ == '__main__':
    flask_app.run(debug=False)