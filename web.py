# require
import sys
import nltk
import os
import operator
import re

# corpus root is ~/cs195/web

files = os.listdir('.')
print "Available text files"
for file in files:
	 if file.endswith(".txt"):
	 	print file

# get input; needs sanity checking
#file_name = sys.argv[1]
#search_word = sys.argv[2]

file_name = raw_input("\nChoose one of these files: ")

print "\nThe file that will be examined is {0}".format(file_name)

from nltk.corpus import PlaintextCorpusReader
corpus_root = '.'
search_text = PlaintextCorpusReader(corpus_root,file_name)
search_text = nltk.Text(search_text.words())


# KWIC concordance
search_word = raw_input("Specify a search word for a keyword in context concordance list: ")
search_text.concordance(search_word,80,lines=1000)

# Apply stopwords to search_text
from nltk.corpus import stopwords
stopwords = nltk.corpus.stopwords.words('bible')
#/Users/barrybandstra/nltk_data/corpora/stopwords
search_text = [word for word in search_text if word.lower() not in stopwords]

# Write search to output.txt file"
output_file = open("output.txt", "w")
for line in search_text:
	output_file.write(line),"\n"
output_file.close()

# Frequency distribution vocabulary list; fd is a dictionary
fd = nltk.FreqDist(search_text)

fd_freq = raw_input("\nFrequency distribution of terms.\nMinimum frequency: ")
fd_freq = int(fd_freq)


print "Frequency distribution of terms in",file_name,"sorted by frequency"
# http://stackoverflow.com/questions/613183/sort-a-python-dictionary-by-value
p = re.compile('\d+')
for (key,value) in sorted(fd.items(), key=operator.itemgetter(1), reverse = True):
	if value > fd_freq - 1:
		# Checks for chapter/verse numbers and skips over them if found
		m = p.match(key)
		if not m:
			print key,value
			
# Vocabulary
vocab = sorted(set(search_text))
print "Vocabulary: ",vocab


