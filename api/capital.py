from http.server import BaseHTTPRequestHandler
from urllib import parse
import requests


class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        url_components = parse.urlsplit(self.path)
        query_string_list = parse.parse_qsl(url_components.query)
        dictionary = dict(query_string_list)
        url = "https://restcountries.com/v2/"

        capital = dictionary.get("capital")
        country = dictionary.get("country")

        if country:
            response = requests.get(url + "name/" + country)
            data = response.json()
            capital_name = data[0]["capital"]
            message = f"The capital of {country} is {capital_name}"

        elif capital:
            response = requests.get(url + "capital/" + capital)
            data = response.json()
            capitals = data[0]["capital"]
            country_name = data[0]["name"]
            message = f"{capitals} is the capital of {country_name}"

        else:
            message = "Please provide a name of a country/capital"

        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()

        self.wfile.write(message.encode())

        return
