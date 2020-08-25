from flask import Flask, request
from helpers import build_page
import random

app = Flask(__name__)

@app.route("/", methods = ["GET", "POST"])
def gra():
	buff = """
	<form method = 'POST'>
		<input name = "value_g" type = "hidden" value = "{}"/>
		<input name = "vaule_p" type = "text" placeholder = "Guess number"/>
		<input type = "submit" value = "play">

	"""
	content_base = "{} <hr/> {}"
	result = ""

	if request.method == 'POST':
		try:
			value_game = int(request.form["value_g"])
			vaule_player = int(request.form["vaule_p"])
			if value_game < vaule_player:
				result = "Too big!"
			if value_game > vaule_player:
				result = "Too small!"
			if value_game == vaule_player:
				result = "You win!"
		except ValueError:
			result = "It's not a number!"
	else:
		value_game = random.randint(1, 100)
		result = 'Guess the number:'

	
	form = buff.format(value_game)
	content = content_base.format(result, form)


	return build_page("Game: Guess the number form 0 to 100:", content)


if __name__ == "__main__":
    app.run()