from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
@app.route('/hello/<name>')
def hello(name=None):
    if name:
        return render_template('hello.html', nme=name)
    return "Hello, man!"