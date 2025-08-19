# version of the same functionality as main.py but using playwright instead of selenium

from playwright.sync_api import sync_playwright
import os

# MINIMUM_DOWN = 2
# MINIMUM_UP = 1 #min upload speed
CONTRACT_DOWNLOAD = 500
CONTRACT_UPLOAD = 30

TWITTER_EMAIL = os.environ["TWITTER_EMAIL"]
TWITTER_PASSW = os.environ["TWITTER_PASSW"]
TWITTER_USERNAME = os.environ["TWITTER_USERNAME"]
SPEEDTEST_URL = "https://www.speedtest.net/"
# NOTE: this tool is handy to discover 'locators' (instead of classes and other html elements) in playwright: https://playwright.dev/docs/codegen
# NOTE: script works in headed mode (most of the time) but not in headless - headed option commented out, fails on tweet_login stage - might be some antibot software

class SpeedToTwit:
    def __init__(self):
        start = sync_playwright().start()
        self.browser = start.chromium.launch(headless=False, slow_mo=150) #DEBUG only
        # self.browser = start.chromium.launch() #HEADLESS
        self.page = self.browser.new_page()
        self.download_speed = None
        self.upload_speed = None

    def reject_cookies(self):
        self.page.goto("https://www.speedtest.net/")
        self.page.get_by_role("button", name="Reject All").click()

    def get_speed(self):
        self.reject_cookies()
        go_button = self.page.get_by_text("Go")
        go_button.click()
        self.page.wait_for_timeout(20000) #wait 20 sec for download to change from default "-" to speed
        download_locator = self.page.locator(".download-speed")
        # await expect(download).not_to_contain_text("-", use_inner_text=True) #`.` for speed e.g. 250.45
        self.download_speed = download_locator.inner_text()
        self.page.wait_for_timeout(20000) # wait another 20 sec for upload
        upload_locator = self.page.locator(".upload-speed")
        self.upload_speed = upload_locator.inner_text()
        # print(download_speed, upload_speed) #DEBUG

    def tweet_login(self):
        self.page.goto("https://x.com/")
        try:
            sign_in_button = self.page.get_by_test_id("loginButton")
            sign_in_button.click()
        except Exception as e:
            pass
        # self.page.wait_for_timeout(2000) # wait for module to load, not needed
        email_input = self.page.get_by_role("textbox", name="Phone, email address, or")
        email_input.fill(TWITTER_EMAIL)
        self.page.get_by_role("button", name="Next").click()
        try:
            password = self.page.get_by_role("textbox", name="Password Reveal password")
            password.fill(TWITTER_PASSW)
            self.page.get_by_test_id("LoginForm_Login_Button").click()
        except:
            try:
                username = self.page.get_by_test_id("ocfEnterTextTextInput")
                username.fill(TWITTER_USERNAME)
                self.page.get_by_test_id("ocfEnterTextNextButton").click()
            except Exception as e:
                print("Error at username stage", e)
        password = self.page.get_by_role("textbox", name="Password Reveal password")
        password.fill(TWITTER_PASSW)
        self.page.get_by_test_id("LoginForm_Login_Button").click()

    def post_tweet(self):
        self.tweet_login()
        tweet_box = self.page.get_by_test_id("tweetTextarea_0").locator("div").nth(2)
        tweet_box.fill(f"Today's speed is; download - {self.download_speed}Mbps, upload - {self.upload_speed}Mbps [this is using playwright script]")
        post_button = self.page.get_by_test_id("tweetButtonInline")
        post_button.click()

    def close_browser(self):
        self.browser.close()


bot = SpeedToTwit()
bot.get_speed()
bot.post_tweet()
# bot.close_browser() #Not sure if that is needed really
