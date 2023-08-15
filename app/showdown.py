from dataclasses import dataclass
from enum import Enum
from typing import List

import json

class Position(Enum):
    GOALIE = 'Goalie'
    DEFENCE = 'Defence'
    OFFENCE = 'Offence'


"""
Pokemon attrs
- height is decimetres
- weight is hectograms

Star Wars attrs in response is correct
"""
@dataclass
class Player:
    name: str
    height: str  # cm
    weight: str  # kg
    position: str


@dataclass
class Team:
    players: List[Player]


def process_response(response: dict, position: str, players: List):
    for value in response:
        # Player(
        #     value["name"],
        #     value["height"],
        #     value["weight"],
        #     position,
        # )
        # players.append(Player)
        value['position'] = position
        players.append(value)


def generate_team(client):
    response = {
        'universe': client.UNIVERSE,
    }
    players = []

    tallest = client.get_tallest()
    heaviest = client.get_heaviest()
    shortest = client.get_shortest()
    
    process_response(tallest['data']['pokemon'], Position.GOALIE.value, players)
    process_response(heaviest['data']['pokemon'], Position.DEFENCE.value, players)
    process_response(shortest['data']['pokemon'], Position.OFFENCE.value, players)

    response['team'] = players  #  Team(players)
    return json.dumps(response)
