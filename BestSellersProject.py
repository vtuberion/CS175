# CS175L-50
# Juliana Gomez, Adnan Hoti, Vincent Tuberion
# BestSellersProject.py
# Last Modified 4/5/2022 11:45 EST

# https://docs.google.com/spreadsheets/d/1DTfvU2GFAV3FK3G3FIOcRwx4A6RrY9yMvqOMIHSm8qY/edit?usp=sharing

bestSellerList = []


def getYearRange():
    # Check for valid input for year to search, keep asking user until valid input is given
    valid_input = False
    while not valid_input:
        # rangeStart is the first year of the range of publish dates to search from
        rangeStart = input("Enter start year: ")
        try:
            # If the input can be converted to an integer, it is valid. This omits unintended string text entries
            rangeStart = int(rangeStart)
            valid_input = True  # The input was able to be converted and is therefore valid input
        except ValueError:  # The data was not able to be converted to integer form, thus not being valid integer input
            print("INPUT ERROR: Data is not valid year, please try again")
    # Check for valid input for year to search, keep asking user until valid input is given
    valid_input = False
    while not valid_input:
        # rangeEnd is the last year of the range of publish dates to search from
        rangeEnd = input("Enter end year: ")
        try:
            # If the input can be converted to an integer, it is valid. This omits unintended string text entries
            rangeEnd = int(rangeEnd)
            valid_input = True  # The input was able to be converted and is therefore valid input
        except ValueError:  # The data was not able to be converted to integer form, thus not being valid integer input
            print("INPUT ERROR: Data is not valid year, please try again")
    # Search the file for the intended data
    # resultsFound will be False by default
    # If anything read in the file matches the search query, resultsFound will be True
    resultsFound = False
    for index in range(len(bestSellerList)):  # Iterate through each entry in the list
        # Each bestSellerList index has book data, bestSellerList[index][3] is the publication date of the current book
        # bestSellerList[index][3][2] is the year of publication of the current book data being read
        # If the books publication year falls between the start and end years given by the user, print the matching data
        if int(bestSellerList[index][3][2]) >= rangeStart and int(bestSellerList[index][3][2]) <= rangeEnd:
            resultsFound = True
            # method to output something that looks like: BookTitle by: BookAuthor (pub date: MM/DD/YYYY)
            print(bestSellerList[index][0], "by:", bestSellerList[index][1], "(pub date:",
                  (bestSellerList[index][3][0] + "/" + bestSellerList[index][3][1] + "/" +
                   bestSellerList[index][3][2]) + ")")
    # If all data was checked and nothing matches the query, output a message that no results were found
    if not resultsFound:
        print("We searched through the records and no results were found. :/")


def getMonthYear():
    # Check for valid input for month to search, keep asking user until valid input is given
    valid_input = False
    while not valid_input:
        # month is the number of the month from 1-12 that the user wants to search for
        month = input("Enter month(1 - 12): ")
        try:
            # If the input can be converted to an integer, it is valid. This omits unintended string text entries
            month = int(month)
            # Make sure input is between 1 and 12, anything else is invalid
            if month >= 1 and month <= 12:
                valid_input = True  # The input was able to be converted and is between 1-12, therefore valid input
            else:
                # User's input was a valid integer but falls outside of required range between 1 and 12
                print("Not a valid month.")
        except ValueError:  # The data was not able to be converted to integer form, thus not being valid integer input
            print("INPUT ERROR: Data is not valid year, please try again")
    # Check for valid input for year to search, keep asking user until valid input is given
    valid_input = False
    while not valid_input:
        # month is the number of the year that the user wants to search for
        year = input("Enter year: ")
        try:
            # If the input can be converted to an integer, it is valid. This omits unintended string text entries
            year = int(year)
            valid_input = True
        except ValueError:  # The data was not able to be converted to integer form, thus not being valid integer input
            print("INPUT ERROR: Data is not valid year, please try again")
    # Search the file for the intended data
    # resultsFound will be False by default
    # If anything read in the file matches the search query, resultsFound will be True
    resultsFound = False
    for index in range(len(bestSellerList)):  # Iterate through each entry in the list
        # Each bestSellerList index has book data, bestSellerList[index][3] is the publication date of the current book
        # bestSellerList[index][3][0] is the month of publication of the current book data being read
        # bestSellerList[index][3][2] is the year of publication of the current book data being read
        # If the books publication matches month and year given by the user, print the matching data
        if int(bestSellerList[index][3][0]) == month and int(bestSellerList[index][3][2]) == year:
            resultsFound = True
            # method to output something that looks like: BookTitle by: BookAuthor (pub date: MM/DD/YYYY)
            print(bestSellerList[index][0], "by:", bestSellerList[index][1], "(pub date:",
                  (bestSellerList[index][3][0] + "/" + bestSellerList[index][3][1] + "/" +
                   bestSellerList[index][3][2]) + ")")
    # If all data was checked and nothing matches the query, output a message that no results were found
    if not resultsFound:
        print("We searched through the records and no results were found. :/")


