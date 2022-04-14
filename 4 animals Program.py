numAnimals = 0
allAnimals = ""

while numAnimals < 4:
    animalName = input("Enter an animal name or e to quit: ")
    if animalName.lower() == "e":
        print("exiting now");
        break
    elif animalName.isalpha():
        numAnimals +=1
        allAnimals = allAnimals + animalName + " "
    else: print("invalid aninal name, please try again\n")
if numAnimals == 0:
    print("no animals")
else:
    print("The names of the animals are:", allAnimals)