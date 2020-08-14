import requests
from bs4 import BeautifulSoup

if __name__ == '__main__':

        all_tweets = []

        url = 'https://twitter.com/elonmusk'

        data = requests.get(url)

        html = BeautifulSoup(data.text, 'html.parser')

        timeline = html.select('#timeline li.stream-item')

        for tweet in timeline:

                tweet_id = tweet['data-item-id']
                tweet_text = tweet.select('p.tweet-text')[0].get_text()

                all_tweets.append({"id": tweet_id, "text": tweet_text})

        print(all_tweets)
