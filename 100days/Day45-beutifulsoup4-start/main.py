from bs4 import BeautifulSoup
# import lxml

with open("website.html") as f:
    contents = f.read()
    lines = f.readline()


# print(type(contents))
# print(contents)


soup = BeautifulSoup(contents, "html.parser")
print(soup.title)
print(soup.title.name)
print(soup.title.string)

# anchor_tags = soup.findAll(name="a")
a_tags = soup.find_all(name="a")
print(a_tags)
# print(a_tags == anchor_tags)

# get links
for tag in a_tags:
    print(tag.get("href"))
    #print names
    print(tag.get_text())


get_specific_heading = soup.find(name="h1", id="name")
print(get_specific_heading)

get_heading_marked_as_class = soup.find(name="h3", class_="heading")
print(get_heading_marked_as_class)

# using css tags in bs4
company_url = soup.select_one(selector="p a")
print(company_url.get("href"))

# class="heading"
h3 = soup.select_one(selector=".heading")
print(h3)

# all list
list_items = soup.select(selector="li")
print(list_items)