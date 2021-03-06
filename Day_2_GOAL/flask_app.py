from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/')
def my_app():
	return render_template('index.html')


@app.route('/hello')
def say_hello():
	name = request.args.get('name')
    return render_template('hello.html', name=name)
