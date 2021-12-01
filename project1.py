#Exercise 24: 
#Comments
#The general approach was to create to short and clean codes that would make the whole process less confusing. It was challenging to understand what exercise 24 requested
#to do with the list and whether the code should be connected together or printing each condition on its own. Since the exercise listed the conditions separately and there 
#was no clear wording to connect them all, I created several vairables that would correspond to each condition separately.

python3
import nltk
from nltk.book import*

endWith_ise = [word for word in text6 if word.endswith('ise')] #this condition would list words in text 6 if the words end with 'ise'. 
print (endWith_ise) #executes the condition

contains_z = [word for word in text6 if 'z' in word] #this condition would list words that include 'z'
print (contains_z) #executes the condition

contains_pt = [word for word in text6 if 'pt'in word] #this condition would list words contain 'pt'
print (contains_pt) #executes the condition

contains_isTitle = [word for word in text6 if word.istitle()] #this condition would list words that begin with an uppercase letter.
print (contains_isTitle) #executes the condition


Feedback Update:
import nltk
from nltk.book import*
aliList = [word for word in text6 if word.endswith('ise') or 'z' in word or 'pt'in word or word.istitle()] #this condition would list 
#words in text 6 if the words end with 'endings'. 
print (aliList) #executes the condition

#Exercise 25:
#Comments

python3
import nltk
from nltk.book import*

sent = ['she', 'sells', 'sea', 'shells', 'by', 'the', 'sea', 'shore'] #defining the variable "sent" with a list of the given words..

contains_sh = [word for word in sent if word.startswith ('sh')] #this code looks for words that begin with 'sh' in the variable "sent"
print (contains_sh) #this prints the words that start with 'sh' in "sent"

word_greaterThan4 = [word for word in sent if len(word)>4] #this variable looks for words whose length is greater than 4 letters in the list of "sent"
print (word_greaterThan4) #this prints the words that are longer than 4 letters in "sent"


Feedback Update:
  
  sent = ['she', 'sells', 'sea', 'shells', 'by', 'the', 'sea', 'shore'] #defining the variable "sent" with a list of the given words..

contains_sh = [ ] #this code looks for words that begin with 'sh' in the variable "sent"
for word in sent :
    if word.startswith ('sh') and len(word)>4: # these are two contditions together and if this satifies, then add the word to the list.
        contains_sh.append(word)

print (contains_sh) #this prints the words that start with 'sh' in "sent"
word_greaterThan4 = [word for word in sent if len(word)>4] #this variable looks for words whose length is greater than 4 letters in the list of "sent"
print (word_greaterThan4) #this prints the words that are longer than 4 letters in "sent"

