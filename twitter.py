# importing the module 
import tweepy 

def Tweet(inpStr):
    # personal details 
    consumer_key ="d2xgptvJEsOTojta8Lz8qeVgx"
    consumer_secret ="OIsph4tEEBNkYNUWRpqm8WnaBbD4KaCzbmMldKbPB6mPAfy8RD"
    access_token ="1177841903573692417-qwKLV8HMz2c2Iz34J4NIEib7rPJfgb"
    access_token_secret ="gGC0ePQyIXj3fUJY7g8kJovVfkkisd0WI8eTUaXg5odIh"
  
    # authentication of consumer key and secret 
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret) 
  
    # authentication of access token and secret 
    auth.set_access_token(access_token, access_token_secret) 
    api = tweepy.API(auth) 
  
    # update the status 
    api.update_status(status = inpStr + "\n\n\nGenerated By BOT") 
