import requests
from bs4 import BeautifulSoupfrom selenium import webdriver
from bs4 import BeautifulSoup
import re
import time
import csv
import io
import pprint as pp


path_to_chromedriver ="C:\\Users\\kishi\\Downloads\\chromedriver_win32\\chromedriver"            #enter path of chromedriver
browser = webdriver.Chrome(executable_path = path_to_chromedriver)


url = input("Enter the url: ")  #eg: https://www.twitter.com/xyz/

#this function is to handle dynamic page content loading - using Selenium
def tweet_scroller(url):

    browser.get(url)
    
    #define initial page height for 'while' loop
    lastHeight = browser.execute_script("return document.body.scrollHeight")
    
    while True:
        browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        #define how many seconds to wait while dynamic page content loads
        time.sleep(3)
        newHeight = browser.execute_script("return document.body.scrollHeight")
        
        if newHeight == lastHeight:
            break
        else:
            lastHeight = newHeight
            
    html = browser.page_source

    return html

if __name__ == '__main__':
        
        all_tweets = []

        url = 'https://twitter.com/elonmusk'
        
        data  = tweet_scroller(url)

        html = BeautifulSoup(data.text, 'html.parser')

        timeline = html.select('#timeline li.stream-item')

        for tweet in timeline:

                tweet_id = tweet['data-item-id']
                tweet_text = tweet.select('p.tweet-text')[0].get_text()

                all_tweets.append({"id": tweet_id, "text": tweet_text})

        print(all_tweets)
