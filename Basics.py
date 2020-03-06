class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Film:
    def __init__(self, name, ageRequirement, numberOfSeatsAvailable):
        self.name = name
        self.ageRequirement = ageRequirement
        self.numberOfSeatsAvailable = numberOfSeatsAvailable

def checkForFilm(filmCollection, userChoice):
    for film in filmCollection:
        if film.name == userChoice:
            return True
    return False

def getValidFilm(filmColleciton, userChoice):
    for film in filmCollection:
        if film.name == userChoice:
            return film
    return None

film1 = Film("Finding Dory", 3, 5)
film2 = Film("Bourne Identity", 18, 5)
film3 = Film("Tarzan", 15, 0)               # Tester for no available seats
film4 = Film("Ghost Busters", 12, 5)

filmCollection = {film1, film2, film3, film4}

while True:
    choice = input("Enter the name of the film you wish to watch: ").strip().title()
    isValidFilm = checkForFilm(filmCollection, choice)

    #check if film name exists in film collection
    if isValidFilm:
        usersChosenFilm = getValidFilm(filmCollection, choice)
        userAge = int(input("How old are you?: ").strip())

        #check user age against the choosen film's minimum age requirement
        if userAge >= usersChosenFilm.ageRequirement:
            #check if there are enough seats available to accomodate the user
            availableSeatCount = usersChosenFilm.numberOfSeatsAvailable
            if availableSeatCount > 0:
                print("Enjoy the film!")
                usersChosenFilm.numberOfSeatsAvailable -= 1
            elif availableSeatCount <= 0:
                print("Sorry we are sold out!")    
            else:
                print("Unexpected Error: Available Seats")  
        elif userAge < usersChosenFilm.ageRequirement:
            print("You are too young to see that film!")
        else:
            print("Unexpected error: User age vs age requirement.")
    elif not isValidFilm:
        print("We don't have that film...")
    else:
        print("Unexpected error: Valid Film")
