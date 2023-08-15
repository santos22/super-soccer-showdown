import requests


from client import BaseAPIClient

POKEMON_GRAPHQL_ENDPOINT = "https://beta.pokeapi.co/graphql/v1beta"


class PokemonAPIClient(BaseAPIClient):
    UNIVERSE = 'Pokemon'

    POKEMON_HEAVIEST_QUERY = """
        query fattest {
            pokemon: pokemon_v2_pokemon(order_by: {weight: desc}, limit: 2, where: {is_default: {_eq: true}}) {
                name
                height
                weight
            }
        }
    """

    POKEMON_SHORTEST_QUERY = """
        query tallest {
            pokemon: pokemon_v2_pokemon(order_by: {height: asc}, limit: 2, where: {is_default: {_eq: true}}) {
                name
                height
                weight
            }
        }
    """

    POKEMON_TALLEST_QUERY = """
        query tallest {
            pokemon: pokemon_v2_pokemon(order_by: {height: desc}, limit: 1, where: {is_default: {_eq: true}}) {
                name
                height
                weight
            }
        }
    """

    def get_heaviest(self) -> list:
        data = {
            "operationName" : "fattest",
            "query": self.POKEMON_HEAVIEST_QUERY,
            "variables": None,
        }

        response = requests.post(
            POKEMON_GRAPHQL_ENDPOINT,
            json=data,
            headers={'Content-Type': 'application/json'},
        )
        return response.json()['data']['pokemon']

    def get_shortest(self) -> list:
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
        return response.json()['data']['pokemon']

    def get_tallest(self) -> list:
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
        return response.json()['data']['pokemon']


pokemon_client = PokemonAPIClient()
