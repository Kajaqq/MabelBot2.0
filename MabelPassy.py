class MabelConfig(object):
    bannned_ids = [""]
    id_grupki=''
    login = "login"
    password = "password"


class MemeConfig(object):
    # files/cache/
    SubredditCacheDirectory = 'files/cache/subreddit_requests/'
    MemeDict = 'files/cache/MemeDict.json'
    # files/temp/
    MemePicture = 'files/temp/memepic.png'
    # files/timing/
    PreviousRequestTime = 'files/timing/prev_req_time.txt'
    # files/sounds/
    SoundsDirectory = 'files/sounds/'
