import tweepy
import.time


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

user=api.me

def limit_handler(cursor):
    try:
        while True:
            yeield cursor.next()
    except:
        time.sleep(300)


search_string="python"
numberofTweets= 2

for tweet in tweepy.cursor(api.search,search_string).items(numberofTweets):
    try:
        tweet.favorite()
        print("I liked that tweet")
    except tweepy.TweepError as e:
        print(e.reason)
    except stopIteration:
        break
