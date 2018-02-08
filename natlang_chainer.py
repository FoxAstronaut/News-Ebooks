import nltk, random

def gen_patterns(texts):
    patterns = []
    for sentence in texts:
        tokens = sentence.split()
        tagged = nltk.pos_tag(tokens)
        pattern = []
        for t in tagged:
            pattern.append(t[1])
        patterns.append(pattern)
    return patterns

def gen_dict(texts):
    dictionary = {}
    for text in texts:
        words = text.split()
        tagged_words = nltk.pos_tag(words)
        for tagged_word in tagged_words:
            word = tagged_word[0]
            key = tagged_word[1]
            if key in dictionary:
                dictionary[key].append(word)
            else:
                dictionary[key] = [word]
    return dictionary

def natlang(texts):
    patterns = gen_patterns(texts)
    dictionary = gen_dict(texts)

    pattern = random.choice(patterns)
    sentence = []

    while True:
        for tag in pattern:
            word = random.choice(dictionary[(tag)])
            sentence.append(word)
        finsentence = " ".join(sentence)
        if finsentence in texts:
            sentence = []
        else:
            break
    return finsentence
