from page import PassagePage
from flask import Flask, Response, request, jsonify, render_template
import json
import functools

flask_app = Flask(__name__)


class PassageContextPage():

	def __init__(self):
		self.inner = None

	def set_inner(self, inner):
		self.inner = inner

	def __getattr__(self, attr):
		if self.inner is not None:
			return getattr(self.inner, attr)


page = PassageContextPage()


def app(name):
	# TODO: use name somewhere?
	return PassageApplication()


@flask_app.route('/<string:passage>')
def index(passage):
	return render_template('passage.html', starting=passage)


@flask_app.route('/call', methods=['POST'])
def caller():
	page.set_inner(PassagePage())
	data = request.get_json()
	endpoint = data['endpoint']
	# TODO: why have text at all
	if 'text' in data:
		endpoints[endpoint](data['text'])
	else:
		endpoints[endpoint]()
	page_json = json.dumps(page.render())
	resp = Response(page_json, status=200, mimetype='application/json')
	page.set_inner(None)
	return resp 


endpoints = {}
def fragment():
	def make_inner(endpoint):
		name = endpoint.__name__
		if name in endpoints:
			raise ValueError("TODO: something about duplicate name")
		endpoints[name] = endpoint
		return endpoint
	return make_inner


def run():
	flask_app.run(debug=True)