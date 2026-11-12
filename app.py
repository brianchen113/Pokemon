import json
## Open the JSON file of pokemon data
pokedex = open("./pokedex.json", encoding="utf8")
## create variable "data" that represents the enitre pokedex list
data = json.load(pokedex)
print(data[0])


    






# Create a function that will take the data from the JSON file and you will iterate through the list of pokemon and print each pokemons name.
x = int
x = 0
def english(x, y):
    for i in range(x, y):
        print(data[i]["name"]['english'])

english(0, len(data))
# Add a language choice feature and print the pokemons name based on the user input

def japanese(x, y):
    for i in range(x, y):
        print(data[i]["name"]['japanese'])

def chinese(x, y):
    for i in range(x, y):
        print(data[i]["name"]['chinese'])

def french(x, y):
    for i in range(x, y):
        print(data[i]["name"]['french'])

choice = str(input("Would you like to see the names of the pokemon in English, Chinese, Japanese, or French? "))
if choice == "English":
    english(0, len(data))
if choice == "Chinese":
    chinese(0, len(data))
if choice == "Japanese":
    japanese(0, len(data))
if choice == "French":
    french(0, len(data))
   
# Develop a function that creates a new list of pokemon based on the type the user searched for. If no pokemon was found of that type inform the user
typemon = []
type = str(input("What type of pokemon would you like to see? "))
def element(x, y):
    for item in range(x, y):
            if type == (data[item]["type"]):
                typemon.append(data[item]["name"]['english'])
element(0, len(data))
#Develop a function to find all pokemon matching the name the user searched for. Ex. if "Char" return Charmander, Charmeleon and Charizard. Make the user aware if no pokemon was found. 


#Based on user input, show all moves that a pokemon could learn based on their type. For example, if Charizard is fire/fyling, show all fire and flying moves. HINT import the moves.json file too!

