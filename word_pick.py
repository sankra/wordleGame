'''
This code uses the nltk library to
ge all the possible 5 letter words in english.
And this code returns the 5 letter word to the 
callable function.
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
