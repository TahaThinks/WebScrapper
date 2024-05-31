
from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/news")
yc_webpage = response.text

soup = BeautifulSoup(yc_webpage, "html.parser")


articles_tags = soup.find_all(name="span", class_="titleline")
for article_tag in articles_tags:
    print(article_tag.a.text)
    print(article_tag.a['href'])

articles_scores = soup.find_all(name="span", class_="score")
for article_score in articles_scores:
    print(article_score.text)
