from flask import Flask

app = Flas(__name__)
app.secret_key = "dasfadsfaf"

if __name__ == '__main__':
	app.run()