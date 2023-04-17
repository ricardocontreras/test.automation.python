import sys
sys.path.append("..")
from HttpRequest import HttpRequest

class Test_01:
    httpRequest = HttpRequest()    
    list_pokemon = [{"id": 1, "name": "Bulbasaur"}, {"id": 4, "name": "Charmander"}]
    
    def test01(self):
        response = self.httpRequest.getPokemon("https://pokeapi.co/api/v2/pokemon/1/")
        for pokemon in self.list_pokemon:
            response = self.httpRequest.getPokemon(f"https://pokeapi.co/api/v2/pokemon/{pokemon['id']}")
            assert response["name"].lower() == pokemon["name"].lower(), f"The pokemon returned is not the expected one. Expected: {pokemon['name']}, Actual: {response['name']}."
        
Test_01().test01()