def printCategories():
    print("1. NBA for $200")
    print("2. Movie for $400")
    print("3. Politics for $600")
    print("4. Overwatch for $800")
    print("5. Random for $1,000")
    print("6. Exit")

def printNBA():
    print("1. Michael Jordan")
    print("2. Wilt Chamberlin")
    print("3. Lebron James")
    print("4. Kobe Bryant")

categoryResponse = 0

while categoryResponse >=0 and categoryResponse <=5 and categoryResponse !=6:
    print("\nSelect one of the following options:")
    printCategories()

    categoryResponse = input("\nYour Selection: ")
    try:
        categoryResponse = int(categoryResponse)
    except:
        categoryResponse = 0

    if(categoryResponse == 1):
        print("\nWhat NBA player had the highest AVG PPG:")
        printNBA()

        questionResponse = input("\nYour Selection: ")
        try:
            questionResponse = int(questionResponse)
        except:
            questionResponse = 0

        if(questionResponse == 1):
            print("\nThat is correct.")
        elif(questionResponse != 1 and questionResponse != 0):
            print("\nSorry. That is incorrect.")
        elif(questionResponse == 0):
            print("[[Unable to convert response to a number.]]")
        else:
            print("[[Unexpected Input Error]]")

    elif(categoryResponse == 2):
        print("\n[Triva Question for Movies]")
    elif(categoryResponse == 3):
        print("\n[Politics Question for Movies]")
    elif(categoryResponse == 4):
        print("\n[Overwatch Question for Movies]")
    elif(categoryResponse == 5):
        print("\n[Random Question for Movies]")
    elif(categoryResponse == 5):
        print("\nThanks for Playing. Goodbye.")
    else:
        print("\n[[Invalid Input Error]]")
