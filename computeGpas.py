# David Campbell
import os
import sys
import pprint

print("        NAME    GPA   #")
def calculateGPA(letter, gpa, credit):
	#calculates intermediate GPA (grade * credit only)
	if letter == 'A':
		gpa_temp = 4.0
	elif letter == 'A-':
		gpa_temp = (4.0-0.33)
	elif letter == 'A+':
		gpa_temp = (4.0+0.33)
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

def sumCredits(inCredit, sumCredits):
    	# sum up credits
	sumCredits += inCredit
	return(sumCredits)

def main():
	lines = [] 
	for line in sys.stdin:
		separatedValues = line.split(' ')
		lines.append(separatedValues)
	#print(lines)
	#first_line = {1: "Name"}
	gradebook = {} #list of student dictionaries
	#gradebook.update(first_line)
	for line in lines:
		# save first and last name in format of expect.txt
		fullName = line[5]+', '+line[4] #check this if there is an extra line at the bottom 
		
		#print(fullName)
		
		flag = 0
		# check if student name already exists in list and add
		for key,value in gradebook.items():
			if key == fullName:
				flag = 1 #found name
				# update GPA
				grade = line[6].strip('\n')
				ret = calculateGPA(grade, gradebook[key]["gpa"], int(line[3]))
				if (ret == "ignore"):
					continue
				else:
					gradebook[key]["gpa"] = ret	
				# update credits 
				gradebook[key]["credits"] = sumCredits(int(line[3]), gradebook[key]["credits"])
		if flag == 0:
			grade = line[6].strip() # strip method helps deal with the new line values in input file
			#student not in gradebook yet, insert with new values
			ret_gpa = calculateGPA(grade, 0.0, int(line[3]))
			if ret_gpa == "ignore":
                        	continue
                        # update credits 
			ret_cred = sumCredits(int(line[3]), 0)
			student = {
				fullName: 
				{
					"name": fullName,
					"gpa": ret_gpa,
					"credits": ret_cred,
					"nameLength": name_len
				}
			}
			
			gradebook.update(student) #insert new student into gradebook
			
	#pprint.pprint(gradebook)
	for key,value in gradebook.items():
		# traverse dictionary and finish GPA calculation
		gradebook[key]["gpa"] /= gradebook[key]["credits"]
		gradebook[key]["gpa"] = round(gradebook[key]["gpa"], 2)
	#pprint.pprint(gradebook)
	#attributesofGradebook = gradebook.keys()

	#replace the brackets with spaces
	#pprint.pprint(students)
	maxLength = 0 
	for key in gradebook:
		temp = len(gradebook[key]["name"])
		if len(gradebook[key]["name"]) > maxLength:
			maxLength = len(gradebook[key]["name"])

		gradebook[key]["nameLength"] = temp
			#print(gradebook[key]["name"])
			#print(maxLength)
		
	
	for key in gradebook:
    	difference = maxLength - gradebook[key]["nameLength"]
    		
		print(gradebook[key]["name"], difference, gradebook[key]["gpa"], gradebook[key]["credits"])
	#print(maxLength)
	#pprint.pprint(str(gradebook).replace("{", "").replace("}", "\n"),)
	#pprint.pprint(gradebook)
			
if __name__ == '__main__':
	main()
