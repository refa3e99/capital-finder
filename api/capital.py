from http.server import BaseHTTPRequestHandler
from urllib import parse
import requests


class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        url_components = parse.urlsplit(self.path)
        query_string_list = parse.parse_qsl(url_components.query)
        dictionary = dict(query_string_list)
        url = "https://restcountries.com/v2/"

        country = dictionary.get("country")

        if country:
            response = requests.get(url + "name/" + country)
            data = response.json()
            capital_name = data[0]["capital"]
            message = f"The capital of {country} is {capital_name}"

        else:
            message = "Please write a city name to get info about it"



        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()

        self.wfile.write(message.encode())

        return