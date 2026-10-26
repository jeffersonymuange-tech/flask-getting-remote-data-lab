import requests
import json


class GetRequester:
    """Fetches data from a remote URL via HTTP GET and parses JSON."""

    def __init__(self, url):
        # Store the endpoint URL to query
        self.url = url

    def get_response_body(self):
        """Send a GET request to the URL and return the raw response body (bytes)."""
        response = requests.get(self.url)
        return response.content

    def load_json(self):
        """Fetch the response body and convert it into Python data (list of dicts)."""
        return json.loads(self.get_response_body())