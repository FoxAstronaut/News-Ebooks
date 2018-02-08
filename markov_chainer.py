import random

def chainer(texts):
    chain = {}
    for sent in texts:
        words = sent.split()
        for word1, word2 in gen_dict(words):
            key = (word1)
            if key in chain:
                chain[key].append(word2)
            else:
                chain[key] = [word2]
    return chain

def gen_dict(words):
    if len(words) < 2:
        return
    for i in range(len(words) - 1):
        yield(words[i], words[i+1])

def markov(texts):
    f_texts = []
    for t in texts:
        f_texts.append("BEGIN " + t + " END")
    chain = chainer(f_texts)
    sentence = []
    word = "BEGIN"
    finsentence = None

    while True:
        word = random.choice(chain[(word)])
        if word == "END":
            if finsentence in texts or finsentence == None:
                sentence = []
                word = "BEGIN"
                finsentence = ""
                word = random.choice(chain[(word)])
            else:
                break
        sentence.append(word)
        finsentence = " ".join(sentence)
    return finsentence
