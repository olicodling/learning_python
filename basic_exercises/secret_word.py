from random_word import RandomWords
from PyDictionary import PyDictionary

dictionary=PyDictionary()
random_words = RandomWords()

secret_word = (random_words.get_random_word(maxLength=8))
guess = ""
guess_count = 0
guess_limit = 3
out_of_guesses = False
define_the_word = ""

#print(secret_word)

if secret_word == "":
    print("What the devil, there's no secret word specified! Bailing.")
    quit()
else:
    while guess != secret_word and not (out_of_guesses):
        if guess_count < guess_limit:
            guess = input("Guess my secret word: ")
            guess_count += 1
        else: 
            out_of_guesses = True
        
if out_of_guesses:
    print("Out of guesses, you lose sucka! The secret word was " + secret_word)
else:
    print("You win, congrats!")
    
define_the_word = input("Type yes if you want to know the definition of the secret word: ")

if define_the_word == "yes":
    print("Here's the defintion ") 
    print(dictionary.meaning(secret_word))
else:
    print("No problemo, see you next time.")
