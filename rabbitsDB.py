import sqlite3
import sys
from os import system, name

con = sqlite3.connect("rabbits.db")
cur = con.cursor()

# This function takes the input to determine male or female and calls the corresponding function
def gender():
    gender_status = ""
    while gender_status != "m" or gender_status != "M" or gender_status != "f" or gender_status != "F":
        gender_status = input("Is this rabbit male or female? (m/f) ")
        if gender_status == "m" or gender_status == "M":
            gather_data_male()
            break
        elif gender_status == "f" or gender_status == "F":
            gather_data_female()
            break
        else:
            print("Please enter m or f ")

# Outputs the information stored in the database
def view():
    view = ""
    while view != "y" or view != "Y" or view != "n" or view != "N":
        view = input("Would you like to see the database? ")
        if view == "y" or view == "Y":
            print("Male")
            # Print Male table
            for row in cur.execute("SELECT * FROM male_rabbits"):
                print(row)
            print("Female")
            # Print Female table
            for row in cur.execute("SELECT * FROM female_rabbits"):
                print(row)
            break

        elif view == "n" or view == "N":
            # Close the connection when done with it
            con.close()
            sys.exit()

def create_tables(cur):
    # Create table for the males with certain criterion
    cur.execute('''CREATE TABLE IF NOT EXISTS male_rabbits
                (name text, last_bred text, doe text, kits_born text, eight_weeks_weight text, comments text)''')

    # Create table for the females with certain criterion
    cur.execute('''CREATE TABLE IF NOT EXISTS female_rabbits
                (name text, last_bred text, buck text, nest_date text, due_date text, kindled tex, kits_born_alive text,
                kits_born_dead text, kits_weaned text, eight_weeks_weight text, comments text)''')

def gather_data_male():
    name = input("What is the name of the rabbit? ")
    bred = input("What date was it bred? ")
    doe = input("Which doe was bred? ")
    kits = input("How many kits resulted from this breeding? ")
    weight = input("What is the average weight of the kits at 8 weeks? ")
    comments = input("What other comments do you have? ")
    insert_data_male(name, bred, doe, kits, weight, comments)

def gather_data_female():
    name = input("What is the name of the rabbit? ")
    bred = input("What date was it bred? ")
    buck = input("Which buck was bred? ")
    nest = input("What is the date for the nest box? (28 days after breeding) ")
    due = input("What is the projected due date? (31 days after breeding) ")
    kindled = input("What date did she kindle? ")
    kits = input("How many live kits resulted from this breeding? ")
    dead = input("How many dead kits were there? ")
    weaned = input("How many kits survived past weaning? ")
    weight = input("What is the average weight of the kits at 8 weeks? ")
    comments = input("What other comments do you have? ")
    insert_data_female(name, bred, buck, nest, due, kindled, kits, dead, weaned, weight, comments)

def insert_data_male(name, bred, doe, kits, weight, comments):
    # Insert a row of data
    cur.execute("INSERT INTO male_rabbits VALUES (?, ?, ?, ?, ?, ?)",(name, bred, doe, kits, weight, comments))

    # Save (commit) the changes to the database
    con.commit()
    print("Male added to file")

    # View database prompt
    view()

def insert_data_female(name, bred, buck, nest, due, kindled, kits, dead, weaned, weight, comments):
    # Insert a row of data
    cur.execute("INSERT INTO female_rabbits VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",(name, bred, buck, nest, due, kindled, kits, dead, weaned, weight, comments))

    # Save (commit) the changes to the database
    con.commit()
    print("Female added to file")

    # View database prompt
    view()

# cur.execute("DROP TABLE female_rabbits")
# cur.execute("DROP TABLE male_rabbits")

if __name__ == "__main__":
    create_tables(cur)

    # See what system is running and use appropriate command to clear the screen
    if name == "nt":
        system("cls")
    else:
        system("clear")

    # Print blank line before anything happens and then look for input for view or input data and call appropriate function
    print("")
    input_or_view = ""
    while input_or_view != "i" or input_or_view != "I" or input_or_view != "v" or input_or_view != "V":
        input_or_view = input("Would you like to Input data or View data? (I/V) ")
        if input_or_view == "i" or input_or_view == "I":
            print("\n")
            gender()
            break
        elif input_or_view == "v" or input_or_view == "V":
            print("\n")
            print("Male")
            for row in cur.execute("SELECT * FROM male_rabbits"):
                print(row)
            print("Female")
            for row in cur.execute("SELECT * FROM female_rabbits"):
                print(row)
            print("\n\n")
            break
