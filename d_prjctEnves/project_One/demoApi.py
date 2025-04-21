import requests

base_url = "https://pokeapi.co/api/v2/"

def get_pokemon_info(name):
    url=f"{base_url}/pokemon/{name}"
    response = requests.get(url)

    if response.status_code ==200:
        poke_data = response.json()
        return poke_data
    else:
        print(f"failed to retrieved data {response.status_code}")


# pokemon_name = "pikachu"
pokemon_name = "typhlosion"

poke_dict = get_pokemon_info(pokemon_name)    

if poke_dict:
    print(f"Name : {poke_dict['name']}")
    print(f"Id : {poke_dict['id']}")
    print(f"Height : {poke_dict['height']}")
    print(f"Weight : {poke_dict['weight']}")
    print(f"Image : {poke_dict['sprites']['front_default']}")
    