import config, requests, json, time, os, platform

def checkIfFilesExpiered(source):
    path = source+'.json'
    if os.path.isfile(path):
        if platform.system() == 'Windows':
            creationDate = os.path.getctime(path)
        else:
            stat = os.stat(path)
            try:
                creationDate = stat.st_birthtime
            except AttributeError:
                # We're probably on Linux. No easy way to get creation dates here,
                # so we'll settle for when its content was last modified.
                creationDate = stat.st_mtime

        return time.time() - 86400 > creationDate
    else:
        return True

def loadJSON(source):
    headlines = []
    with open(source+'.json','r', encoding='utf-8') as json_data:
        d = json.load(json_data)
        for i in d['articles']:
            headlines.append(i['title'])
        return headlines

def loadNews(source):
    api_key = config.newsapi_key
    url = ('https://newsapi.org/v2/top-headlines?sources=breitbart-news&apiKey=f5f07d8f68a1482689a3f8036f25aa4a')
    response = requests.get(url)
    response = response.json()

    headlines = []
    if response['status'] != 'ok':
        print("News API Error:" + response['status'])
        return loadJSON(source)
    for i in response['articles']:
        headlines.append(i['title'])
    with open(source+'.json','w', encoding='utf-8') as json_file:
        json.dump(response, json_file)

    return headlines

def loadHeadlines(source):
    if checkIfFilesExpiered(source):
        #More than a day so load more news
        return loadNews(source)
    else:
        #Less than a day so load the JSON file
        return loadJSON(source)
