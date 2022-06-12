import datetime
import json
import random

import memeUtil
import PreviousRequestTime
import RateLimit
from MabelPassy import MemeConfig as Config

'''
    Black box diagram of this class

                  _______________
                 |               |
    giveMeme() --|   MemeRequest |-- post
                 |_______________|

    Where post = {
        "title" : someTitle, 
        "url" : someUrl, 
        "nsfw" : True/False
        }
'''


class MemeRequest:
    """
    Requests memes from various subreddits, but limits the
    rate of requests to 1 every 30 min.
    This class is instantiated once per request.
    """

    subreddits = [
        'dankmemes',
        'me_irl',
        'MemeEconomy',
        'ProgrammerHumor',
        'rarepuppers',
        'Aww',
        'wholesomememes',
        'mademesmile'

    ]
    danksubs = subreddits[0:3]
    awwsubs = subreddits[4:5]
    wholesomesubs = subreddits[6:7]

    RATE_LIMIT = 1800  # 1800 seconds = 30 min

    def __init__(self):
        self.time_of_creation = datetime.datetime.now()
        self.rateLimiter = RateLimit.RateLimit(MemeRequest.RATE_LIMIT)
        self.prevReqTime = PreviousRequestTime.PreviousRequestTime(Config.PreviousRequestTime)

    def __parseMemes(self):
        """Parses the json response"""
        memeDict = {}
        for subreddit in MemeRequest.subreddits:
            filename = Config.SubredditCacheDirectory + subreddit + '.json'
            data = memeUtil.loadJsonFile(filename)
            memes = {}
            # Parse the json response
            for i in range(0, 25):
                title = data['data']['children'][i]['data']['title']
                url = data['data']['children'][i]['data']['url']
                nsfw = (data['data']['children'][i]['data']['thumbnail'] == 'nsfw')
                memes[i] = {
                    "title": title,
                    "url": url,
                    "nsfw": nsfw
                }
            memeDict[subreddit] = memes
        jsonString = json.dumps(memeDict)

        f = open(Config.MemeDict, 'w')
        f.write(jsonString)
        f.close()

    def __request(self):
        """Request memes (if the rate limiter allows)"""
        # Calculate the delta time
        prev_datetime = self.prevReqTime.get()
        delta_seconds = (self.time_of_creation - prev_datetime).total_seconds()
        # Limit the rate
        canRequest = self.rateLimiter.canAct(delta_seconds)
        # canRequest = True
        # If request available, then send it
        if canRequest:
            print("Request sent")
            memeUtil.getJsonFile()
            self.__parseMemes()
            self.prevReqTime.update(self.time_of_creation)
        # True => A request has been sent
        # False => A request has not been sent
        return canRequest

    def giveMeme(self, subreddit):
        """Request the latest (dankest) memes"""
        self.__request()
        memeDict = memeUtil.loadJsonFile(Config.MemeDict)
        # Pick a random sub and a random post from that sub
        if subreddit == "dank":
            sub = MemeRequest.danksubs[random.randint(0, len(MemeRequest.danksubs) - 1)]
        elif subreddit == "aww":
            sub = MemeRequest.awwsubs[random.randint(0, len(MemeRequest.awwsubs) - 1)]
        elif subreddit == "wholesome":
            sub = MemeRequest.wholesomesubs[random.randint(0, len(MemeRequest.wholesomesubs) - 1)]
        else:
            sub = MemeRequest.subreddits[random.randint(0, len(MemeRequest.subreddits) - 1)]
        postnum = random.randint(0, 24)
        post = memeDict[sub][str(postnum)]
        # Return the post
        return post
