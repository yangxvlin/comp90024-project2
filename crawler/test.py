import GetOldTweets3 as got

tweetC = got.manager.TweetCriteria().setQuerySearch("covid-19")\
                                    .setMaxTweets(2)\
                                    .setEmoji('unicode')\
                                    .setNear('Melbourne')\
                                    .setSince("2020-02-20")\
                                    .setUntil("2020-03-01")

tweet = got.manager.TweetManager.getTweets(tweetC)

print("got tweet", len(tweet))

for i in tweet:
    if i.geo is not "":
        print(i.geo)

print(tweet[0].permalink)
