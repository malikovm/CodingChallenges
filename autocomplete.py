pokeFile = open("pokemon.csv", "r")
pokeString = pokeFile.read().strip()
pokeFile.close()
filePrint = (input("Do you want to list all pokemon? (Y/N)")).lower()
pokeList = pokeString.split(", ")
if filePrint == "y": print(*pokeList, sep = "\n")
prefix = input("Enter the first few letters of the desired Pokemon's name: ").strip()
prefix = prefix[0].upper() + prefix[1:].lower()
print("Looking for all Pokemon that start with \"{}\"...".format(prefix))
prefixLen = len(prefix)
outputPokelist = []
for mon in pokeList:
    if mon[:prefixLen] == prefix: outputPokelist.append(mon)
matches = len(outputPokelist)
if matches == 0: print("No Pokemon name starts with \"{}\"".format(prefix))
else:
    print(matches, " Pokemon start with \"{}\":".format(prefix))
    print(*outputPokelist, sep = ", ")

