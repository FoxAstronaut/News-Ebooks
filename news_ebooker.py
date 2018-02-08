import config,api_handler,markov_chainer,natlang_chainer

def main():
    sources = ['breitbart-news','buzzfeed','daily-mail','hacker-news','the-guardian-uk','bbc-news']
    headlines = []
    for source in sources:
        headlines.extend(api_handler.loadHeadlines(source))
    #markov_chainer.markov(headlines))
    #natlang_chainer.natlang(headlines))

if __name__ == "__main__":
    main()
