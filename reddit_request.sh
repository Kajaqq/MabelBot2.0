#!/usr/bin/env bash

# Positional Args: ./request_reddit $1, where $1 = the name of the subreddit
curl -A 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36' -X GET -L https://www.reddit.com/r/$1/top/.json?count=20 > files/cache/subreddit_requests/$1.json