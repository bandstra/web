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

print "\nThe file that will be analysed is {0}\n".format(file_name)

#from nltk.corpus import PlaintextCorpusReader
#corpus_root = '.'
#search_text = PlaintextCorpusReader(corpus_root,file_name)
#search_text = nltk.Text(search_text.words())

# Apply stopwords to search_text
#from nltk.corpus import stopwords
#stopwords = nltk.corpus.stopwords.words('bible')
#/Users/barrybandstra/nltk_data/corpora/stopwords
#search_text = [word for word in search_text if word.lower() not in stopwords]

#f = open(file_name)
f = '001:001 In the beginning God created the heavens and the earth. 001:002 Now the earth was formless and empty. Darkness was on the surface of the deep. God\'s Spirit was hovering over the surface of the waters. 001:003 God said, "Let there be light," and there was light. 001:004 God saw the light, and saw that it was good. God divided the light from the darkness. 001:005 God called the light Day, and the darkness he called Night. There was evening and there was morning, one day. 001:006 God said, "Let there be an expanse in the middle of the waters, and let it divide the waters from the waters." 001:007 God made the expanse, and divided the waters which were under the expanse from the waters which were above the expanse; and it was so. 001:008 God called the expanse sky. There was evening and there was morning, a second day. 001:009 God said, "Let the waters under the sky be gathered together to one place, and let the dry land appear;" and it was so. 001:010 God called the dry land Earth, and the gathering together of the waters he called Seas. God saw that it was good. 001:011 God said, "Let the earth put forth grass, herbs yielding seed, and fruit trees bearing fruit after their kind, with its seed in it, on the earth;" and it was so. 001:012 The earth brought forth grass, herbs yielding seed after their kind, and trees bearing fruit, with its seed in it, after their kind; and God saw that it was good. 001:013 There was evening and there was morning, a third day. 001:014 God said, "Let there be lights in the expanse of sky to divide the day from the night; and let them be for signs, and for seasons, and for days and years; 001:015 and let them be for lights in the expanse of sky to give light on the earth;" and it was so. 001:016 God made the two great lights: the greater light to rule the day, and the lesser light to rule the night. He also made the stars. 001:017 God set them in the expanse of sky to give light to the earth, 001:018 and to rule over the day and over the night, and to divide the light from the darkness. God saw that it was good. 001:019 There was evening and there was morning, a fourth day. 001:020 God said, "Let the waters swarm with swarms of living creatures, and let birds fly above the earth in the open expanse of sky." 001:021 God created the large sea creatures, and every living creature that moves, with which the waters swarmed, after their kind, and every winged bird after its kind. God saw that it was good. 001:022 God blessed them, saying, "Be fruitful, and multiply, and fill the waters in the seas, and let birds multiply on the earth." 001:023 There was evening and there was morning, a fifth day. 001:024 God said, "Let the earth bring forth living creatures after their kind, livestock, creeping things, and animals of the earth after their kind;" and it was so. 001:025 God made the animals of the earth after their kind, and the livestock after their kind, and everything that creeps on the ground after its kind. God saw that it was good. 001:026 God said, "Let us make man in our image, after our likeness: and let them have dominion over the fish of the sea, and over the birds of the sky, and over the livestock, and over all the earth, and over every creeping thing that creeps on the earth." 001:027 God created man in his own image. In God\'s image he created him; male and female he created them. 001:028 God blessed them. God said to them, "Be fruitful, multiply, fill the earth, and subdue it. Have dominion over the fish of the sea, over the birds of the sky, and over every living thing that moves on the earth." 001:029 God said, "Behold, I have given you every herb yielding seed, which is on the surface of all the earth, and every tree, which bears fruit yielding seed. It will be your food. 001:030 To every animal of the earth, and to every bird of the sky, and to everything that creeps on the earth, in which there is life, I have given every green herb for food;" and it was so. 001:031 God saw everything that he had made, and, behold, it was very good. There was evening and there was morning, a sixth day. 002:001 The heavens and the earth were finished, and all their vast array. 002:002 On the seventh day God finished his work which he had made; and he rested on the seventh day from all his work which he had made. 002:003 God blessed the seventh day, and made it holy, because he rested in it from all his work which he had created and made. 002:004 This is the history of the generations of the heavens and of the earth when they were created.'

text2tag = nltk.word_tokenize(f)
tagged_text = nltk.pos_tag(text2tag)

for i in tagged_text:
	if i[1].startswith('N'):
		print i[0]
		
		

