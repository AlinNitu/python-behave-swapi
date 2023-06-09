"""
Storing the base URL here in case it might change in the future.
This way we can call it from here and if changes occur we need to fix the url only in one place.
"""


class ApiConfig:
    BASE_URL = "https://swapi.dev/api"
    