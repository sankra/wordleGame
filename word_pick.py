'''
This code randomly picks a 5 letter word
from all the 5 letter words possible in english language.

I achieved this by using ntlk library of python.
nltk:- Natural Language Tool Kit
I have used random module to pick the 5 letter word randomly
from list words given by ntlk.
'''

import random
from nltk.corpus import words

# # Download the word corpus if not already done
# import nltk
# nltk.download('words')


# Get all 5-letter words from the nltk word list
def word_pick():
    five_letter_words = [word.upper() for word in words.words() if len(word) == 5]

# Pick a random word
    random_word = random.choice(five_letter_words)
    return random_word 
# print(f"Random 5-letter word: {random_word}")
