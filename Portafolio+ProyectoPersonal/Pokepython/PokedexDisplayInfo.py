import PokedexTranslation
PokeTranslate = PokedexTranslation.type_translation
from googletrans import Translator
import time

# Create an instance of Translator
traductor = Translator()


#pip install googletrans

def PokeDisplay(pokeinfo):
    if pokeinfo:
        print(f"Pokémon #{pokeinfo["id"]}: {pokeinfo["name"].capitalize()}")
        print(f"Altura: {pokeinfo["height"]} pies   Peso: {pokeinfo["weight"]} libras")

        types = [t['type']['name'] for t in pokeinfo['types']]
        translated_types = [PokeTranslate.get(t, t) for t in types]
        types_str = ", ".join(translated_types)
        print(f"Tipos: {types_str.capitalize()}")

        abilities = [a['ability']['name'] for a in pokeinfo['abilities']]
        abilities_str = ", ".join(abilities)
        extra_filter = abilities_str
        print(f"Habilidad(es): {abilities_str}")

        pass
pass