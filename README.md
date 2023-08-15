# super-soccer-showdown

## Starting the app
After cloning this repository, run the following command from the root directory:
```bash
docker compose up -d
```

Visit the following links:
- http://127.0.0.1:8000/showdown?universe=starwars
- http://127.0.0.1:8000/showdown?universe=pokemon
- http://127.0.0.1:8000/showdown

## Running tests
Make sure the Docker container is running and run the following commands:
```bash
# to run star wars tests
docker exec -it super-soccer-showdown-web-1 python -m pytest test_starwars.py

# to run pokemon tests
docker exec -it super-soccer-showdown-web-1 python -m pytest test_pokemon.py
```
