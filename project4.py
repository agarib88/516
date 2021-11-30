import os.path # this line imports the library that has a fetaure that tells whether a file exists or not to say the least 
# open a file 
file = input("please input file as .txt: ")
if os.path.exists(file):
    print("it exists")
else:
    print("please name file that exists: ")
    file = input()

#this opens the file and you give a path to open
file_doc = open(file)
file_content = file_doc.read()

print(file_content)

# find the annotation 
import re
file_annotation = re.findall(r"\[\[.+?\]\]\(\(.+?\)\)", file_content) #this line reads and finds all the what is between () that are within file_content
print(file_annotation)

# save the output as new lines (optimal version)
f = open('output.txt', "a+") #this means that if the file exists open but if it does not then create it
for item in file_annotation: #whatever annotation i found 
    f.write(str(item + '\n')) #then write the string out into the file
