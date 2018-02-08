# News_Ebooks
## WIP Notes
**This is a WIP**
This program is currently a WIP. At the moment it is a very simple news ebooker. In the future I hope to include natural language processing to make some more interesting and believable headlines

#News API
This program uses the news api, aptly named News API (https://newsapi.org/), to request JSON files of news articles from specific sources. To reduce the amount of requests made it will only make a new request if the JSON file doesn't exist or is more than a day old otherwise it will read from the file

## Markov Chains
As most ebookers do, this involves markov chains which takes a list of headlines and breaks them down into pairs of words. These pairs are put into a dictionary. To write the headline we select a random starting word then a word that can follow the starting word and on and on until we reach the end of a headline. This was made with the assistance of my friend [notagoat](https://github.com/notagoat "Not A Goat Github")
