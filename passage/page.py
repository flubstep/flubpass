import json


class PassageOutput():

	def __init__(self, text):
		self.text = text

	def render(self):
		return {
			'lineType': 'output',
			'data': {
				'text': self.text
			}
		}

class PassageInput():

	def __init__(self, text, then):
		self.text = text
		self.then = then

	def render(self):
		return {
			'lineType': 'input',
			'data': {
				'text': self.text,
				'endpoint': self.then
			}
		}

class PassagePage():

	def __init__(self):
		self._messages = []

	def output(self, *messages):
		self._messages += [PassageOutput(message) for message in messages]

	def ask_for_input(self, message, then):
		self._messages.append(PassageInput(message, then))

	def render(self):
		return [message.render() for message in self._messages]
