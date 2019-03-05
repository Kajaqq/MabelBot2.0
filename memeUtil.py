import requests
import MemeRequest
import json



def getJsonFile():
    """Uses requests lib to send a GET request to the reddit api"""
    for subreddit in MemeRequest.MemeRequest.subreddits:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36',
        }

        params = (
            ('count', '20'),
        )
        response = requests.get(f'https://www.reddit.com/r/{subreddit}/top/.json', headers=headers, params=params)
        data = response.json()
        with open(f'files/cache/subreddit_requests/{subreddit}.json', 'w') as f:
            json.dump(data, f)


def loadJsonFile(filename):
    try:
        f = open(filename, 'r')
        s = f.read()
        f.close()
        data = json.loads(s)
        return data
    except IOError:
        print("Unable to open the json file")
