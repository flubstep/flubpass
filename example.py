from passage import *


@fragment()
def get_user_page():
	page.output("USER LOOKUP TOOL")
	page.output("================")
	page.ask_for_input('Lookup by User ID', then='find_by_user_id')
	page.ask_for_input('Lookup by User Email', then='find_by_user_email')
	page.ask_for_input('What is your name?', then='echo_your_name')


@fragment()
def find_by_user_id(user_id):
	user_info = {
		'first_name': 'Steve',
		'last_name': 'The Cat',
		'email': 'steve@passage.com'
	}
	page.output("okay whatever")
	page.output(user_info)
	# page.button('Delete?').then(delete_by_user_id, args={'user_id': user_id})


@fragment()
def find_by_user_email(email):
	user_info = {
		'first_name': 'Steve',
		'last_name': 'McQueen',
		'email': email
	}
	page.output(user_info)
	# page.button('Delete?').then(delete_by_user_id, args={'user_id': user_id})


@fragment()
def echo_your_name(name):
	page.output('Hey, your name is ' + name)


@fragment()
def delete_user_id(user_id):
	page.output('BALEETED!')


# TODO: this is pretty crufty
run()