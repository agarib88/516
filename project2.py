@Exercise 18:

import nltk
from nltk import *

from nltk.book import text7 #this line imports the specific text from which I will be retreiving the 50 most reoccuring bigrams

sampleText = [w for w in text7] #This line lists all the words from text 7  ---Since Python is case-sensitive, I need a line that makes all words lower-case so that they are all identified correctly by Python. 
#So this function  Makes a list of all the words in lower case
    
stopword = nltk.corpus.stopwords.words('english') #This line lists all stopwords from the NLTK corpus that are in the English language.

textBigram = bigrams(sampleText) #This is a function that takes the list of words in "sampleText" and creates all possible bigrams

bigramNoStopword = []  #This list is initiated to hold any bigrams with no stopwords
for x in textBigram: #This is a for loop and what it does it that for any member/item (x) in textBigram itirates over all bigrams in textBigram
    if x[0] not in stopword and x[1] not in stopword:# This conditional checks if the first (x[0]) or second words (x[1]) of bigrams is in the stopword list 
        if x[0].isalpha() and x[1].isalpha():#this other conditional checks if neither of the first and second words of the bigram are actual words and if they are 
          #alphabet then it removes punc. marks  (.isalpha() checks if the item is a word)
            bigramNoStopword.append(x) #this function appends(adds) bigrams wiht above properties/features
                                        #to the bigramNoStopword list  

bigramfreq = FreqDist(bigramNoStopword) #now we have a list of bigrams - this function of fre dis craete a sorted list of frequntly occuring words in the list of nostopwords
print(bigramfreq.most_common(5)) # this function prints the 5o most frequent bigrams




#Exercise 19:

import nltk
from nltk.corpus import brown
from nltk import ConditionalFreqDist
nltk.download('brown')

# Get genres available in brown corpus
genres = brown.categories() #this line categozies all categories in the Brown Corpus.

#genres  = ['edotorial', 'news', ...] #
word_genre = [] #this line creates an empty list for the following data 

for genre in genres: #this line loops through all genres in the above categories of genre in Brwon corpus; that is, it iterates over genres
    # Get words for each genre in brown corpus
    #worditheNewsgere = ['The', 'Fulton', 'County', 'Grand', 'Jury', 'said', ...]
    for item in brown.words(categories=genre): # this line loops through all words in brown that have the category as genre (
        # Create a list of (genre, word) pairs
        word_genre.append([genre, item])# this line creates a list of 'genre and word' pairs  

cfdist = ConditionalFreqDist(word_genre)
selected_genres = ["reviews", "news"]#, "editorial", "government", "mystery", "adventure"]
# My selected conjunctive adverbs for evaluation
conjunctive_adverbs = ["incidentally", "lately", "additionally", "equally", "regardless", "anyway", "undoubtedly", "otherwise", "instead"]

#conclusion: 
# Generate table of occurances
cfdist.tabulate(conditions=selected_genres, samples=conjunctive_adverbs) #conditions is what I want to tabuate for 
