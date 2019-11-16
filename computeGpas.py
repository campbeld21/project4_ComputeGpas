#David Campbell 
import os
import sys

def computeGpas():
	lines = [] 

	for line in sys.stdin:
		separatedValues = line.split(' ')
		lines.append(separatedValues)
		#print(separatedValues)	
		#print(lines)

	grades = []
	for line in lines:
		# traverse lines list of lists and use list comprehension to grab each name and calculate grade

		# save first and last name in format of expect.txt
		student = []
		name = line[5]+', '+line[4]
		student.append(name)

		# check if student name already exists in list
		for s in grades:
			if student in s:
				# add to existing value 
				# GPA
				# gpas that are already in grades are in s[1]
				if line[6] == 'A':
					s[1] += 4.0
				elif line[6] == 'A-':
					s[1] += (4.0-0.33)
				elif line[6] == 'A+':
					s[1] += (4.0+0.33)
				elif line[6] == 'B':
					s[1] += 3.0
				elif line[6] == 'B-':
					s[1] += (3.0-0.33)
				elif line[6] == 'B+':
					s[1] += (3.0+0.33)
				elif line[6] == 'C':
					s[1] += 2.0
				elif line[6] == 'C-':
					s[1] += (2.0-0.33)
				elif line[6] == 'C+':
					s[1] += (2.0+0.33)
				elif line[6] == 'D':
					s[1] += 1.0
				elif line[6] == 'D-':
					s[1] += (1.0-0.33)
				elif line[6] == 'D+':
					s[1] += (1.0+0.33)
				elif line[6] == 'F':
					s[1] += 0.0
				else:
					continue #ignore if grade is wrong
				# add number of credits - s[2]
				s[2] += line[3]	
			else:
				# set to 0 and add values
			
		
