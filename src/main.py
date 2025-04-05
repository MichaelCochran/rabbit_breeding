import modules

db = DatabaseHelper("rabbits.db")

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
