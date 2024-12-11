import random
array = ["bob", "jake", "john"]


def get_word():
    word = array[random.randint(0,len(array)-1)]
    print(word)

get_word()

