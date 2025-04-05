import modules

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


