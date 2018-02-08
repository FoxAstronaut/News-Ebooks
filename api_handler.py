import config, requests, json, time, os, platform

def checkIfFilesExpiered(path,filename):
    filepath = path+'\\'+filename+'.json'
    if os.path.isfile(filepath):
        if platform.system() == 'Windows':
            creationDate = os.path.getctime(filepath)
        else:
            stat = os.stat(filepath)
            try:
                creationDate = stat.st_birthtime
            except AttributeError:
                # We're probably on Linux. No easy way to get creation dates here,
                # so we'll settle for when its content was last modified.
                creationDate = stat.st_mtime

        return time.time() - 86400 > creationDate
    else:
        return True

def loadJSON(path,filename):
    filepath = path+'\\'+filename+'.json'
    headlines = []
    with open(filepath,'r', encoding='utf-8') as json_data:
        d = json.load(json_data)
        for i in d['articles']:
            headlines.append(i['title'])
        return headlines

def loadNews(path,source):
    filepath = path+'\\'+source+'.json'
    api_key = config.newsapi_key
    url = ('https://newsapi.org/v2/top-headlines?sources=' + source + '&apiKey=' + api_key)
    response = requests.get(url)
    response = response.json()

    headlines = []
    if response['status'] != 'ok':
        print("News API Error:" + response['status'])
        return loadJSON(path,source)
    for i in response['articles']:
        headlines.append(i['title'])
    with open(filepath,'w', encoding='utf-8') as json_file:
        json.dump(response, json_file)

    return headlines

def loadHeadlines(source):
    path = 'news_files'
    if not os.path.exists(path):
        os.makedirs(path)

    if checkIfFilesExpiered(path,source):
        #More than a day so load more news
        return loadNews(path,source)
    else:
        #Less than a day so load the JSON file
        return loadJSON(path,source)
