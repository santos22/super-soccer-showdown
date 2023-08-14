from flask import Flask, request

from showdown import generate_team

app = Flask(__name__)

@app.route('/showdown', methods=['GET'])
def showdown():
	universe = request.args.get('universe')
	if universe == 'starwars':
		players = generate_team('starwars')
		return players
	elif universe == 'pokemon':
		players = generate_team('pokemon')
		return players
	else:
		return 'Universe is not supported...'

if __name__ == '__main__':
	app.run(debug = True, host='0.0.0.0', port=8000)
