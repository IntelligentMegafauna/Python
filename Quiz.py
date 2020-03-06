users = ["James", "Tony", "Bob"]

guest = input("Hello my name is Sam. What is your name?: ").title().strip()

update_list = ""
while update_list != "y" and update_list != "n" and len(users) <= 10:
    if guest not in users:
        update_list = input("Would you like to be added to the list? (y/n)").strip().lower()
    elif guest in users:
        print("I see you're already on the list. Go on ahead inside.")
    else:
        print("Unexpected Error")

if update_list == "y":
    users.append(guest)
    print(guest + " has been added to the list.")
elif update_list == "n":
    print("Fine, then get out of here you scumbag ninney")
else:
    print("Unexpected Error")

print(users)
print(len(users))