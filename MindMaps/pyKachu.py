import requests
import json

# -------------------------
# Jinja2
# -------------------------
from jinja2 import Environment, FileSystemLoader
template_dir = 'Templates/'
env = Environment(loader=FileSystemLoader(template_dir))
pyKachu_All_template = env.get_template('pyKachu_All.j2')
pyKachu_One_template = env.get_template('pyKachu_One.j2')

# -------------------------
# Headers
# -------------------------
headers = {
  'Accept': 'application/json',
  'Content-Type': 'application/json',
}

with open("../MindMaps/Pokemon/Gotta_Catch_Em_All.md", "w") as fh:
  fh.write("# Gotta Catch Em All\n")
  fh.close()

# -------------------------
# All Pokemon
# -------------------------
allPokemon = requests.request("GET", "https://pokeapi.co/api/v2/pokemon?limit=1200", headers=headers)
allPokemonJSON = allPokemon.json()

for detail in allPokemonJSON['results']:
    singlePokemon = requests.request("GET", detail['url'], headers=headers)
    singlePokemonJSON = singlePokemon.json()
    print(singlePokemonJSON)

    parsed_all_output = pyKachu_All_template.render(
      singlePokemon = singlePokemonJSON
      )

    with open("../MindMaps/Pokemon/Gotta_Catch_Em_All.md", "a") as fh:
      fh.write(parsed_all_output)               
      fh.close()

    with open(f"../MindMaps/Pokemon/{ singlePokemonJSON['name'] }.md", "w") as fh:
      fh.write(parsed_all_output)               
      fh.close()