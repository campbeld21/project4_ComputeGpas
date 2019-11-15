#David Campbell 
import os
#file = "input.txt"


testdir = "testdir" #holds input.txt and output.txt 

if not os.path.isdir(testdir):
    print("Invalid test directory", testdir)
    exit(1)

for file in os.listdir(testdir):
    print(file)

readFile = open("input.txt" , "r")
print(readFile.read())


# for file in os.listdir(testdir):
#     if not os.path.isfile(testdir + "/" + file):
#         continue 

#     parts = file.split()
#     if not file.endswith(".txt"):
#         continue 


#     test = file[:-7]
    
#     #check matching output
#     if not os.path.isfile(testdir + "/" + test + ".out.txt"):
#         print("Input file '" + file + "' missing output")
#         continue
#     tests.append(test)