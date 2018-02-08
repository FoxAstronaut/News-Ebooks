import random

def gen_dict(texts):
    dictionary = {}
    for sent in texts:
        words = sent.split()
        for word1, word2 in gen_pairs(words):
            key = (word1)
            if key in dictionary:
                dictionary[key].append(word2)
            else:
                dictionary[key] = [word2]
    return dictionary

def gen_pairs(words):
    if len(words) < 2:
        return
    for i in range(len(words) - 1):
        yield(words[i], words[i+1])

def markov(texts):
    f_texts = []
    for t in texts:
        f_texts.append("BEGIN " + t + " END")
    dictionary = gen_dict(f_texts)
    sentence = []
    word = "BEGIN"
    finsentence = None

    while True:
        word = random.choice(dictionary[(word)])
        if word == "END":
            if finsentence in texts or finsentence == None:
                sentence = []
                word = "BEGIN"
                finsentence = ""
                word = random.choice(dictionary[(word)])
            else:
                break
        sentence.append(word)
        finsentence = " ".join(sentence)
    return finsentence
