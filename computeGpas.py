#David Campbell 
import os
import sys


#filepath = "input.txt"
#f = open(filepath, "r")
lines = [] 

for line in sys.stdin:
	separatedValues = line.split(' ')
	lines.append(separatedValues)

print(lines)
