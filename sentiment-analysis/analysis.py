import re
from textblob import TextBlob


class TwitterClassifier():

    def clean_tweet(self, tweet):
         return ' '.join(re.sub("(@[A-Za-z0-9]+) | ([ ^ 0-9A-Za-z \t]) \
                                | (\w+: \/\/\S+)", " ", tweet).split())
    
    def to_text(self, tObject):
        return tObject['full_text']


    def analyse(self, tweet, num_mode=False):
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

        res.append(polarity)
        res.append(subjectivity)
        return res


if __name__ == "__main__":
    import json
    import numpy as np

    p = TwitterClassifier()

    pd = [[],[],[]]

    with open("test.jsonl") as f:
        for t in f.readlines():
            tweet = json.loads(t)
            polarity, subjectivity = p.analyse(tweet, num_mode=True)
            year = np.random.randint(low=0, high=80, size=1)[0]
            pd[0].append(polarity)
            pd[1].append(subjectivity)
            pd[2].append(year)

    with open("test.csv", "w") as f:
        f.writelines("polarity,subjectivity,years_old\n")
        
        for i in range(len(pd[0])):
            for j in range(len(pd)):
                f.writelines(str(pd[j][i]))
                if j < len(pd) -1:
                    f.writelines(",")
            f.writelines("\n")
