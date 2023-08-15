import requests

from client import BaseAPIClient


STARWARS_GRAPHQL_ENDPOINT = "https://swapi-graphql.netlify.app/.netlify/functions/index"


class StarWarsAPIClient(BaseAPIClient):
    UNIVERSE = 'Star Wars'

    def get_heaviest(self):
        pass

    def get_shortest(self):
        pass
    def get_tallest(self):
        pass


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

    def get_players_graphql(self):
        data = {
            "query": self.STARWARS_ALL_PEOPLE_QUERY,
        }

        response = requests.post(
            STARWARS_GRAPHQL_ENDPOINT,
            json=data,
            headers={'Content-Type': 'application/json'},
        )
        return response.json()


starwars_client = StarWarsAPIClient()
