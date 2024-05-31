
from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/news")
yc_webpage = response.text

soup = BeautifulSoup(yc_webpage, "html.parser")

article_texts = []
article_links = []


articles_tags = soup.find_all(name="span", class_="titleline")
for article_tag in articles_tags:
    article_texts.append(article_tag.a.text)
    article_links.append(article_tag.a['href'])

articles_upvotes = [int(score.text.split()[0]) for score in soup.find_all(name="span", class_="score")]

# print(article_texts)
# print(article_links)
print(articles_upvotes)
highest_score = max(articles_upvotes)
highest_score_index = articles_upvotes.index(max(articles_upvotes))
print(article_texts[highest_score_index])
print(article_links[highest_score_index])

print(f"Removing the Value {highest_score} with index {highest_score_index}")
articles_upvotes.pop(highest_score_index)
print(articles_upvotes)
