#David Campbell 
import os
import sys

lines = [] 
#f = open('input.txt', 'r')

for line in sys.stdin:
    #print(line)
    separatedValues = line.split()
    lines.append(separatedValues)

print(lines)
