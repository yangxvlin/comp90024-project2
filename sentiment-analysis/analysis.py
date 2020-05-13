import re
from textblob import TextBlob


class TwitterClassifier():

    def clean_tweet(self, tweet):
         return ' '.join(re.sub("(@[A-Za-z0-9]+) | ([ ^ 0-9A-Za-z \t]) \
                                | (\w+: \/\/\S+)", " ", tweet).split())
    
    def to_text(self, tObject):
        return tObject['full_text']


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

        if polarity == 0:
            res.append("neutral")
        elif polarity > 0:
            res.append("positive")
        else:
            res.append("negative")
        
        if subjectivity > 0:
            res.append("objective")
        elif subjectivity == 0:
            res.append("neutral")
        else:
            res.append("objective")

        return res


if __name__ == "__main__":
    import json

    p = TwitterClassifier()

    with open("test.jsonl") as f:
        for t in f.readlines():
            tweet = json.loads(t)
            print(tweet['full_text'])
            print(p.analyse(tweet))
            break
