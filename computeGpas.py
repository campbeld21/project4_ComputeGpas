#David Campbell 
import os
import sys


#filepath = "input.txt"
#f = open(filepath, "r")
lines = [] #array that contains everything 

for line in sys.stdin:
	separatedValues = line.split(' ')
	lines.append(separatedValues)
	#lines.append(separatedValues)

grades = []
for line in lines:
    #traverse lines list of lists and use list comprehension to grab each name and calculate grade
	curr_first = line[4] #first name
	curr_last = line[5] #last name 

	#save first and last name in format of last, first
	student = []
	name = line[5] + ', ' + line[4]
	student.append(name)
	
	# check if student name already exists in list
	for s in grades:
    	if student in s:
    		#add gpa to existing value
			# gpas that are already in grades are in s[1]
			if line[6]  == 'A':
    				s[1] += 4.0
			elif line[6]  == 'A-':
    				s[1] += 3.7
			elif line[6]  == 'B+':
    				s[1] += 3.3
			elif line[6]  == 'B':
					s[1] += 3.0
			elif line[6]  == 'B-':
    				s[1] += 2.7
			elif line[6]  == 'C+':
    				s[1] += 2.3
			elif line[6]  == 'C':
    				s[1] += 2.0
			elif line[6]  == 'C-':
    				s[1] += 1.7
			elif line[6]  == 'D':
    				s[1] += 1.0
			elif line[6]  == 'A':
    				s[1] += 0.7
			elif line[6]  == 'F':
    				s[1] += 0.0
		else:
    		continue #ignore if grade is wrong
    	
		#number of credits 
		s[2] += s[3] #add number of credits to eventual output string

	# save and calculate gpa 
	gpa = 0.0


#print(lines)
