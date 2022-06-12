import time
from nltk.corpus import wordnet

class Timer(object):
    """ Allows to count the time elapsed since the timer was started """

    def __init__(self):
        """ Initializes the timer """
        self.start()

    def __getCurrentTime():
        """ Return the current time """

        return time.time()

    def start(self):
        """ Starts the timer """

        self.__start = self.__getCurrentTime()

    def stop(self):
        """ Stops the timer """

        self.__end = self.__getCurrentTime()

    def getElapsedTime(self):
        """ Returns the elapsed time """
        return self.__end - self.__start

    def print(self):
        """ Prints the elapsed time """

        return print("\n\n==> Time elapsed: {}".format(self.__getElapsedTime()))

def getSynonyms(word):
    """ Returns the synonyms of a word """

    if not word:
        return []

    all_synonyms_with_ = { lemm.name() for syn in wordnet.synsets(word) for lemm in syn.lemmas() }
    all_synonyms_with_.add(word)
    
    if word[-1] != "s":
        all_synonyms_with_.add(word + 's')
        all_synonyms_with_.add(word + 'es')
    else:
        all_synonyms_with_.add(word[:-1])

    return list(map(lambda word_with_: word_with_.split("_"), all_synonyms_with_))