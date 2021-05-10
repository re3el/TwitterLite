# TwitterLite
## A user configurable twitter feed experience!

### About
If you ever wondered on how to get rid of the ads that constantly keep popping on your twitter feed, this is a good place to get started. Using the twitter APIs, you can tweak your user feed to be the way you wish - I personally hate seeing the constant ad/sponsored tweets, the games which I don't wish to play, and the random recommendations which I don't really care about. In other words, this project is all about creating a user-configurable twitter feed.

### Configuration
- First thing you need for playing with the twitter APIs is getting a twitter developer account: https://developer.twitter.com/en/apply-for-access
- Using the developer account, you will need to generate these four tokens - `consumer_key`, `consumer_secret`, `access_token_key`, `access_token_secret` so that you can gain access to the twitter APIs - https://developer.twitter.com/ja/docs/basics/authentication/guides/access-tokens
  > Use the generated tokens from above in the place holders in Main.py program
- Flask and python-twitter are the only libs I had to install for running this project - both of these can be installed using pip. pip install flask.
- With these installed, you can now run python3 Main.py in your terminal and visit http://localhost:8000 in your browser to see your own configured TwitterLite :)
  > Re-run the code to fetch the latest results in your local browser!
<br></br>

### Demo
![image](https://user-images.githubusercontent.com/8306822/117591414-3780f980-b0e9-11eb-85f0-fcf9fa5065aa.png)

### Going Forward
- Currently, this project fetches the results once per ever run. Having the option to fetch the latest results by the minute/second would be the most useful next step imo. This would make it seemless and a much happier user experience.
- Being an amateur frontend engineer, I did not focus much on the aesthetics of the website but that's one of the biggest places of improvements I can think of in my mind - Consider the scenario of having multiple userfeeds in the same screen each one serving a different purpose (these are difficult projects to scale but let's think about it when we get there)
- A whole set of avenues lie around in making the feed actually user-configurable. For example:
  - Giving the option of viewing the verified-user tweets only (different from search where you can currently only search for a person)
  - Configure to only read the tweets from a subset of followers (make collections and view the feed as per the choice)
  - Generate a better follower-recommendation system based on the location, interests, etc (recommend people based on the set of topics configured)

### Feedback
Please reach out to me at yogeshdorbala@gmail.com. Would love to know more!
