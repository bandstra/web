import nltk
import os

# Retrieve a file list
files = os.listdir('.')
print "All the files in the directory:"
for file in files:
	if file.endswith('.txt'):
		print file

file_name = raw_input("Choose a file: ")

print "The file that was chosen is {0}".format(file_name)

from nltk.corpus import PlaintextCorpusReader
corpus_root = "."
search_text = PlaintextCorpusReader(corpus_root,file_name)
search_text = nltk.Text(search_text.words())

keyword = raw_input("Specify a search term: ")

search_text.concordance(keyword,80,lines=30)