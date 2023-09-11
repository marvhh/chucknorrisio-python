# chucknorrisio-python

**chucknorrisio-python** is a simple library for getting chuck norris jokes from the [chucknorris.io JSON API](https://chucknorris.io).

### Example Usage:
```python
>>> from src.chucknorrisio import ChuckNorrisIOClient
>>> client = ChuckNorrisIOClient()
>>> client.get_random_joke()
'He who lives by the sword, dies by the sword. He who lives by Chuck Norris, dies by the roundhouse kick.'

>>> client.get_random_joke(category="dev")
'"It works on my machine" always holds true for Chuck Norris.'

>>> client.get_random_joke(name="marvhh", category=["dev", "food"])
'marvhh can solve the Towers of Hanoi in one move.'

>>> client.get_categories()
['animal', 'career', 'celebrity', 'dev', 'explicit', 'fashion', 'food', 'history', 'money', 'movie', 'music', 'political', 'religion', 'science', 'sport', 'travel']

>>> client.search("asked for a Big Mac")
{'total': 1, 'result': [{'categories': [], 'created_at': '2020-01-05 13:42:30.480041', 'icon_url': 'https://assets.chucknorris.host/img/avatar/chuck-norris.png', 'id': 'NUGhv06RSda5kyVGdQ-39w', 'updated_at': '2020-01-05 13:42:30.480041', 'url': 'https://api.chucknorris.io/jokes/NUGhv06RSda5kyVGdQ-39w', 'value': 'when Chuck Norris went to burger king he asked for a big mac, one minute later they gave him one'}]}
```

## Author

[Marvin Stark](https://github.com/marvhh)