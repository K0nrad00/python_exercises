
import re
from bs4 import BeautifulSoup
import requests
from playwright.sync_api import sync_playwright
import os

G_FORM_LINK = os.environ["G_FORM_LINK"] #NOTE: form to be publicly editable
G_FORM_EDIT_LINK = os.environ["EDITABLE_FORM_LINK"] # editable link
URL = "https://appbrewery.github.io/Zillow-Clone/"
G_USERNAME = os.environ["USERNAME"]
G_PASSWORD = os.environ["PASSWORD"] #NOTE: turn off 2FA!


response = requests.get(url=URL)
html_content = response.text

soup = BeautifulSoup(html_content, "html.parser")
# print(soup.title) #DEBUG

#  Use BeautifulSoup/Requests to scrape all the listings from the Zillow-Clone web address (Step 4 above).
link_tags = soup.find_all(name="a", class_="property-card-link")
property_links = []
for link in link_tags:
    property_links.append(link.get("href"))

#  Create a list of prices for all the listings you scraped
# <span data-test="property-card-price" class="PropertyCardWrapper__StyledPriceLine">$2,895+/mo</span>
price_tags = soup.find_all(name="span", class_="PropertyCardWrapper__StyledPriceLine")
# print(price_tags)
property_prices = []
for price in price_tags:
    property_prices.append(price.get_text().strip("+/mo 1 bd"))


# Create a list of addresses for all the listings you scraped and clean up
# <address data-test="property-card-addr">
# 747 Geary Street, 747 Geary St, Oakland, CA 94609
# </address>
address_tags = soup.find_all(name="address")
# print(address_tags)
property_addresses = []
for address in address_tags:
    temp = address.get_text().strip(" \n ").split("|") #temp introduced to clean up
    property_addresses.append("".join(temp))

# print(len(property_addresses)) -> 44

# fill in the form you created (step 1,2,3 above). Each listing should have its price/address/link added to
#  the form. You will need to fill in a new form for each new listing
class PropertySpreadsheet:
    def __init__(self):
        start = sync_playwright().start()
        self.browser = start.chromium.launch(headless=False, slow_mo=150, args=[
        '--disable-blink-features=AutomationControlled',
        '--no-sandbox',
        '--disable-web-security', #use with caution
        '--disable-infobars',
        '--disable-extensions',
        '--start-maximized',
        '--window-size=1280,720',
        ])  # to address issue with log into the google. needed for g_log_in()
            # https://stackoverflow.com/questions/76603386/playwright-chrome-this-browser-or-app-may-not-be-secure
        self.page = self.browser.new_page()

    def fill_in_form(self):
        item_number = 0 #change to 42 to debug on 2 items only, otherwise should be 0
        for _ in range(len(property_addresses)): #: # range(2) for debug
            self.page.goto(G_FORM_LINK)
            self.page.get_by_role("textbox", name="What's the address of").fill(property_addresses[item_number])
            self.page.get_by_role("textbox", name="What's the price per month?").fill(property_prices[item_number])
            self.page.get_by_role("textbox", name="Whats the link to property?").fill(property_links[item_number])
            self.page.get_by_role("button", name="Submit").click()
            item_number += 1

    def g_log_in(self): # google doesn't let to sign in using chromium browser so you need additional args at the browser launch
        self.page.get_by_role("link", name="Sign in").click()
        self.page.get_by_role("textbox", name="Email or phone").fill(G_USERNAME)
        self.page.get_by_role("button", name="Next").click()
        self.page.get_by_role("textbox", name="Password").fill(G_PASSWORD)
        self.page.get_by_role("button", name="Next").click()
        self.page.wait_for_timeout(3000)
        try:
            self.page.get_by_role("button", name="Skip").click() #Skip home address if asked
        except Exception as e:
            pass


    def move_to_gsheet(self):
        self.page.goto(G_FORM_EDIT_LINK)
        self.page.wait_for_timeout(3000)
        try:
            self.page.get_by_role("button", name="Close").click()  # close pop up
        except Exception as e:
            pass
        self.g_log_in()
        self.page.get_by_text(re.compile("Responses")).first.click() # re.compile needed to match any 'Responses' link and select only first
        with self.page.expect_popup() as tab2_info:
            self.page.get_by_role("button", name="View in Sheets").click() #. Opens linked sheet. That's removed so nothing there to display at any time now
        tab2 = tab2_info.value
        tab2.wait_for_timeout(30000) #see the sheet


    def close(self):
        self.browser.close()

bot = PropertySpreadsheet()
bot.fill_in_form()
bot.move_to_gsheet()
bot.close() #probably not needed