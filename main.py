
from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/news")
yc_webpage = response.text

soup = BeautifulSoup(yc_webpage, "html.parser")
links = soup.find(name='span', class_="titleline")

# print(link.a["href"])
# for Links the href is in an anchor tag with span class="titleline"
# Score is in Class="Score"
