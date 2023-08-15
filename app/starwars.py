import copy
import operator

import requests

from client import BaseAPIClient


STARWARS_GRAPHQL_ENDPOINT = "https://swapi-graphql.netlify.app/.netlify/functions/index"


class StarWarsAPIClient(BaseAPIClient):
    UNIVERSE = 'Star Wars'

    def get_heaviest(self) -> list:
        players = self._get_players_graphql()
        sorted_list = sorted(players, key=operator.itemgetter("mass"), reverse=True)
        return sorted_list[:2]  # two heaviest

    def get_shortest(self) -> list:
        players = self._get_players_graphql()
        sorted_list = sorted(players, key=operator.itemgetter("height"), reverse=True)
        return sorted_list[-2:]  # two shortest

    def get_tallest(self) -> list:
        players = self._get_players_graphql()
        sorted_list = sorted(players, key=operator.itemgetter("height"), reverse=True)
        return sorted_list[:1]  # one tallest


    STARWARS_ALL_PEOPLE_QUERY = """
    {
        allPeople {
            edges {
                node {
                    id
                    height
                    mass
                    name
                }
            }
        }
    }
    """

    def _get_players_graphql(self) -> list:
        # TODO cache this...
        data = {
            "query": self.STARWARS_ALL_PEOPLE_QUERY,
        }

        response = requests.post(
            STARWARS_GRAPHQL_ENDPOINT,
            json=data,
            headers={'Content-Type': 'application/json'},
        )
        edges = response.json()['data']['allPeople']['edges']
        nodes = [player['node'] for player in edges]

        # need to handle null/None values returned in response
        players = []
        for node in nodes:
            player = copy.copy(node)
            if node.get("mass") is None:
                player["mass"] = 0
            if node.get("height") is None:
                player["height"] = 0
            players.append(player)
        return players


starwars_client = StarWarsAPIClient()
