from flask import Flask

app = Flask(__name__)

@app.route('/index.html')
@app.route('/')
def test():
	return'<h1> Got again Here </h1>'

if __name__ == '__main__':
	app.run(host='0.0.0.0', debug=True)