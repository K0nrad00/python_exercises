# https://playwright.dev/docs/codegen ->  playwright codegen <url>
from playwright.sync_api import sync_playwright
import os

SIMILAR_ACCOUNT = "itchybootstravel"
INSTA_USERNAME = os.environ["USERNAME"]
INSTA_PASSWORD = os.environ["PASSWORD"]
INSTA_URL = "https://www.instagram.com/"

class InstaFollower:
    '''Goal: to find insta account and follow all followers of given SIMILAR_ACCOUNT'''
    def __init__(self):
        start = sync_playwright().start()
        self.browser = start.chromium.launch(headless=False, slow_mo=150)  # DEBUG only
        # self.browser = start.chromium.launch() #HEADLESS
        self.page = self.browser.new_page()

    def reject_cookies(self):
        self.page.get_by_role("button", name="Decline optional cookies" ).click()

    def insta_login(self):
        self.page.goto(INSTA_URL)
        self.reject_cookies()
        self.page.get_by_role("textbox", name="Phone number, username or").fill(INSTA_USERNAME)
        self.page.get_by_role("textbox", name="Password").fill(INSTA_PASSWORD)
        self.page.get_by_role("button", name="Log in", exact=True).click()
        self.page.wait_for_timeout(1000) #DEBUG
        try:
            self.page.get_by_role("button", name="Not now").click() #refuse to save login creds
        except Exception as e:
            try:
                self.reject_cookies() #sometimes it asks cookies again?
            except Exception as e:
                pass

    def find_account(self):
        self.page.goto(f"{INSTA_URL}{SIMILAR_ACCOUNT}")

    def find_followers(self):
        self.page.get_by_role("link",
                              name=" followers").click()  # NOTE; `name` - By default, matching is case-insensitive and searches for a substring
        self.page.wait_for_timeout(1000) #DEBUG

    def follow(self, number_of_repeats):
        '''
        follow one instagrammer and close the window, the action is performed x number_of_repeats,
        number of repeats is number you will follow at each run
        '''
        for _ in range(number_of_repeats):
            try:
                self.find_followers()
                self.page.locator("._aswp._aswr._aswu").first.click() #follow first one that is not followed atm
                self.page.wait_for_timeout(1000) # wait 1 sec
                self.page.get_by_role("button", name="Close").click() #close the followers window
            except Exception as e:
                print(e) # likely out of range error
            # ref: https://playwright.dev/python/docs/api/class-locator


follower_bot = InstaFollower()
follower_bot.insta_login()
follower_bot.find_account()
follower_bot.follow(3) #follow 3 followers of SIMILAR_ACCOUNT