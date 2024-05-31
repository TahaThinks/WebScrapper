import requests
from bs4 import BeautifulSoup

url = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"
response = requests.get(url)
movies_webpage = response.text

soup = BeautifulSoup(movies_webpage, "html.parser")
movies_list = [movie.text for movie in soup.find_all(name="h3", class_="title")]
print(movies_list[::-1])
