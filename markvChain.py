# coding: utf-8
from urllib.request import urlopen
from random import randint

__author__ = 'szq'


def word_list_sum(wor_list):
    total = 0
    for word, value in wor_list.items():
        total += value
    return total


def retrieve_random_word(wor_lst):
    rand_index = randint(1, word_list_sum(wor_lst))
    for word, value in wor_lst.items():
        rand_index -= value
        if rand_index <= 0:
            return word


def build_word_dict(text):
    # Remove newLines and quotes
    text = text.replace("\n", " ")
    text = text.replace("\"", "")
    # Make sure punctuation marks are treated as their own "words"
    # so that they will be include in the Markov chain
    punctuation = [',', '.', ';', ':']
    for symbol in punctuation:
        text = text.replace(symbol, " " + symbol + "")
    words = text.split(" ")
    # Filter out empty words
    words = [word for word in words if word != ""]
    word_dict = {}
    for i in range(1, len(words)):
        if words[i - 1] not in word_dict:
            # Create a new dictionary for this word
            word_dict[words[i - 1]] = {}
        if words[i] not in word_dict[words[i - 1]]:
            word_dict[words[i - 1]][words[i]] = 0
        word_dict[words[i - 1]][words[i]] += 1
    return word_dict


url = "http://pythonscraping.com/files/inaugurationSpeech.txt"
text1 = str(urlopen(url).read(), 'utf-8')
word_dic = build_word_dict(text1)
# Generate a Markov chain of length 100
length = 100
chain = ""
current_word = "I"
for j in range(0, length):
    chain += current_word + " "
    current_word = retrieve_random_word(word_dic[current_word])
print(chain)
