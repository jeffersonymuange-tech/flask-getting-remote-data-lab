# Retrieving Remote Data from an API

## Overview
`GetRequester` is a reusable class that fetches data from a remote URL with an
HTTP GET request and parses JSON responses. It is designed for a Company
Directory Dashboard, where a Flask app pulls the latest employee records from
a remote JSON endpoint.

## Usage
```python
from lib.GetRequester import GetRequester

requester = GetRequester("https://learn-co-curriculum.github.io/json-site-example/endpoints/people.json")
raw = requester.get_response_body()   # raw response body (bytes)
people = requester.load_json()        # parsed Python list of dicts
```

## Methods
- `__init__(url)`: stores the endpoint URL.
- `get_response_body()`: sends a GET request and returns the response body.
- `load_json()`: converts the response body into Python data structures.

## Setup
```bash
pipenv install
pipenv shell
pytest -v
```

## Screenshot
![Tests passing](screenshot.png)