def getAuthor():
    # Prompt the user for text to search with
    # author is the text data that the user wants to search for
    author = input("Enter search string: ")
    author = author.lower()  # remove any case sensitivity during search, we only care about matching text
    # Search the file for the intended data
    # resultsFound will be False by default
    # If anything read in the file matches the search query, resultsFound will be True
    resultsFound = False
    for index in range(len(bestSellerList)):  # Iterate through each entry in the list
        # Each bestSellerList index has book data, bestSellerList[index][1] is the author of the current book
        # If any text in author name matches text given by the user, print the matching data
        if author in bestSellerList[index][1].lower():  # .lower() removes casing for better results to match user input
            # method to output something that looks like: BookTitle by: BookAuthor (pub date: MM/DD/YYYY)
            print(bestSellerList[index][0], "by:", bestSellerList[index][1], "(pub date:",
                  (bestSellerList[index][3][0] + "/" + bestSellerList[index][3][1] + "/" +
                   bestSellerList[index][3][2]) + ")")
    # If all data was checked and nothing matches the query, output a message that no results were found
    if not resultsFound:
        print("We searched through the records and no results were found. :/")

def getTitle():
    # Prompt the user for text to search with
    # title is the text data that the user wants to search for
    title = input("Enter search string: ")
    title = title.lower()  # remove any case sensitivity during search, we only care about matching text
    # Search the file for the intended data
    # resultsFound will be False by default
    # If anything read in the file matches the search query, resultsFound will be True
    resultsFound = False
    for index in range(len(bestSellerList)):  # Iterate through each entry in the list
        # Each bestSellerList index has book data, bestSellerList[index][0] is the title of the current book
        # If any text in title name matches text given by the user, print the matching data
        if title in bestSellerList[index][0].lower():  # .lower() removes casing for better results to match user input
            resultsFound = True
            # method to output something that looks like: BookTitle by: BookAuthor (pub date: MM/DD/YYYY)
            print(bestSellerList[index][0], "by:", bestSellerList[index][1], "(pub date:",
                  (bestSellerList[index][3][0] + "/" + bestSellerList[index][3][1] + "/" +
                   bestSellerList[index][3][2]) + ")")
    # If all data was checked and nothing matches the query, output a message that no results were found
    if not resultsFound:
        print("We searched through the records and no results were found. :/")


def menu():
    # While program is active, running is True. When the user wants to end, running is set to False and the loop stops
    running = True
    while running:
        # Prompt the user to select a choice by entering a number or using "q" to quit and end the program
        user_input = input('''What would you like to do?
        1: Look up year range
        2: Look up month/year
        3: Search for author
        4: Search for title
        Q: Quit\n''')
        # The options to choose are only a single character, anything else is obviously invalid
        if len(user_input) > 1:
            print("Invalid Input: Input too long, not one of the listed options")
        else:
            # User input is only 1 character, it will now be checked to see what it is
            user_input = user_input.lower()
            if user_input == "1":
                getYearRange()
            elif user_input == "2":
                getMonthYear()
            elif user_input == "3":
                getAuthor()
            elif user_input == "4":
                getTitle()
            elif user_input == "q":
                print("Thank you for using our program!")
                running = False
            else:
                # The user's input was one character but was not one of the options
                print("Input is not valid")


def main():
    # Open a file named bestsellers.txt.
    try:
        file = open('bestsellers.txt', 'r')
        # Read each line from the file
        # Keep a count of how many lines of data were read
        books_read = 0
        for line in file.readlines():  # Iterate through every line in the file
            newIndex = line.strip('\n')  # Remove any newline characters
            # Split each piece of data into its own list (the data is separated by tabs)
            newIndex = newIndex.split("\t")
            bestSellerList.append(newIndex)  # Add the next list of book data into the BestSellerList as an new index
            bestSellerList[books_read][3] = bestSellerList[books_read][3].split("/")
            books_read += 1  # Add 1 to the book counter (Horray! Another book was read)
        # Inform the user how many books are in the list and that processing the data into a list was completed.
        print(f"I read {books_read} books")
        # Close the open text file. If the user suddenly quits the program during the menu, the data will be safe
        file.close()
        menu()
    except FileNotFoundError:  # Inform the user that the file was not found and the program cannot continue
        print("FileNotFoundError: Required file does not exist. 'bestsellers.txt' is missing")


# Call the main function.
if __name__ == '__main__':
    main()
