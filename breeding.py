import sqlite3
import sys
from os import system, name
from datetime import datetime, timedelta

con = sqlite3.connect("rabbits.db")
cur = con.cursor()

# See what system is running to use appropriate command to clear the screen
def clear():
    if name == "nt":
        system("cls")
    else:
        system("clear")

def later_date(input_date, days):
    # Convert input_date string to a datetime object
    input_date = datetime.strptime(input_date, "%B %d")
    # Add the specified number of days to the input_date
    later_date = input_date + timedelta(days=days)
    # Return the later date as a string
    return later_date.strftime("%B %d")

# Outputs the information stored in the database
def view():
            print("Female, Breed Date, Buck, Palpatate, Nest Box, Kindling Date, Comments")
            # Print data in the table
            for row in cur.execute("SELECT * FROM rabbits"):
                print("\t".join(str(cell) for cell in row))
            # break
            print("\n")
            return
            

def create_tables(cur):
    # Create table for the females with certain criterion
    cur.execute('''CREATE TABLE IF NOT EXISTS rabbits
                (name text, last_bred text, buck text, palpatate text, nest_date text, due_date text, comments text)''')

def gather_data():
    print("Please enter the following information for the doe.")
    name = input("What is the name of the rabbit? ")
    bred = input("What date was it bred? (Month and day, ex. May 5) ")
    buck = input("Which buck was bred? ")
    comments = input("What other comments do you have? ")
    palpatating = later_date(bred, 15)
    nest = later_date(bred, 27)
    due = later_date(bred, 31)
    print(palpatating, nest, due)
    insert_data(name, bred, buck, palpatating, nest, due, comments)

def insert_data(name, bred, buck, palpatating, nest, due, comments):
    # Insert a row of data
    cur.execute("INSERT INTO rabbits VALUES (?, ?, ?, ?, ?, ?, ?)",(name, bred, buck, palpatating, nest, due, comments))
    # Save (commit) the changes to the database
    con.commit()
    print("Data added to file")
    # View database prompt
    view()

# cur.execute("DROP TABLE rabbits")

if __name__ == "__main__":
    create_tables(cur)
    
    clear()

    # Print blank line before anything happens and then look for input for view or input data and call appropriate function
    print("")
    input_or_view = ""
    while input_or_view != "i" or input_or_view != "I" or input_or_view != "v" or input_or_view != "V":
        input_or_view = input("Would you like to Input data, View data, or Exit? (I/V/E) ")
        if input_or_view == "i" or input_or_view == "I":
            print("\n")
            gather_data()
        elif input_or_view == "v" or input_or_view == "V":
            clear()
            view()
        elif input_or_view == "e" or input_or_view == "E":
            clear()
            break


            con.close()
