from bs4 import BeautifulSoup
import requests

static_url = "https://appbrewery.github.io/news.ycombinator.com/"

response = requests.get(url=static_url)
# print(response.status_code)
yc_web = response.text

soup = BeautifulSoup(yc_web, "html.parser")

# print(soup.title)

articles_tags = soup.find_all(name="a", class_="storylink")
# print(articles_tags)

articles_links = []
articles_texts = []

for article_tag in articles_tags:
    text = article_tag.get_text()
    articles_texts.append(text)
    links = article_tag.get("href")
    articles_links.append(links)

print(articles_texts)
print(articles_links)

articles_votes = [int(score.get_text().split()[0]) for score in soup.find_all(class_="score")]
# print(int(articles_votes.split()[0]))

print(articles_votes)
print(max(articles_votes))
index_of_highest_vote = articles_votes.index(max(articles_votes))
print(f"Highest voted article in the website is: "
      f"{articles_texts[index_of_highest_vote]} "
      f"with vote count: {max(articles_votes)} "
      f"link: {articles_links[index_of_highest_vote]} ")


# article_link = articles_tags.get("href")
# print(article_link)
# article_votes = soup.find(class_="score")
# print(article_votes.get_text()) #== article_votes.text)