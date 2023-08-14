# from universe.starwars import starwars_client

import pokebase as pb
import requests

BASE_URL = "https://swapi.dev/api/people/"
POKEMON_BASE_URL = "https://pokeapi.co/api/v2/pokemon/"

# TODO figure out module later...
class StarWarsClient:

    def get_players(self):
        players = []
        response = requests.get(BASE_URL)
        response.raise_for_status()
        json_response = response.json()
        players.extend(json_response.get('results'))

        while json_response.get("next") is not None:
            next_url = json_response['next']
            response = requests.get(next_url)
            response.raise_for_status()
            json_response = response.json()
            players.extend(json_response.get('results'))

        return players

class PokemonClient:

    def get_players(self):
        players = []
        response = requests.get(POKEMON_BASE_URL)
        response.raise_for_status()
        json_response = response.json()
        players.extend(json_response.get('results'))

        while json_response.get("next") is not None:
            next_url = json_response['next']
            response = requests.get(next_url)
            response.raise_for_status()
            json_response = response.json()
            players.extend(json_response.get('results'))

        return players

pokemon_client = PokemonClient()
starwars_client = StarWarsClient()

def generate_team(universe: str) -> dict:
    if universe == 'starwars':
        players = starwars_client.get_players()
    elif universe == 'pokemon':
        players = pokemon_client.get_players()
    return players
