import tweepy

api_key = "yHAJgaLyyzoPC54ZIOqFMVQgm"
api_secret = "IteijZA5I8X3GUIlk7Rvguq7kjdsyppaln4H6JqmQVUp1qYQu8"

acc_token = "1251736692341366784-e3SefdSdbxGAjLN5cxSXYzUQFCZ2gK"
acc_secret = "SLmyvGwbI8MQMqaSSiXt1OX8X3brEbODCrYMoBTH92KuQ"

tweetsPerQry = 100
maxTweets = 1000000
hashtag = "#covid-19"

great_melb = [144.31638069715942, -38.51027328718954, 145.90390511094049, -37.16111433367172]
center_melb = [145.1028, -37.8658]

authentication = tweepy.OAuthHandler(api_key, api_secret)
authentication.set_access_token(acc_token, acc_secret)
api = tweepy.API(authentication, wait_on_rate_limit=True,
                 wait_on_rate_limit_notify=True)
                
maxId = -1
tweetCount = 0
while tweetCount < maxTweets:
    if(maxId <= 0):
        newTweets = api.search(q=hashtag, count=tweetsPerQry,
                               result_type="recent", tweet_mode="extended")
    else:
        newTweets = api.search(q=hashtag, count=tweetsPerQry, max_id=str(
            maxId - 1), result_type="recent", tweet_mode="extended")

    if not newTweets:
        # nothing here so far
        break

    for tweet in newTweets:
        #print(tweet.full_text.encode('utf-8'))
        print(tweet._json)
        exit(1)

    tweetCount += len(newTweets)
    maxId = newTweets[-1].id
