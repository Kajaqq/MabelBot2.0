import json
import urllib.request
import urllib.parse

class Cleverbot:
    def __init__(self, api_user, api_key, nick=None):
        self.user = api_user
        self.key = api_key
        self.nick = nick
        params = {"user": self.user, "key": self.key}
        data = str.encode(urllib.parse.urlencode(params))
        if self.nick is None:
            req = urllib.request.Request('https://cleverbot.io/1.0/create', headers={'User-Agent': 'Mozilla/5.0'})
            response = json.loads(bytes.decode(urllib.request.urlopen(req, data).read()))
            self.nick = response['nick']

    def say(self, statement):
        req = urllib.request.Request('https://cleverbot.io/1.0/ask', headers={'User-Agent': 'Mozilla/5.0'})
        params = {"user": self.user, "key": self.key, "text": statement, "nick": self.nick}
        data = str.encode(urllib.parse.urlencode(params))
        response = json.loads(bytes.decode(urllib.request.urlopen(req, data).read()))
        return response['response']
