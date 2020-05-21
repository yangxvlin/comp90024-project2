import re
from textblob import TextBlob


class TwitterClassifier():

    def clean_tweet(self, tweet):
         return ' '.join(re.sub("(@[A-Za-z0-9]+) | ([ ^ 0-9A-Za-z \t]) \
                                | (\w+: \/\/\S+)", " ", tweet).split())
    
    def to_text(self, tObject):
        return tObject['text']


    def analyse(self, tweet):
        """
        init the class object and simply pass either twitter object or 
        tweets plain text to this method. The analysis will return a list
        indicating the polarity and subjectivity of the tweets.
        """

        if (type(tweet) == dict):
            text = self.clean_tweet(self.to_text(tweet))
        else:
            text = self.clean_tweet(tweet)

        analysis = TextBlob(text)
        polarity = analysis.polarity
        subjectivity = analysis.subjectivity

        res = []

        # if polarity > 0.3:
        #     res.append("positive")
        # elif polarity < -0.3:
        #     res.append("negative")
        # else:
        #     res.append("neutral")
        #
        # if subjectivity > 0.6:
        #     res.append("subject")
        # elif subjectivity < 0.3:
        #     res.append("objective")
        # else:
        #     res.append("neutral")

        res.append(polarity)
        res.append(subjectivity)

        return res


if __name__ == "__main__":
    import json

    p = TwitterClassifier()

    with open("test.jsonl") as f:
        for t in f.readlines():
            tweet = json.loads(t)
            print(tweet['text'])
            print(p.analyse(tweet))
            break
