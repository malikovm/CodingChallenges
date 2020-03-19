pokeFile = open("pokemon.csv", "r")
pokeString = pokeFile.read().strip()
pokeFile.close()
filePrint = (input("Do you want to list all pokemon? (Y/N)")).lower()
if filePrint == "y": print(pokeString)
pokeList = pokeString.split(", ")
prefix = input("Enter the first few characters of the desired Pokemon name: ")

