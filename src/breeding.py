import modules

def later_date(input_date, days):
    # Convert input_date string to a datetime object
    input_date = modules.datetime.strptime(input_date, "%B %d")
    # Add the specified number of days to the input_date
    later_date = input_date + modules.timedelta(days=days)
    # Return the later date as a string
    return later_date.strftime("%B %d")

# Outputs the information stored in the database
def view():
    print("Female\tBreed Date\tBuck\tPalpate\tNest Box\tKindling Date\tComments")
    rows = modules.db.view_data()
    for row in rows:
        print("\t".join(str(cell) for cell in row))
    print("\n")

def gather_data():
    modules.Utils.clear()
    print("Please enter the following information.")

    # Define questions and corresponding keys
    questions = {
        "name": "What is the name of the doe? ",
        "bred": "What date was she bred? (Type 'today' for today's date, or enter Month and day, ex. May 5): ",
        "buck": "Which buck was bred? ",
        "comments": "What other comments do you have? "
    }

    # Gather data
    data = {}
    for key, question in questions.items():
        if key == "bred":
            response = input(question).strip().lower()
            if response == "today":
                # Get today's date in "Month Day" format, e.g., "April 6"
                data[key] = modules.datetime.now().strftime("%B %d")
            else:
                data[key] = response
        else:
            data[key] = input(question)       

    # Calculate dates
    palpatating, nest, due = later_date(data["bred"], 15), later_date(data["bred"], 27), later_date(data["bred"], 31)

    # Display dates
    print("\nPalpatate, Nest box, Due")
    print(palpatating, nest, due)

    # Insert data
    modules.db.insert_data(data["name"], data["bred"], data["buck"], palpatating, nest, due, data["comments"])
    
    # Return to the main options after a button press
    print("\n Press any key to continue ... \n")
    input()
    modules.Utils.clear()


