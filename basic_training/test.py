from random_word import RandomWords
import time



random_words = RandomWords()

secret_word = (random_words.get_random_word(maxLength=8))

#time.sleep(3) # Sleep for 3 seconds

print(secret_word)