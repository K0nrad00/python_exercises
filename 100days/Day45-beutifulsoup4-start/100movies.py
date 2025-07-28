import requests
from bs4 import BeautifulSoup
import lxml

response = requests.get(url="https://www.empireonline.com/movies/features/best-movies-2/")
print(response.status_code)
url_content = response.text


soup = BeautifulSoup(url_content, "lxml")
print(soup.title)


titles = soup.select(selector="h2 strong")
# print(titles)

for t in titles[::-1]:
    with open("movies.txt", "a") as f:
        f.write(f"{t.get_text()} \n")

