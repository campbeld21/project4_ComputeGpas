# David Campbell

# COMPILE COMMAND
# python3 computeGpas.py < input.txt 

import os
import re
import sys
import pprint
from collections import OrderedDict
from operator import getitem

def calculateGPA(letter, gpa, credit):
	#calculates intermediate GPA (grade * credit only)
	if letter == 'A':
		gpa_temp = 4.0
	elif letter == 'A-':
		gpa_temp = (4.0-0.33)
	elif letter == 'A+':
		gpa_temp = (4.0)
	elif letter == 'B':
		gpa_temp = 3.0
	elif letter == 'B-':
		gpa_temp = (3.0-0.33)
	elif letter == 'B+':
		gpa_temp = (3.0+0.33)
	elif letter == 'C':
		gpa_temp = 2.0
	elif letter == 'C-':
		gpa_temp = (2.0-0.33)
	elif letter == 'C+':
		gpa_temp = (2.0+0.33)
	elif letter == 'D':
		gpa_temp = 1.0
	elif letter == 'D-':
		gpa_temp = (1.0-0.33)
	elif letter == 'D+':
		gpa_temp = (1.0+0.33)
	elif letter == 'F':
		gpa_temp = 0.0
	else:
		return("ignore") #if no grade in between A-F, ignore this parameter 
		
	return(gpa + (gpa_temp * credit))

# Method which sums the number 
# of credits for each student
def sumCredits(inCredit, sumCredits):
	# check if invalid credits
	if inCredit < 0:
		return(-1) #error return value
	sumCredits += inCredit
	return(sumCredits)

# Processes course, GPA, and credits to ensure they are valid
# and will return them if they are
def processLine(index, line, gradebook, fullName, flag):

	## COURSE PROCESSING
	#check validity of course name and number
	if (re.match('^[A-Z]+$', line[0])) == False or (line[1].isdigit() == False):
		print("Error: Course name invalid at line {}.\n".format(index+1))
		return(-1,-1,-1)
	# check if course was already added 
	course = line[0] + line[1] # 'CS273' is course string
	if flag == 1:
		# new student,  no course processing necessary, but if 1, need processing
		if course in gradebook[fullName]["classes"]:
			print("Error: {} was enrolled in the course {} more than once. Error in line {}.\n".format(fullName, course, index+1))
			return(-1,-1,-1)
	#otherwise add course to classes list in dictionary
	

	## GPA PROCESSING
	grade = line[6].strip('\n')
	if flag == 1:
		retGPA = calculateGPA(grade, gradebook[fullName]["gpa"], int(line[3]))
	elif flag == 0:
		retGPA = calculateGPA(grade, 0.0, int(line[3]))
	if (retGPA == "ignore"):
		print("Error: Invalid grade at line {}.\n".format(index+1))
		return(-1,-1,-1)
	

	## CREDIT PROCESSING
	if flag == 1:
		retCredit = sumCredits(int(line[3]), gradebook[fullName]["credits"])
	elif flag == 0:
		retCredit = sumCredits(int(line[3]), 0)
	if retCredit == -1:
		#invalid credit entry in line, print line for error messasge
		print("Error: Invalid number of credits in line {}\n".format(index+1))
		return(-1,-1,-1)
	#otherwise update credit number in gradebook
	return(course, retGPA, retCredit)

# Processes all courses and makes sure they are valid,
# if they are add the course and credits to the dictionary
def processCourses(lines):
	# print error message if a course is listed with different credits
	courses = {}
	for index,line in enumerate(lines):
		## LINE ENTRIES
		if line[0] == '\n':
			continue
		# if wrong number of entries on line skip (must be 7)
		if len(line) != 7 :
			continue
		flag = 0
		for key,value in courses.items():
			if key == (line[0]+line[1]):
				flag = 1
				if courses[key] != line[3]:
					print("Error: Course {} listed with differing number of credits on line {}.\n".format(key, index+1))
		if flag == 0:
			# add course and credits to dict
			new = {(line[0]+line[1]): line[3]}
			courses.update(new)
def main():
	lines = [] 
	for line in sys.stdin:
		# if empty line, skips that line
		separatedValues = line.split(' ')
		lines.append(separatedValues)

	## CHECK COURSE AND CREDIT COMBO
	processCourses(lines)

	gradebook = {} #list of student dictionaries
	for index,line in enumerate(lines):
		## LINE ENTRIES, accounts for empty first line
		if line[0] == '\n':
			continue
		# if wrong number of entries on line skip (must be 7)
		if len(line) != 7 :
			print("Error: Invalid number of items on line {}.\n".format(index+1))
			continue

		# save first and last name in format of expect.txt
		fullName = line[5]+', '+line[4] #check this if there is an extra line at the bottom 
		flag = 0
		# check if student name already exists in list and add
		for key,value in gradebook.items():
			if key == fullName:
				flag = 1 #found name
				#def processLine(index, line, gradebook, key, fullName):
				course, retGPA, retCredit = processLine(index, line, gradebook, fullName, flag)
				if course == -1:
					continue
				# else
				gradebook[key]["classes"].append(course)
				gradebook[key]["gpa"] = retGPA
				gradebook[key]["credits"] = retCredit
		if flag == 0:
			#def processLine(index, line, gradebook, key, fullName):
			course, retGPA, retCredit = processLine(index, line, gradebook, fullName, flag)
			if course == -1:
				continue
			student = {
				fullName:{
					"name": fullName,
					"gpa": retGPA,
					"credits": retCredit,
					"nameLength": 0,
					"classes": [course]
				}
			}
			gradebook.update(student) #insert new student into gradebook
			
	for key,value in gradebook.items():
		# traverse dictionary and finish GPA calculation
		if gradebook[key]["credits"] == 0:
			gradebook[key]["gpa"] = '----'
		else:
			gradebook[key]["gpa"] /= gradebook[key]["credits"]
			gradebook[key]["gpa"] = format(gradebook[key]["gpa"], '.2f')



	# This maxLength value was used with header length 
	# to format the names so they would 
	# all be in the same vertical column
	maxLength = 0 
	for key in gradebook:
		temp = len(gradebook[key]["name"])
		if len(gradebook[key]["name"]) > maxLength:
			maxLength = len(gradebook[key]["name"])
		gradebook[key]["nameLength"] = temp
	
	header_length = ' ' * (maxLength - 4)
	name_header = header_length + 'NAME'
	print(name_header + ' GPA  #')
	for key in gradebook:
		difference = maxLength - gradebook[key]["nameLength"]
		diff_str = ' ' * difference
		namePrint = diff_str + gradebook[key]["name"]
		gradebook[key]["name"] = namePrint #save the way we want to print it in dictionary

	ordered = OrderedDict(sorted(gradebook.items(), key = lambda x: getitem(x[1], "gpa"), reverse=True))
	if gradebook == {}:
		print("Error: No valid entries in input.\n")
	else:
		for key in ordered:
			print(ordered[key]["name"], ordered[key]["gpa"], ordered[key]["credits"])

if __name__ == '__main__':
	main()
