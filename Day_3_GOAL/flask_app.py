from flask import Flask, render_template, request

from src.eightball import get_answer

app = Flask(__name__)


@app.route('/')
def index():
	prompt = 'Ask the Magic Eightball a Yes/No question'
	return render_template('index.html', prompt=prompt)


@app.route('/eightball')
def eightball():
	answer = get_answer()
	question = request.args.get('question')
	return render_template('eightball.html', question=question, answer=answer)
