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

def printMovie():
    print("1. The Blue Pill")
    print("2. The Red Pill")

def printPolitics():
    print("1. William Mckinley")
    print("2. Woodrow Wilson")
    print("3. Herbert Hoover")
    print("4. Calvin Coolidge")

def checkAnswer(answerToQuestion):
    questionResponse = input("\nYour Selection: ")
    try:
        questionResponse = int(questionResponse)
    except:
        questionResponse = 0

    if(questionResponse == answerToQuestion):
        print("\nThat is correct.")
    elif(questionResponse != answerToQuestion and questionResponse != 0):
        print("\nSorry. That is incorrect.")
    elif(questionResponse == 0):
        print("[[Unable to convert response to a number.]]")
    else:
        print("[[Unexpected Input Error]]")

categoryResponse = 0
while categoryResponse >= 0 and categoryResponse <= 5:
    print("\nSelect one of the following options:")
    printCategories()

    categoryResponse = input("\nYour Selection: ")
    try:
        categoryResponse = int(categoryResponse)
    except:
        categoryResponse = 0

    # NBA Category
    if(categoryResponse == 1):
        print("\nWhat NBA player had the highest AVG PPG:")
        printNBA()

        checkAnswer(1)

    # Movies Category
    elif(categoryResponse == 2):
        print("In the Matrix, does Neo take the blue pill or the red pill?: ")
        printMovie()

        checkAnswer(1)

    # Movies Category
    elif(categoryResponse == 3):
        print("Who ran for President of the United States with the campaign slogan 'A chicken in every pot and a car in every garage?'")
        printPolitics()

        checkAnswer(3)

    # Overwatch Category
    elif(categoryResponse == 4):
        print("\n[Trivia Question for Overwatch]")

    # Random Category
    elif(categoryResponse == 5):
        print("\n[Trivia Question for Random]")

    # Program Exit
    elif(categoryResponse == 6):
        print("\nThanks for Playing. Goodbye.")
    else:
        print("\n[[Invalid Input Error]]")
