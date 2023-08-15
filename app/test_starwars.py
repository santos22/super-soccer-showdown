import responses


from starwars import starwars_client, STARWARS_GRAPHQL_ENDPOINT


MOCKED_RESPONSE = {
  "data": {
    "allPeople": {
      "edges": [
        {
          "node": {
            "id": "cGVvcGxlOjE=",
            "height": 172,
            "mass": 77,
            "name": "Luke Skywalker"
          }
        },
        {
          "node": {
            "id": "cGVvcGxlOjI=",
            "height": 167,
            "mass": 75,
            "name": "C-3PO"
          }
        },
        {
          "node": {
            "id": "cGVvcGxlOjM=",
            "height": 96,
            "mass": 32,
            "name": "R2-D2"
          }
        },
        {
          "node": {
            "id": "cGVvcGxlOjQ=",
            "height": 202,
            "mass": 136,
            "name": "Darth Vader"
          }
        }
      ]
    }
  }
}


@responses.activate
def test_get_heaviest():
    responses.add(
        responses.POST,
        STARWARS_GRAPHQL_ENDPOINT,
        json=MOCKED_RESPONSE,
    )
    client = starwars_client
    response = client.get_heaviest()

    assert len(response) == 2

    # response is sorted
    assert 'Darth Vader' == response[0]['name']
    assert 'Luke Skywalker' == response[1]['name']


@responses.activate
def test_get_shortest():
    responses.add(
        responses.POST,
        STARWARS_GRAPHQL_ENDPOINT,
        json=MOCKED_RESPONSE,
    )
    client = starwars_client
    response = client.get_shortest()

    assert len(response) == 2

    # response is sorted
    assert 'C-3PO' == response[0]['name']
    assert 'R2-D2' == response[1]['name']


@responses.activate
def test_get_tallest():
    responses.add(
        responses.POST,
        STARWARS_GRAPHQL_ENDPOINT,
        json=MOCKED_RESPONSE,
    )
    client = starwars_client
    response = client.get_tallest()

    assert len(response) == 1

    assert 'Darth Vader' == response[0]['name']
