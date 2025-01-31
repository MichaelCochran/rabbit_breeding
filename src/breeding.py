<<<<<<< Tabnine <<<<<<<
import sqlite3#-
import sys
from datetime import datetime, timedelta

from utils import Utils
from database_helper import DatabaseHelper#+

con = sqlite3.connect("rabbits.db")#-
cur = con.cursor()#-
db = DatabaseHelper("rabbits.db")#+


def later_date(input_date, days):
    # Convert input_date string to a datetime object
    input_date = datetime.strptime(input_date, "%B %d")
    # Add the specified number of days to the input_date
    later_date = input_date + timedelta(days=days)
    # Return the later date as a string
    return later_date.strftime("%B %d")

# Outputs the information stored in the database
def view():
            print("Female\tBreed Date\tBuck\tPalpate\tNest Box\tKindling Date\tComments")#-
            # Print data in the table#-
            rows = cur.fetchall()#-
            for row in cur.execute("SELECT * FROM rabbits"):#-
                print("\t".join(str(cell) for cell in row))#-
            print("\n")#-
            return#-
    print("Female\tBreed Date\tBuck\tPalpate\tNest Box\tKindling Date\tComments")#+
    rows = db.view_data()#+
    for row in rows:#+
        print("\t".join(str(cell) for cell in row))#+
    print("\n")#+

def create_tables(cur):#-
    # Create table for the females with certain criterion#-
    cur.execute('''#-
        CREATE TABLE IF NOT EXISTS rabbits (#-
            name TEXT,#-
            last_bred TEXT,#-
            buck TEXT,#-
            palpatate TEXT,#-
            nest_date TEXT,#-
            due_date TEXT,#-
            comments TEXT#-
        )#-
    ''')#-

#+
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
    insert_data(data["name"], data["bred"], data["buck"], palpatating, nest, due, data["comments"])#-
    db.insert_data(data["name"], data["bred"], data["buck"], palpatating, nest, due, data["comments"])#+

def insert_data(name, bred, buck, palpitating, nest, due, comments):#-
    try:#-
        # Insert a row of data#-
        cur.execute("INSERT INTO rabbits VALUES (?, ?, ?, ?, ?, ?, ?)", (name, bred, buck, palpitating, nest, due, comments))#-
        # Save (commit) the changes to the database#-
        con.commit()#-
        print("\nData added to file")#-
    except Exception as e:#-
        # Handle exceptions gracefully#-
        print("Error:", e)#-
    finally:#-
        # Return to the main options after a button press#-
        print("\n Press any key to continue ... \n")#-
        input()#-
        Utils.clear()#-
    # Return to the main options after a button press#+
    print("\n Press any key to continue ... \n")#+
    input()#+
    Utils.clear()#+

    return#-


#+
if __name__ == "__main__":
    create_tables(cur)#-
    db.create_tables()#+

    Utils.clear()

    # Print blank line before anything happens and then look for input for view or input data and call appropriate function
    print("")
    while True:
        input_or_view = input("Would you like to Input data, View data, or Exit? (I/V/E) ").lower()
        if input_or_view == "i":
            print("\n")
            gather_data()
        elif input_or_view == "v":
            Utils.clear()
            view()
        elif input_or_view == "e":
            Utils.clear()
            con.close()#-
            db.close_connection()#+
>>>>>>> Tabnine >>>>>>># {"source":"chat"}
            sys.exit()
        else:
            print("Invalid input. Please enter 'I' to input data, 'V' to view data, or 'E' to exit.")
