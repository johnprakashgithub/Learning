known_users = ["Alice","Bob","Claire","Dan","Emma","Fred","Georgie","Harry"]

print(len(known_users))

while True:
    print("Hi, My name is Travis")
    name = input("What is your name ?: ").strip().capitalize()
    if name in known_users:
        print("Hello {}!".format(name))
        remove = input("Would you like to be removed from the system (y/n) ?: ").strip().lower()
        if remove == "y":
            print("Before removing {} from the list {}".format(name, known_users))
            known_users.remove(name)
            print("After removing {} from the list {}".format(name, known_users))
        elif remove == "n":
            print("Nothing happened !!!")
    else:
        print("Name NOT recognised!!!")
        print("Hmmm I don't think I have met you yet {}".format(name))
        add_me = input("Would you like to be added to the system (y/n) ?: ").strip().lower()
        if add_me == "y":
            known_users.append(name)
    check = input("Do you want to continue (y/n)? ").strip().lower()
    if check == "y":
        pass
    else:
        break
