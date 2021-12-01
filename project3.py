#Project 3: Write a script in Python that converts British spelling of a text to the American spelling using at least two generalizable replacement patterns. 
#“Generalizable” means applicable to more than one lexeme. For example, replacing “fireman” with “firefighter” is not generalizable, but replacing “theatre” with “theater” is. 
#Your script should read an input text file and write an output text file. The names of the input and output files may be hard-coded in the script.

import re
# I created lines of code that are as short as possible. The first one below reads the input file 
# which is in British English
data = open('british_english.txt').read()

# The following line changes words ending with 're' to 'er'
processed_data = re.sub(r"\b(\w+)re\b", r"\1er", data) #\1=matches the same text as the most recently matched by the 1st capturing word. 
#\w = matches any word character. \b = asserts position at a word boundary. 

# This second function change words ending with 'our' to 'or'
processed_data = re.sub(r"\b(\w+)our\b", r"\1or", processed_data)

# The last line saves American English version of the original text to another text file
open("american_english.txt", "w+").write(processed_data)
