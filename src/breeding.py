import sys
from datetime import datetime, timedelta

from utils import Utils
from database_helper import DatabaseHelper

db = DatabaseHelper("rabbits.db")


def later_date(input_date, days):
    # Convert input_date string to a datetime object
    input_date = datetime.strptime(input_date, "%B %d")
    # Add the specified number of days to the input_date
    later_date = input_date + timedelta(days=days)
    # Return the later date as a string
    return later_date.strftime("%B %d")

# Outputs the information stored in the database
def view():
    print("Female\tBreed Date\tBuck\tPalpate\tNest Box\tKindling Date\tComments")
    rows = db.view_data()
    for row in rows:
        print("\t".join(str(cell) for cell in row))
    print("\n")

def gather_data():
    Utils.clear()
    print("Please enter the following information.")

    # Define questions and corresponding keys
    questions = {
        "name": "What is the name of the doe? ",
        "bred": "What date was she bred? (Month and day, ex. May 5) ",
        "buck": "Which buck was bred? ",
        "comments": "What other comments do you have? "
    }

    # Gather data
    data = {}
    for key, question in questions.items():
        data[key] = input(question)

    # Calculate dates
    palpatating, nest, due = later_date(data["bred"], 15), later_date(data["bred"], 27), later_date(data["bred"], 31)

    # Display dates
    print("\nPalpatate, Nest box, Due")
    print(palpatating, nest, due)

    # Insert data
    db.insert_data(data["name"], data["bred"], data["buck"], palpatating, nest, due, data["comments"])
    
    # Return to the main options after a button press
    print("\n Press any key to continue ... \n")
    input()
    Utils.clear()


if __name__ == "__main__":
    db.create_tables()

    Utils.clear()

    # Print blank line before anything happens and then look for input for view or input data and call appropriate function
    print("")
    while True:
        # Prompt the user for input and convert it to lowercase
        input_or_view = input("Would you like to Input data, View data, or Exit? (I/V/E) ").lower()

        # Define a dictionary of actions corresponding to user inputs
        actions = {
            'i': lambda: gather_data(),  # If 'i' is entered, call gather_data function
            'v': lambda: (Utils.clear(), view()),  # If 'v' is entered, clear screen and call view function
            'e': lambda: (Utils.clear(), db.close_connection(), sys.exit())  # If 'e' is entered, clear screen, close DB connection, and exit
        }

        # Get the corresponding action for the user input, or None if input is invalid
        action = actions.get(input_or_view)
        if action:
            # If a valid action is found, execute it
            action()
        else:
            # If input is invalid, display an error message
            print("Invalid input. Please enter 'I' to input data, 'V' to view data, or 'E' to exit.")
