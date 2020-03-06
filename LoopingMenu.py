def printMenu():
    print("1. Print Greeting")
    print("2. Print Insult")
    print("3. Print Fact")
    print("4. Exit")

response = 0
while response >= 0 and response <= 3 and response != 4:
    print("\nSelect one of the following options:")
    printMenu()

    response = input("Your Selection: ")
    try:
        response = int(response)
    except:
        response = 0
        
    if(response == 1):
        print("Greetings stanger. Stay awhile and listen!")
    elif(response == 2):
        print("Your mother was a hamster and your father smelt of elderberries")
    elif(response == 3):
        print("Zammy is a sexy devil. :D")
    elif(response == 4):
        print("Exiting....")
    else:
        print("Unexpected error")


