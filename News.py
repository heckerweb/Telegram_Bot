import requests
from bs4 import BeautifulSoup
import json
from Article import Article

baseUrl = "https://vnexpress.net/"

def GetNews(limit_news = 20):
    s = requests.Session()
    response = s.get(baseUrl)
    soup = BeautifulSoup(response.content, 'html.parser')
    article = soup.select("article.item-news", limit=limit_news)

    listArticle = []
    for element in article:
        title = element.select("h3.title-news > a") # Lấy phần thẻ chứa title
        description = element.select("p.description > a") # Lấy phần thẻ chứa description
        for x in range(len(title)): # serialize object này lại thành json để lấy dữ liệu dễ dàng hơn
            listArticle.append(json.dumps(Article(title[x]['title'], title[x]['href'], description[x].text).__dict__, ensure_ascii=False))
    return listArticle
