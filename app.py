import os
from flask import Flask

app = Flask(__name__)
app.config.from_object(os.environ.get("APP_SETTINGS", default="config.DevelopmentConfig"))

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/<name>')
def hello_name(name):
    return "Hello {}!".format(name)


if __name__ == '__main__':
    app.run()
