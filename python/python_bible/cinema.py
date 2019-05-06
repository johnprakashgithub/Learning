films = {
    "Finding Dory": [3,5],
    "Tarzen": [15,5],
    "Bourny": [18,5],
    "Ghost Busters": [12,5]
}

while True:

    choice = input("What film would you like to watch? ").strip().title()
    if choice in films:

        age = int(input("How old are you? ").strip())

        # check user age
        if age >= films[choice][0]:

            # check enough seats
            num_seats = films[choice][1]
            seats = int(input("Available seats {}. How many seats? ".format(num_seats)).strip())
            if num_seats >= seats:
                print("Enjoy the film!")
                films[choice][1] = films[choice][1] - 1
            else:
                print("Sorry, we are sold out!")
        else:
            print("You are too young to see that film!")
    else:
        print("We do not have that film..")
        print("Films avialable: {}".format(films))
        new = input("How about adding the movie {} (y/n) ? ".format(choice)).strip().lower()
        if new == "y":
            age_limit = int(input("Age limit of movie {}? ".format(choice)).strip())
            films [choice] = [age_limit,5]
    check = input("Do you want to continue (y/n)? ").strip().lower()
    if check == "y":
        pass
    else:
        exit()
