# Breitbart_Ebooks
## WIP Notes
**This is a WIP**
At some point this will be using a News API (https://newsapi.org/) to get headlines from Breitbart News to keep this updated with recent articles, however currently it uses a local JSON file which is in the same format at the News API.

## Markov Chains
As most ebookers do, this involves markov chains which takes a list of headlines and breaks them down into pairs of words. These pairs are put into a dictionary. To write the headline we select a random starting word then a word that can follow the starting word and on and on until we reach the end of a headline. This was made with the assistance of my friend [notagoat](https://github.com/notagoat "Not A Goat Github")
