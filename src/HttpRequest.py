import requests

class HttpRequest:
    
    def getPokemon(self, url):
        response = requests.get(url)
        return response.json()