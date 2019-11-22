from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time
import random
import sys
import json
#---------------------------------------------------------------------
def login(browser, user, passcode):
        browser.get('https://www.instagram.com/accounts/login/')
        time.sleep(2)
        emailInput = browser.find_element_by_xpath('//*[@id="react-root"]/section/main/div/article/div/div[1]/div/form/div[2]/div/label/input')
        passwordInput = browser.find_element_by_xpath('//*[@id="react-root"]/section/main/div/article/div/div[1]/div/form/div[3]/div/label/input')
        emailInput.send_keys(user)
        passwordInput.send_keys(passcode)
        passwordInput.send_keys(Keys.ENTER)
        time.sleep(2)
#---------------------------------------------------------------------
def like_photo(browser, hashtag):
        browser.get("https://www.instagram.com/explore/tags/" + hashtag + "/")
        time.sleep(2)

        # gathering photos
        pic_hrefs = []
        for i in range(1, 2):# pataisyt
            try:
                browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                time.sleep(2)
                # get tags
                hrefs_in_view = browser.find_elements_by_tag_name('a')
                # finding relevant hrefs
                hrefs_in_view = [elem.get_attribute('href') for elem in hrefs_in_view
                                 if '.com/p/' in elem.get_attribute('href')]
                # building list of unique photos
                [pic_hrefs.append(href) for href in hrefs_in_view if href not in pic_hrefs]
                # print("Check: pic href length " + str(len(pic_hrefs)))
            except Exception:
                continue

        # Liking photos
        unique_photos = len(pic_hrefs)
        for pic_href in pic_hrefs:
            
            if(checkRunning() == 1):
                browser.get(pic_href)
                time.sleep(15)
                try:
                    time.sleep(random.randint(2, 4))
                    # likes = browser.find_element_by_xpath('/html/body/div[3]/div[2]/div/article/div[2]/section[2]/div/div/button/span').text
                    # print(likes)
                    # if (likes > 250):
                    follow_button = lambda: browser.find_element_by_class_name("oW_lN").click()
                    follow_button().click()
                except Exception as e:
                    time.sleep(2)

                browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")

                try:
                    time.sleep(1)
                    like_button = lambda: browser.find_element_by_xpath('//span[@aria-label="Like"]').click()
                    like_button().click()
                except Exception as e:
                    time.sleep(2)

                unique_photos -= 1
            else:
                exit()

        

#---------------
def checkRunning():
    with open('run.json') as f:
        data = json.load(f)
        running = data["process"]["running"]
        print(running)
    f.close()
    return running
#---------------



#---------------------------------------------------------------------
#if __name__ == "__main__":
def run(username, password, hashtag):
    bot = webdriver.Chrome()
    login(bot, username, password)
    like_photo(bot, hashtag)
