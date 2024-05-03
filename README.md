# Overview

This is a project that began its life as an assignment for school that I have gone back to improve and see if I can make perform as well as I originally would have liked for it to but I was not able at the time because of the lack of knowledge. It is a database that can store information regarding the breeding of rabbits. It helps to track which buck and which doe are being the most productive. By knowing which animals are most productive, you know which animals to keep breeding for the best gains.

Since this is continued from an assignement there will be some large changes from the following video, but it shows how it behaved at the time of submission for class. When the time comes that I feel like I have finished this project I will share a different video showcasing the improvements made.

[Software Demo Video](https://youtu.be/5o7wtbrOkB0)

# Relational Database

There are two tables in this database. One is for information regarding the male rabbits, and one is for the female rabbits. Each table has datapoints that are specific to the gender. For example, the female table has a place to put information about the nest box and expected kindling date whereas the male table does not. 

# Development Environment

This was written using Python 3.9.6 and SQLite3 in VSCode 1.74.2. 

I included an extra that this program could have done without, but it makes it look a little more professional. I imported the system and name from the os library which allows me to see which system this program is being run on and then clears the terminal screen of any previous output before the program outputs anything.

# Useful Websites

- [SQLite](https://www.sqlitetutorial.net/)
- [TutorialsPoint](https://www.tutorialspoint.com/sqlite/sqlite_python.htm)

# Future Work

- This program could be adapted to help track other animals that could be found on a farm/homestead including goats, pigs, cows, etc.
- A GUI would make this program more appealing to most users.
- I need to add a way to edit information that is saved to the tables.
- I should separate some of the information inserted into the female table so that it is not all entered at the beginning. Maybe move that information to a new table.
- I need to find a better way to handle the database as a whole; open, close, etc. needs to be done better.
