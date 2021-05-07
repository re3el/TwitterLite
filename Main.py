import twitter
import json
from flask import Flask, jsonify, render_template
from datetime import datetime

def getPrettyJson(jsonText):
    return json.dumps(jsonText, default=lambda o: o.__dict__, indent=2, separators=(',', ': '))

def getDateTime(time):
	return  datetime.strftime(datetime.strptime(time,'%a %b %d %H:%M:%S +0000 %Y'), '%Y-%m-%d %H:%M:%S')

api = twitter.Api(
    consumer_key='FILL_ME_FROM_README',
    consumer_secret='FILL_ME_FROM_README',
    access_token_key='FILL_ME_FROM_README',
    access_token_secret='FILL_ME_FROM_README')
    
class Tweet:
    def __init__(self, user, favorite_count, retweet_count, text, location, created_at):
        self.user = user
        self.favorite_count = favorite_count
        self.retweet_count = retweet_count
        self.text = text
        self.location = location
        self.created_at = created_at

    def display(self):
        from pprint import pformat
        return pformat(vars(self), indent=4, width=1)

class User:
    def __init__(self, name, screen_name, description, verified, followers_count, friends_count, profile_image_url):
        self.name = name
        self.screen_name = screen_name
        self.description = description
        self.verified = verified
        self.followers_count = followers_count
        self.friends_count = friends_count
        self.profile_image_url = profile_image_url
    
    def display(self):
        from pprint import pformat
        return pformat(vars(self), indent=4, width=1)

# trends = api.GetTrendsCurrent()

friends = api.GetFriends(screen_name="YogeshDorbala")
tweets = []

for friend in friends:
    user = User(friend.name, friend.screen_name, friend.description, friend.verified, friend.followers_count, friend.friends_count, friend.profile_image_url)
    userTimeLine = api.GetUserTimeline(screen_name=user.screen_name, count=5)
    customTweets = []
    for tweet in userTimeLine:
        customTweets.append(Tweet(user, tweet.favorite_count, tweet.retweet_count, tweet.text, tweet.location, getDateTime(tweet.created_at)))
    tweets.extend(customTweets)

tweets.sort(key= lambda x: (x.created_at), reverse=True)
tweets = tweets[0:100]

app = Flask(__name__, static_url_path='')
@app.route('/', methods = ['GET'])
def samplefunction():
    return render_template("index.html", tweets=tweets)

if __name__ == '__main__':
    port = 8000
    app.run(host='localhost', port=port)
