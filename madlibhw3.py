print("START*******")

import nltk 
from nltk.book import *
import random
from nltk import word_tokenize, sent_tokenize
from nltk.corpus import gutenberg
#Nealon Suthersan

# Using text2 from the nltk book corpa, create your own version of the


# Requirements:
# 1) Only use the first 150 tokens
# 2) Pick 5 parts of speech to prompt for, including nouns
# 3) Replace nouns 15% of the time, everything else 10%

# Deliverables:
# 1) Print the orginal text (150 tokens)
# 1) Print the new text

tagged_tokens = nltk.pos_tag(text2) 
tagmap = {"NN":"a noun","NNS":"a plural noun","VB":"a verb","JJ":"an adjective", "RB": "an adverb"}
substitution_probabilities = {"NN":.15,"NNS":.15,"VB":.1,"JJ":.1, "RB":.1}

def spaced(word):
	if word in [",", ".", "?", "!", ":"]:
		return word
	else:
		return " " + word
final_words = []

orig = []
whole_text = tagged_tokens[:150] #creates variable with first 150 tokens
for (word, tag) in whole_text:
	if tag not in substitution_probabilities or random.random() > substitution_probabilities[tag]:
		final_words.append(spaced(word))
	else:
		new = input("Enter %s:"%(tagmap[tag])) #Asks for raw input
		final_words.append(spaced(new))


def spaced2(list2):
	list1 = []
	for word in list2:
		if word in [",", ".", "?", "!", ":"]:
			list1.append(word)
		else:
			list1.append(' ' + word)
	print(''.join(list1)) #joins list into a string
print ('\n')
print('Original Text')
s = tagged_tokens[:150]
for tuples in s:
	orig.append(tuples[0])
final_original = spaced2(orig)


print('\n')
print('Madlibs Text')
print("".join(final_words)) #joins into a string 



print("\n\nEND*******")
