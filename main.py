
from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/news")
yc_webpage = response.text

soup = BeautifulSoup(yc_webpage, "html.parser")

article_tag = soup.find(name="span", class_="titleline")
print(article_tag.a.text)
print(article_tag.a['href'])

article_score = soup.find(name="span", class_="score")
print(article_score.text.split()[0])


# article_links = soup.find_all(name='span', class_="titleline")

# for article_link in article_links:
#     print(article_link.a.text)
