import threading
import PokedexDisplayInfo
import time
import requests
PokeDisplay = PokedexDisplayInfo.PokeDisplay



def get_starters_by_region(region_name):

    fuego = ""
    agua = ""
    planta = ""

    import requests

    def Pokedex(name, url_base):
        url = f"{url_base}pokemon/{name}"  # Use 'name' instead of 'pokenombre'
        respuesta = requests.get(url)

        if respuesta.status_code == 200:
            print("Conexión asegurada! Pokemon encontrado!")
            print()
            pokemon_data = respuesta.json()
            return pokemon_data  # Return the pokemon data
        else:
            print("Errr! Error error! Pokemon desconocido!")
            print(f"Numero del error es: {respuesta.status_code}")
            return {}  # Return an empty dictionary if there was an error


    url_base = "https://pokeapi.co/api/v2/"
    # Dictionary mapping regions to their starter Pokémon
    starters_first = {
        "kanto 1": ["Bulbasaur", "Charmander", "Squirtle"],
        "johto 1": ["Chikorita", "Cyndaquil", "Totodile"],
        "hoenn 1": ["Treecko", "Torchic", "Mudkip"],
        "sinnoh 1": ["Turtwig", "Chimchar", "Piplup"],
        "unova 1": ["Snivy", "Tepig", "Oshawott"],
        "kalos 1": ["Chespin", "Fennekin", "Froakie"],
        "alola 1": ["Rowlet", "Litten", "Popplio"],
        "galar 1": ["Grookey", "Scorbunny", "Sobble"],
        "paldea 1": ["Sprigatito", "Fuecoco", "Quaxly"]
    }
    starters_second = {
        "kanto 2": ["Ivysaur", "Charmeleon", "Wartortle"],
        "johto 2": ["Bayleef", "Quilava", "Croconaw"],
        "hoenn 2": ["Grovyle", "Combusken", "Marshtomp"],
        "sinnoh 2": ["Grotle", "Monferno", "Prinplup"],
        "unova 2": ["Servine", "Emboar", "Dewott"],
        "kalos 2": ["Quilladin", "Braixen", "Frogadier"],
        "alola 2": ["Dartrix", "Torracat", "Brionne"],
        "galar 2": ["Thwackey", "Raboot", "Drizzile"],
        "paldea 2": ["Floragato", "Crocalor", "Quaxwell"]
    }
    starters_third = {
        "kanto 3": ["Venusaur", "Charizard", "Blastoise"],
        "johto 3": ["Meganium", "Typhlosion", "Feraligatr"],
        "hoenn 3": ["Sceptile", "Blaziken", "Swampert"],
        "sinnoh 3": ["Torterra", "Infernape", "Empoleon"],
        "unova 3": ["Serperior", "Chandelure", "Samurott"],
        "kalos 3": ["Chesnaught", "Delphox", "Greninja"],
        "alola 3": ["Decidueye", "Incineroar", "Primarina"],
        "galar 3": ["Rillaboom", "Cinderace", "Inteleon"],
        "paldea 3": ["Meowscarada", "Skeledirge", "Quaquaval"]
    }

    if region_name in starters_first:
        planta = starters_first[1]
        fuego = starters_first[2]
        agua = starters_first[3]
    def BuscarPlanta():
        time.sleep(1)
        pokeinfo = Pokedex(planta,url_base)
        PokeDisplay(pokeinfo)
        print()
    def BuscarFuego():
        time.sleep(2)
        pokeinfo = Pokedex(fuego,url_base)
        PokeDisplay(pokeinfo)
        print()
    def BuscarAgua():
        time.sleep(3)
        pokeinfo = Pokedex(agua,url_base)
        PokeDisplay(pokeinfo)

    IniPlanta = threading.Thread(target= BuscarPlanta)
    IniFuego = threading.Thread(target=BuscarFuego)
    IniAgua = threading.Thread(target=BuscarAgua)

    IniPlanta.start()
    IniFuego.start()
    IniAgua.start()



def get_region(region_name):
    region = ["kanto","johto","hoenn","sinnoh","unova","kalos","alola","galar","paldea"]
    if region_name in region:
        IsRegion = True
        print("its a match!")
        pass
    else:
        IsRegion = False

    return IsRegion