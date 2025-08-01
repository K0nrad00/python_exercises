from bs4 import BeautifulSoup
import requests
import os
from dotenv import load_dotenv
import smtplib

load_dotenv()
SMTP_ADDRESS = os.environ["SMTP_ADDRESS"]
EMAIL_ADDRESS= os.environ["EMAIL_ADDRESS"]
EMAIL_PASSWORD=os.environ["EMAIL_PASSWORD"]

# url = "https://appbrewery.github.io/instant_pot/"
url = "https://www.amazon.ie/gp/product/B0B5PL93XQ/ref=sw_img_1?smid=ASDF7E03CFY5A&th=1"
headers = {
    "User-Agent" : "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 "
                   "(KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36",
    "Accept-Language" : "en-GB,en-US;q=0.9,en;q=0.8"
}
html_contents = requests.get(url=url)
print(html_contents.status_code) #DEBUG
html_text = html_contents.text
# print(html_text) #DEBUG

soup = BeautifulSoup(html_text, "html.parser")
print(soup.title.get_text()) #DEBUG

# <span id="productTitle" class="a-size-large product-title-word-break">
# AOC CU34V5C - 34 Inch Curved QHD Monitor, 100Hz, VA, USB-C Docking, 65W power delivery,
# USN Hub, Height Adjust, Speakers (3440 x 1440 @ 100Hz, 300 cd/m², HDMI 2.0/ DP 1.2 /
# USB-C 3.2 DP alt mode)       </span>
try:
    product = soup.find(name="span", id="productTitle")
    # print("AMZN product text:" , product.get_text()) #DEBUG
    product_name = product.text.strip() # THIS SOMETIMES THROWS 503, soup.title can be used instead
except AttributeError:
    print(f"{product_name} wasn't found on amazon")
else:
    product_name = soup.title.get_text()

# <span class="a-price-whole">295<span class="a-price-decimal">.</span></span>
# <span class="a-offscreen">€295.00</span>
price = soup.find(name="span", class_="a-offscreen")
price_float =  float(price.get_text().split("€")[1])

if price_float < 300.00:
    with smtplib.SMTP(SMTP_ADDRESS) as connection:
        connection.starttls()
        connection.login(user=EMAIL_ADDRESS, password=EMAIL_PASSWORD)
        connection.sendmail(from_addr=EMAIL_ADDRESS, to_addrs=EMAIL_ADDRESS,
                            msg=f"Subject:Item: '{product_name[0:15]}..' dropped to {price_float} on Amazon Ireland\n\n"
                                f"This item {product_name} \n\tdropped to price of €"
                                f"{price_float} - "
                                f"\n\tThis is direct link to the item: {url}.".encode("utf-8"))


