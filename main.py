from flask import (
	Flask,render_template,url_for,
	session	
)

app = Flas(__name__)

@app.route("/")
def index():
	return "index.html"

if __name__ == '__main__':
	app.run(debug=True)