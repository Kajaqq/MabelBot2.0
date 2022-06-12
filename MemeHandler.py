import MemeRequest

def MemeHandler(type):
    mc = MemeRequest.MemeRequest()
    post = mc.giveMeme(type)
    memeStuff = [post['title'], post['url']]
    return memeStuff
