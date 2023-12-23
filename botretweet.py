# -*- coding: utf-8 -*-
"""
Created on Sat Aug 29 17:56:37 2020
Author: Parzival

Script to automate Twitter interactions using Selenium.
"""

from selenium import webdriver
import selenium.webdriver.common.keys as Keys
import time

# Set up Chrome WebDriver
driver = webdriver.Chrome('C:\\Program Files\\chromedriver.exe')
driver.get("https://www.twitter.com")

# Login Process
login_button = driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div/main/div/div/div/div[1]/div/a[2]')
login_button.click()
time.sleep(2)  

username_field = driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div[1]/form/div/div[1]/label/div/div[2]/div/input')
username_field.send_keys("your_email_here") 

password_field = driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div[1]/form/div/div[2]/label/div/div[2]/div/input')
password_field.send_keys("your_password_here")  
password_field.send_keys(Keys.ENTER)

# Searching for a hashtag
time.sleep(5)  # Wait for home page to load
search_box = driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/header/div/div/div/div[1]/div[2]/nav/a[2]')
search_box.send_keys("#IndiaAgainstNaxals")
search_box.send_keys(Keys.ENTER)

# Retweeting the first tweet
time.sleep(5)  # Wait for search results to load
tweets = driver.find_elements_by_xpath('//div[@data-testid="tweet"]')
if tweets:
    first_tweet = tweets[0]
    retweet_button = first_tweet.find_element_by_xpath('.//div[@data-testid="retweet"]')
    retweet_button.click()
    time.sleep(1)  # Wait for the retweet confirmation dialog

    # Confirm the retweet
    confirm_button = driver.find_element_by_xpath('//div[@data-testid="retweetConfirm"]')
    confirm_button.click()
else:
    print("No tweets found")


driver.quit()
