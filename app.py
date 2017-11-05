from flask import Flask, session, redirect, render_template, request, url_for
from flask_session import Session
import os

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
	login = ""
	if request.method == 'POST':
		login = request.form.get('username')
		login = str(login)
		print(str(login))

	return render_template('index.html', nombre = login)

@app.route('/contacto')
def contact():
    return render_template('contacto.html')

@app.errorhandler(404)
def page_not_found(error):
    return render_template('http_404.html')


if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug = True, use_reloader = True)
