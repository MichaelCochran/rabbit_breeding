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
    view = ""
    while view != "y" or view != "Y" or view != "n" or view != "N":
        view = input("Would you like to see the database? ")
        if view == "y" or view == "Y":
            print("Female")
            # Print data in the table
            for row in cur.execute("SELECT * FROM female_rabbits"):
                print("\t".join(str(cell) for cell in row))
            # break
        elif view == "n" or view == "N":
            # Close the connection when done with it
            con.close()
            sys.exit()

def create_tables(cur):
    # Create table for the females with certain criterion
    cur.execute('''CREATE TABLE IF NOT EXISTS female_rabbits
                (name text, last_bred text, buck text, palpatate text, nest_date text, due_date text, comments text)''')

def gather_data_female():
    print("Please enter the following information for the doe.")
    name = input("What is the name of the rabbit? ")
    bred = input("What date was it bred? (Month and day, ex. May 5) ")
    buck = input("Which buck was bred? ")
    # weight = input("What is the average weight of the kits at 8 weeks? ")
    comments = input("What other comments do you have? ")
    palpatating = later_date(bred, 15)
    nest = later_date(bred, 27)
    due = later_date(bred, 31)
    print(palpatating, nest, due)
    insert_data_female(name, bred, buck, palpatating, nest, due, comments)
    # gather_data_male()

def insert_data_female(name, bred, buck, palpatating, nest, due, comments):
    # Insert a row of data
    cur.execute("INSERT INTO female_rabbits VALUES (?, ?, ?, ?, ?, ?, ?)",(name, bred, buck, palpatating, nest, due, comments))
    # Save (commit) the changes to the database
    con.commit()
    print("Female added to file")
    # View database prompt
    view()

# cur.execute("DROP TABLE female_rabbits")
# cur.execute("DROP TABLE male_rabbits")

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
            # gender()
            gather_data_female()
        elif input_or_view == "v" or input_or_view == "V":
            print("\n")
            # print("Male")
            # for row in cur.execute("SELECT * FROM male_rabbits"):
            #     print(row)
            print("Female")
            for row in cur.execute("SELECT * FROM female_rabbits"):
                print(row)
            print("\n")
        elif input_or_view == "e" or input_or_view == "E":
            clear()
            break
