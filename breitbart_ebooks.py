import json,random

headlines = []

def loadJSON():
    with open('breitbart.json', encoding='utf-8') as json_data:
        d = json.load(json_data)
        count = 0;
        for i in d['articles']:
            headlines.append("BEGIN " + i['title'] + " END")
loadJSON()

def chainer():
    chain = {}
    for head in headlines:
        words = head.split()
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

def markov():

    chain = chainer()

    headline = []
    word = "BEGIN"

    while True:
        word = random.choice(chain[(word)])
        if word == "END":
            finheadline = " ".join(headline)
            if ("BEGIN " + finheadline + " END") in headlines:
                headline = []
                word = "BEGIN"
            else:
                break
        headline.append(word)
    return finheadline

print(markov())
