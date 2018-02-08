import config,api_handler,markov_chainer

def main():
    headlines = api_handler.loadHeadlines('breitbart-news')
    print(markov_chainer.markov(headlines))

if __name__ == "__main__":
    main()
