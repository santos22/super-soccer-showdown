# from universe.starwars import starwars_client

import pokebase as pb
import requests

BASE_URL = "https://swapi.dev/api/people/"
POKEMON_BASE_URL = "https://pokeapi.co/api/v2/pokemon/"
POKEMON_GRAPHQL_ENDPOINT = "https://beta.pokeapi.co/graphql/v1beta"

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

    POKEMON_FATTEST_QUERY = """
        query fattest {
            pokemon: pokemon_v2_pokemon(order_by: {weight: desc}, limit: 2, where: {is_default: {_eq: true}}) {
                name
                weight
            }
        }
    """

    POKEMON_SHORTEST_QUERY = """
        query tallest {
            pokemon: pokemon_v2_pokemon(order_by: {height: asc}, limit: 2, where: {is_default: {_eq: true}}) {
                name
                height
            }
        }
    """

    POKEMON_TALLEST_QUERY = """
        query tallest {
            pokemon: pokemon_v2_pokemon(order_by: {height: desc}, limit: 1, where: {is_default: {_eq: true}}) {
                name
                height
            }
        }
    """

    def get_fattest(self):
        data = {
            "operationName" : "fattest",
            "query": self.POKEMON_FATTEST_QUERY,
            "variables": None,
        }

        response = requests.post(
            POKEMON_GRAPHQL_ENDPOINT,
            json=data,
            headers={'Content-Type': 'application/json'},
        )
        return response.json()

    def get_shortest(self):
        data = {
            "operationName" : "tallest",
            "query": self.POKEMON_SHORTEST_QUERY,
            "variables": None,
        }

        response = requests.post(
            POKEMON_GRAPHQL_ENDPOINT,
            json=data,
            headers={'Content-Type': 'application/json'},
        )
        return response.json()

    def get_tallest(self):
        data = {
            "operationName" : "tallest",
            "query": self.POKEMON_TALLEST_QUERY,
            "variables": None,
        }

        response = requests.post(
            POKEMON_GRAPHQL_ENDPOINT,
            json=data,
            headers={'Content-Type': 'application/json'},
        )
        return response.json()

pokemon_client = PokemonClient()
starwars_client = StarWarsClient()

def generate_team(universe: str) -> dict:
    if universe == 'starwars':
        players = starwars_client.get_players()
    elif universe == 'pokemon':
        players = pokemon_client.get_shortest()
    return players
