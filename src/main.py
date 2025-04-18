import modules
from breeding import gather_data, view, delete_data, input_and_handle_entry #, economics, mating, growth, health, behavioral, animals

modules.db.create_tables()

modules.Utils.clear()

# Print blank line before anything happens and then look for input and call appropriate function
print("")
while True:
    # Prompt the user for input and convert it to lowercase
    input_or_view = input("Would you like to \033[4mI\033[0mnput, \033[4mV\033[0miew, \033[4mD\033[0melete, or E\033[4mx\033[0mit? ").lower()

    # Define a dictionary of actions corresponding to user inputs
    actions = {
        'i': lambda: (modules.Utils.clear(), input_and_handle_entry()),
        'v': lambda: (modules.Utils.clear(), view()),
        'd': lambda: (modules.Utils.clear(), delete_data()),
        'x': lambda: (modules.Utils.clear(), modules.db.close_connection(), modules.sys.exit()),
    }

    # Get the corresponding action for the user input, or None if input is invalid
    action = actions.get(input_or_view)
    if action:
        # If a valid action is found, execute it
        action()
    else:
        # If input is invalid, display an error message
        print("Invalid input. Please etry again.")

