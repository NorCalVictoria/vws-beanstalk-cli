from flask import Flask

application = Flask(__name__)     # cherrypy.tree.mount(Root()) 
app = application

@app.route('/index.html')
@app.route('/')
def test():
	return'<h1> Got again Here . Final Test vws </h1>'

if __name__ == '__main__':
	app.run(debug=True)