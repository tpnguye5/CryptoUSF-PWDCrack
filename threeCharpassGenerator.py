#take in file, this will be output file
import random, passlib.pwd
from passlib import pwd
import math

file ="dictionary.txt"
outfile = open(file, 'w')
checker =[]
count = 0
while count <= (math.factorial(26)):
    #factorial 26 to get all the possible combination of passwords from a-z
    p = pwd.genword(length = 3)
    if p not in checker:
        checker.append(p)
        outfile.write(p + "\n")
    count+=1
outfile.close()