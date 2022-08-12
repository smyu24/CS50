# TODO
from csv import reader, DictReader
from sys import argv
import csv
from cs50 import SQL

if len(argv) != 2 and (argv[2] != "Gryffindor" or argv[2] != "Hufflepuff" or argv[2] != "Ravenclaw" or argv[2] != "Slytherin"):
    print("Usage error: roster.py house")
    exit(1)

db = SQL("sqlite:///students.db")

#sort last name then
sorted_list = {}
sorted_list = db.execute("SELECT * FROM students WHERE house = ? ORDER BY last, first;", argv[1])

#print(sorted_list)
#print(sorted_list['first'], sorted_list['middle'], sorted_list['last'], sorted_list['birth'])


for temp in sorted_list:
    if temp['middle'] == None:
        print(temp['first'], temp['last'] + ", born", temp['birth'])
    else:
        print(temp['first'], temp['middle'], temp['last'] + ", born", temp['birth'])


#In roster.py, write a program that prints a list of students for a given house in alphabetical order.

#Your program should accept the name of a house as a command-line argument.
#If the incorrect number of command-line arguments are provided, your program should print an error and exit.
#Your program should query the students table in the students.db database for all of the students in the specified house.
#Your program should then print out each student’s full name and birth year (formatted as, e.g., Harry James Potter, born 1980 or Luna Lovegood, born 1981).
#Each student should be printed on their own line.
#Students should be ordered by last name. For students with the same last name, they should be ordered by first name.