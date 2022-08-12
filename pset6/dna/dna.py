from csv import reader, DictReader
from sys import argv
import csv
#fopen for opening file
#print no match at end if


if len(argv) < 3:
    print("Usage error: dna.py database.csv sequence.txt")
    exit(1)

with open(argv[1],"r") as dnafile:
    dnareader = list(csv.reader(dnafile))
#    print("--------1")
#    print(dnareader)
    dnareader[0].remove("name")
#    print("--------2")
#    print(dnareader)
    init = dnareader[0] # this stores DNA strains that we look for


# sequence load
with open(argv[2]) as sequence:
    seq_data = sequence.read()

#print("--------3 seqdata")
#print(seq_data)

result = []

for i in range(len(init)):
    # i will have individual dan code that we.
    # aregoing to look for small -3 large -8 depending on the csv file
    previous_pos = 0
    position = 0
    max_cons_count = 0
    temp = 0
    while position < len(seq_data):
        position = seq_data.find(init[i],position)
        #print ("----------4 position")
        #print("STR: " + init[i])
        #print("position: " + str(position))
        #print("previous position: " + str(previous_pos))
        #print("max count: " + str(max_cons_count))
        #print("temp: " + str(temp))
        if position == -1: # this is if there is nothing that is found
            max_cons_count = 0
            break
        # if the sequence starts at the begining
        elif position != -1 and previous_pos == 0:
            max_cons_count += 1
            temp = max_cons_count
            previous_pos = position
        #--------------------------------------------
        #sequencial occurences find goes here
        elif position != 1 and previous_pos > 0: # check
            if int(previous_pos) + len(init[i])== int(position):#begin concurrency combo
                max_cons_count += 1
                previous_pos = position

                if temp < max_cons_count:#change temp to biggest combo
                    temp = max_cons_count
            elif int(previous_pos) + len(init[i]) != int(position):#concurrency ends
                max_cons_count = 1 #restart
                previous_pos = position
                if temp < max_cons_count:#change temp to biggest combo
                    temp = max_cons_count
        position += 1
    result.append(temp) # why IndexError: list assignment index out of range; num[temp] = max_cons_count
        #print("previous position: " + str(previous_pos))
        #print("max count: " + str(max_cons_count))
        #print("temp: " + str(temp))

    #for #comparision of values of dna list and sequence
    #make sure to add a if for no match
#compare with names in 2d list
#ex. init[i][0]   in a for loop
#another ex. number way (int(result[i]) == int(init[i][{forloop}]), repeat
#ADD ELSE: print("NO MATCH")
#print(dnareader)
#print(init)
#print(len(init))
#print(result)

#reader[0].add(".STRS")
temp = 0
temp2 = []

for r in range(1,len(dnareader)):
    temp = 0
    for c in range(len(result)):
        if int(dnareader[r][c+1]) == int(result[c]):
            temp += 1
    temp2.append(temp)
#print("temp1 = ", temp ,"temp 2 = " , temp2)
if len(init) in temp2:
    print(dnareader[temp2.index(len(init)) + 1][0])
else:
    print("No match")