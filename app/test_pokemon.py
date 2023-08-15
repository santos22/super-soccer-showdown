import responses


from pokemon import pokemon_client, POKEMON_GRAPHQL_ENDPOINT


@responses.activate
def test_get_heaviest():
    FATTEST_MOCKED_RESPONSE = {
        "data": {
            "pokemon": [
            {
                "name": "cosmoem",
                "height": 1,
                "weight": 9999
            },
            {
                "name": "celesteela",
                "height": 92,
                "weight": 9999
            }
            ]
        }
    }
    responses.add(
        responses.POST,
        POKEMON_GRAPHQL_ENDPOINT,
        json=FATTEST_MOCKED_RESPONSE,
    )
    response = pokemon_client.get_heaviest()

    assert len(response) == 2
    assert 'data' not in response

    # response is sorted
    assert 'cosmoem' == response[0]['name']
    assert 'celesteela' == response[1]['name']


@responses.activate
def test_get_shortest():
    SHORTEST_MOCKED_RESPONSE = {
        "data": {
            "pokemon": [
            {
                "name": "joltik",
                "height": 1,
                "weight": 6
            },
            {
                "name": "flabebe",
                "height": 1,
                "weight": 1
            }
            ]
        }
    }
    responses.add(
        responses.POST,
        POKEMON_GRAPHQL_ENDPOINT,
        json=SHORTEST_MOCKED_RESPONSE,
    )
    response = pokemon_client.get_shortest()

    assert len(response) == 2
    assert 'data' not in response

    assert 'joltik' == response[0]['name']
    assert 'flabebe' == response[1]['name']


@responses.activate
def test_get_tallest():
    TALLEST_MOCKED_RESPONSE = {
        "data": {
            "pokemon": [
            {
                "name": "eternatus",
                "height": 200,
                "weight": 9500
            }
            ]
        }
    }
    responses.add(
        responses.POST,
        POKEMON_GRAPHQL_ENDPOINT,
        json=TALLEST_MOCKED_RESPONSE,
    )
    response = pokemon_client.get_tallest()

    assert len(response) == 1
    assert 'data' not in response

    assert 'eternatus' == response[0]['name']
