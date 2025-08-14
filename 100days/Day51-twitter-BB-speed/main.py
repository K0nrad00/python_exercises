# Twitter/x bot that complains to ISP about the speed, uses speedtest.net
import os

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

# My package name: SKY_ULTRAFAST_PLUS
MINIMUM_DOWN = 2
MINIMUM_UP = 1 #min upload speed
CONTRACT_DOWNLOAD = 500
CONTRACT_UPLOAD = 30

TWITTER_EMAIL = os.environ["TWITTER_EMAIL"]
TWITTER_PASSW = os.environ["TWITTER_PASSW"]
TWITTER_USERNAME = os.environ["TWITTER_USERNAME"]
SPEEDTEST_URL = "https://www.speedtest.net/"


class InternetSpeedTwitterBot:
    def __init__(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=chrome_options)
        self.wait = WebDriverWait(self.driver, 5)
        self.download = None
        self.upload = None

    def reject_cookies(self):
        ''' helper to reject cookies from speedtest.net '''
        # id = "onetrust-reject-all-handler" > Reject
        reject = self.driver.find_element(By.ID, "onetrust-reject-all-handler")
        reject.click()

    def get_internet_speed(self):
        self.driver.get(SPEEDTEST_URL)
        self.driver.implicitly_wait(5)  # wait to load
        self.reject_cookies()
        self.driver.implicitly_wait(5) # wait to load
        go_button = self.driver.find_element(By.CLASS_NAME, "start-text")
        go_button.click()
        self.driver.implicitly_wait(5)
        wait = WebDriverWait(self.driver, 180)
        # Wait for the element to be visible
        wait.until(
            EC.visibility_of_element_located((By.CLASS_NAME, "result-item"))
        )
        try:
            self.download = self.driver.find_element(By.XPATH, '//*[@id="container"]/div[1]/div[3]/div/div/div/div[2]/div[2]/div/div[4]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span').text
            self.upload = self.driver.find_element(By.XPATH, '//*[@id="container"]/div[1]/div[3]/div/div/div/div[2]/div[2]/div/div[4]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span').text
            # return self.download.text, self.upload.text
        except Exception as e:
            # return e #DEBUG
            pass #BAD practise, should be at least log


    def tweeter_login(self):
        self.driver.get("https://x.com/")
        self.driver.implicitly_wait(10)
        # xpath = //*[@id="react-root"]/div/div/div[2]/main/div/div/div[1]/div/div/div[3]/div[3]/a/div
        # xpath2 = //*[@id="react-root"]/div/div/div[2]/main/div/div/div[1]/div/div/div[2]/div[3]/a/div
        try: # there are 2 different xpaths, depending on which twitter ui you randomly get
            sign_in_button = self.driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div[1]/div/div/div[3]/div[3]/a/div')
            sign_in_button.click()
        except Exception as e:
            try:
                sign_in_button = self.driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div[1]/div/div/div[2]/div[3]/a/div')
                sign_in_button.click()
            except Exception as e:
                #print(e) # DEBUG
                pass #BAD practise, should be at least log
        # Wait for the element to be visible
        self.wait.until(
            EC.visibility_of_element_located((By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]'))
        )
        email = self.driver.find_element(By.XPATH, "//input[@name='text']")
        email.send_keys(TWITTER_EMAIL)
        # <span class="css-1jxf684 r-bcqeeo r-1ttztb7 r-qvutc0 r-poiln3">Next</span>
        next_button = self.driver.find_element(By.XPATH, "//span[text()='Next']")
        next_button.click()
        self.driver.implicitly_wait(2)
        #SOMETIMES X also asks for your phone number or username.. If it asks for username few times - this will fail
        try:
            # ref: https://gist.github.com/TheMuellenator/e6dc9a8a75ae1bbce550a664fff6cbd7?permalink_comment_id=5654661#gistcomment-5654661
            password = self.driver.find_element(By.XPATH, "//input[@name='password']")
            password.send_keys(TWITTER_PASSW)
        except:
            try:
                username = self.driver.find_element(By.XPATH, "//input[@name='text']")
                username.send_keys(TWITTER_USERNAME)
                next_button = self.driver.find_element(By.XPATH, "//span[text()='Next']")
                next_button.click()
                self.driver.implicitly_wait(3)
            except:
                pass #THIS should be handled properly

        password = self.driver.find_element(By.XPATH, "//input[@name='password']")
        password.send_keys(TWITTER_PASSW)
        self.driver.implicitly_wait(2)
        log_in_button = self.driver.find_element(By.XPATH, "//span[text()='Log in']")
        log_in_button.click()

    def tweet_at_provider(self):
        # //*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div[2]/div[1]/div/div
        self.wait.until(
            EC.visibility_of_element_located((By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div[2]/div[1]/div/div'))
        )

        post = self.driver.find_element(By.CSS_SELECTOR, 'div[aria-label="Post text"]')
        if float(self.download) <= MINIMUM_DOWN or float(self.upload) <= MINIMUM_UP:
            post.send_keys(f"Hey @MyISP.. My Download today is only {self.download} and upload is {self.upload}. Please fix asap")
        else:
            post.send_keys(f"Download: {self.download}Mbps, Upload: {self.upload}Mbps")
        post_button = self.driver.find_element(By.CSS_SELECTOR, 'div[data-testid="toolBar"] button[data-testid="tweetButtonInline"]')
        post_button.click()

bot = InternetSpeedTwitterBot()
bot.get_internet_speed()
# print(down)
# print(up)
sleep(5) # wait for X platform to load
bot.tweeter_login()
bot.tweet_at_provider()

