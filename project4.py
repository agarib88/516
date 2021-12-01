# open a file 
with open('project3_example_text.txt') as project3_example_doc:
    project3_example_content = project3_example_doc.read()
# print(project3_example_content)

# find the annotation 
import re
project3_annotation = re.findall(r"\[\[.+?\]\]\(\(.+?\)\)", project3_example_content)
# print(project3_annotation)

#separate the annotation into different files by tags
with open('output1.txt', 'w') as output1_doc:
    output_tag1 = re.findall("\[\[.+?\]\]\(\(Establishing a niche_Indicating a gap\)\)", str(project3_annotation))
    output_tag1_lines = '\n'.join(output_tag1)
    output1_doc.write(str(output_tag1_lines))


with open('output2.txt', 'w') as output2_doc:
    output_tag2 = re.findall("\[\[.+?\]\]\(\(Establishing a territory_Making topic generalizations\)\)", str(project3_annotation))
    output_tag2_lines = '\n'.join(output_tag2)
    output2_doc.write(str(output_tag2_lines))

# write all of the annotation lines
with open('output0.txt', 'w') as output0_doc:
    output0_lines = '\n'.join(project3_annotation)
    output0_doc.write(str(output0_lines))
    
    
    
    
    
    
    
    
    
    
    


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
