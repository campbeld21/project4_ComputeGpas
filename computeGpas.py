#David Campbell 
import os
import sys

def main():
	filepath = "input.txt"
	f = open(filepath, "r")
	lines = [] 
	lines = f.readlines()
	
	for line in lines:
		line.split(' ')
		print(line)

	f.close()
	#print(lines)
	return

if __name__ == "__main__":
	main()
