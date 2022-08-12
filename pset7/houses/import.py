# TODO
from cs50 import SQL
from csv import reader, DictReader
from sys import argv
import csv

db = SQL("sqlite:///students.db")

if len(argv) != 2:
    print("Usage error: import.py characters.csv")
    exit(1)

with open(argv[1], "r") as c_csv:
    house_kids = list(csv.reader(c_csv))
#print(house_kids)
#print("\n\n")

for c in range(1, len(house_kids)):
    FML = house_kids[c][0].split(" ") #"First","Middle","Last"

    #print(FML)
    #print(c)
    #print(len(FML))
    if len(FML) == 3:
        db.execute("INSERT INTO students (first, middle, last, house, birth) VALUES(?, ?, ?, ?, ?)", FML[0], FML[1], FML[2], house_kids[c][1], house_kids[c][2])
    elif len(FML) == 2:
        FML.insert(1, None)
        db.execute("INSERT INTO students (first, middle, last, house, birth) VALUES(?, ?, ?, ?, ?)", FML[0], FML[1], FML[2], house_kids[c][1], house_kids[c][2])
#split()
#none if no middle name
#db.execute to insert into db

