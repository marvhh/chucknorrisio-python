#!/usr/bin/env python

import requests
import logging

API_BASE_URL = "https://api.chucknorris.io"
__version__ = "1.0.0"


class ChuckNorrisIOClient:
    """Client class for accessing the chucknoris.io API"""

    def __init__(self):
        self.base_url = API_BASE_URL
        self.version = __version__
        self.session = requests.Session()
        self.session.headers.update(
            {"User-Agent": f"chucknorris-io/client-python-{self.version}"}
        )

    def create_request(self, url, payload=None):
        """create requests and return json object"""
        try:
            response = self.session.get(url, params=payload)
            response.raise_for_status()
            return response.json()

        except requests.RequestException as e:
            logging.error(f"Error in request: {e}")
            raise

    def get_joke(self, id):
        """Get a joke by specific id"""
        url = f"{self.base_url}/jokes/{id}"

        joke_data = self.create_request(url)
        return joke_data.get("value")

    def get_random_joke(self, name=None, category=None):
        """Get random joke"""
        url = f"{self.base_url}/jokes/random"

        payload = {}

        if name is not None:
            payload["name"] = name

        if category is not None:
            if isinstance(category, str):
                payload["category"] = category

            if isinstance(category, list):
                payload["category"] = ",".join(category)

        joke_data = self.create_request(url, payload)
        return joke_data.get("value")

    def get_categories(self):
        """Get available joke categorys"""
        url = f"{self.base_url}/jokes/categories"

        category_data = self.create_request(url)
        return category_data

    def search(self, searchtext):
        """Do a free text search in the database"""
        url = f"{self.base_url}/jokes/search"

        payload = {"query": searchtext}

        search_data = self.create_request(url, payload)
        return search_data
