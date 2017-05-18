from flask import Flask

app = Flas(__name__)

@app.route("/")
def index():
	return "index.html"

if __name__ == '__main__':
	app.run()