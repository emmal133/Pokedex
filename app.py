import json
## Open the JSON file of pokemon data
pokedex = open("./pokedex.json", encoding="utf8")
## create variable "data" that represents the enitre pokedex list
data = json.load(pokedex)
language=input("What language do you want it in? (english, japanese, chinese, french)")

# Create a function that will take the data from the JSON file and you will iterate through the list of pokemon and print each pokemons name.

# Add a language choice feature and print the pokemons name based on the user input
for pokemon in data:
    if language=="english":
        print(pokemon["name"]["english"])
    if language=="japanese":
        print(pokemon["name"]["japanese"])
    if language=="chinese":
        print(pokemon["name"]["chinese"])
    if language=="french":
        print(pokemon["name"]["french"])
# Develop a function that creates a new list of pokemon based on the type the user searched for. If no pokemon was found of that type inform the user
type=input("What type of pokemon?(Steel, grass, poison, fire, flying, water, bug, normal, electric, ground, fighting, psychic, rock, steel, ice, ghost, fairy, dragon, dark, )")
for pokemon in data:
    print(pokemon["type"])
#Develop a function to find all pokemon matching the name the user searched for. Ex. if "Char" return Charmander, Charmeleon and Charizard. Make the user aware if no pokemon was found. 


#Based on user input, show all moves that a pokemon could learn based on their type. For example, if Charizard is fire/fyling, show all fire and flying moves. HINT import the moves.json file too!
                                                                                        
