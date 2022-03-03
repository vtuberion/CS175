# CS175L-50
# Vincent Tuberion
# CalculateAverage.py
# Last Modified 2/28/2022 19:17 EST

# ---------- IMPORT EXTERNALS ----------
import my_random

# Generating placeholder variables to be used in the computations
# V1 variables
'''score1 = 0
score2 = 0
score3 = 0
score4 = 0
score5 = 0'''
# V2 variables
scoreRange = 5
scoreList = []
scoreTotal = 0


# ---------- FUNCTION CREATIONS ----------
# Calculate the average of the 5 scores
def calc_average(total):
    average = total/5
    return average

# Assign a letter grade based on a given number input
def determine_grade(gradeNumber):
    gradeLetter = ""  # Placeholder local variable creation to be set and then returned at the end
    if gradeNumber >= 90:  # Anything above a 90 is an A letter grade
        gradeLetter = "A"
    elif 80 <= gradeNumber < 90:  # 80s turn into a B letter grade
        gradeLetter = "B"
    elif 70 <= gradeNumber < 80:  # 70s turn into a C letter grade
        gradeLetter = "C"
    elif 60 <= gradeNumber < 70:  # 60s turn into a D letter grade
        gradeLetter = "D"
    else:
        gradeLetter = "F"  # Anything lower than a 60 will be considered failing, yielding an F letter grade
    return gradeLetter  # Output the letter grade to wherever it needs to go


# V1 Only, number input not taken in V2
# Assign valid input to a variable, keep harassing the user until they provide what they are asked to.
'''def checkForInt(prompt):
    validInput = False  # Local placeholder variable
    while not validInput:  # Loop to keep asking the user until valid input is given
        userInput = input(prompt)  # Take in new input
        # My code in the past has had a history of being broken by Shrek/Bee Movie script, stop long inputs now
        if len(userInput) > 10:
            print("Okay, first of all, what kind of numbers are you putting in? Cut it out and do it right >:|")
        else:
            # If the input is not an excessive length, see if the string is actually a number input
            if userInput.isnumeric():  # Check if the number is actually a number
                userInput = float(userInput)  # Turn input into a float for decimal handling and formatting purposes
                validInput = True  # Everything checks out, user may proceed to the next step of the program
            else:
                # Print an error message and make the user input data again
                print("Invalid Input, please try again")
    return userInput  # Assign the good user input to the variable that the function call is assigned to
'''


# Ask the user if they wish to repeat the program
def repeat(prompt):
    validInput = False  # Local placeholder variable
    while not validInput:  # Loop to keep asking the user until valid input is given
        userInput = input(prompt)  # Take in new input
        # Same as checkForInt(), prevent excessive user input length
        if len(userInput) > 10:
            print("That is nowhere near what input you were asked to provide... do it again, CORRECTLY")
        else:
            userInput = userInput.lower()  # Turn input to lowercase to handle more input situations
            if userInput == "yes":
                print("Preparing another calculation for you, please stand by...")
                validInput = True  # The input is valid, they said yes so we return true to run program again
                return True
            elif userInput == "no":
                print("Ending Program, thank you for using our services!")
                validInput = True  # The input is valid, they said no so we return false to end the program
                return False
            else:
                # Input is not valid, make the user try again
                print("Invalid Input, please try again. (Please use 'yes' or 'no')")

# ---------- MAIN PROGRAM ----------
running = True
while running:  # Main loop to keep the program running, variable 'running' is the sentinel variable of the loop
    # V1 Only, number input not taken in V2
    # Take in only valid input for the 5 scores
    '''score1 = checkForInt("Enter score 1: ")
    score2 = checkForInt("Enter score 2: ")
    score3 = checkForInt("Enter score 3: ")
    score4 = checkForInt("Enter score 4: ")
    score5 = checkForInt("Enter score 5: ")'''
    # V2 features
    # Clear total and scoreList in case user looped program (we don't want to double the list)
    scoreList = []
    scoreTotal = 0
    for i in range(1, scoreRange+1):
        scoreList.append(my_random.my_random(1, 100))
        scoreTotal += scoreList[i-1]
        print("New Auto-Generated Score:", scoreList[i-1])
    # ---------- PROGRAM OUTPUT ----------
    print(f'''Score		Numeric Grade	Letter Grade
----------------------------------------------------''')
    # V2 changed to list iteration print from multiline format print statement that did 5 scores individually
    for i in range(1, scoreRange+1):
        print(f"score {i}:	    {scoreList[i-1]:.2f}		{determine_grade(scoreList[i-1])}")
    print(f"Average score:	{calc_average(scoreTotal):.2f}	    {determine_grade(calc_average(scoreTotal))}")
    # Run the function repeat() to check user input and see if user wants to run program again
    running = repeat("Would you like to make another calculation? ('yes'/'no')\n")
