#Exercise 18
import nltk
from nltk.corpus import stopwords
try: # Try store stopwords into sw variable, if an exception occurs then download stopwords then store them into sw variable 
    sw = stopwords.words('english')
except:
    nltk.download('stopwords')
    sw = stopwords.words('english')
# Split sequence into tokens, extract bigrams using nltk bigrams function and then convert to a list
bigrams = list(nltk.bigrams(sequence.split()))
# Convert stop words to set to do intersection with bigrams
set_sw = set(sw)
# Iterate over extracted bigrams to remove those with stop words
for bigram in bigrams:
    # convert bigrams to set to do intersection
    set_bigram = set(bigram)
    # If bigram intersects with stop words, then we want to skip it
    intersection = set_sw.intersection(set_bigram)
    if not intersection:
        # Convert tuple bigram to string to use as a key for the dictionary
        bigram_join = '_'.join(bigram)
        # Store occurances of each bigram in the dictionary
        if bigram_join not in dict_bigrams:
          dict_bigrams[bigram_join] = 1
        else:
            dict_bigrams[bigram_join] += 1
# Sort the dictionary of bigrams with most occurances to least
sorted_dict = sorted(dict_bigrams.items(), key=lambda item: item[1], reverse=True)
# Get the top 50 most occured bigrams
top_50_bigrams = sorted_dict[0:50]
# top_50_bigrams = [('really_great', 2), ('great_moving', 1), ('moving_parts', 1)]
# Convert string bigrams back to list of bigrams
result = []
for bigram in top_50_bigrams:
    bigram = bigram[0].split('')
    result.append((_bigram, bigram[1]))
# result = [(['really', 'great'], 2), (['great', 'moving'], 1), (['moving', 'parts'], 1)]


OR

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

from nltk.corpus import brown
from nltk import ConditionalFreqDist
nltk.download('brown')

# Get genres available in brown corpus
genres = brown.categories() #this line categozies all categories in the Brown Corpus.

#genres  = ['edotorial', 'news', ...] #
word_genre = [] #this line creates an empty list for the following data 

for item in genres: #this line loops through all genres in the above categories of genre in Brwon corpus; that is, it iterates over genres
    # Get words for each genre in brown corpus
    for word in brown.words(categories=genre): # this line loops through all words in brown that have the category as genre (
        # Create a list of (genre, word) pairs
        word_genre.append((genre, word))
        

brown.words(categories = 'news')
brown.words(categories = 'dfhs')
brown.words(categories = 'esdfsdotorial')
brown.words(categories = 'edotosdfsrial')



for item in categories:
   brown.words(categories = item)


# Create a conditional Frequency distribution object
cfdist = ConditionalFreqDist(word_genre)
# My selected genres for evaluation
selected_genres = ["reviews", "news", "editorial", "government", "mystery", "adventure"]
# My selected conjunctive adverbs for evaluation
conjunctive_adverbs = ["incidentally", "lately", "additionally", "equally", "regardless", "anyway", "undoubtedly", "otherwise", "instead"]

#conclusion: 
# Generate table of occurances
cfdist.tabulate(conditions=selected_genres, samples=conjunctive_adverbs)
