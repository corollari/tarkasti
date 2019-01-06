import tweepy, math, time
from secret import *
from web3 import Web3

twitterCreationTimestamp=1104537600 # 01/01/2005 @ 12:00am (UTC)
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

def calculateTokens2Mint(creationTimestamp, followers):
    now = time.time()//1
    return math.exp((now-creationTimestamp)/(now-twitterCreationTimestamp))*followers

#override tweepy.StreamListener to add logic to on_status
class MyStreamListener(tweepy.StreamListener):
    def on_status(self, status):
        if not status.retweeted:
            print(status.text)
            #api.retweet(status.id)
            print(status.author.screen_name)
            print(status.author.timestamp())
            print(status.author.followers_count)

#myStreamListener = MyStreamListener()
#myStream = tweepy.Stream(auth = api.auth, listener=myStreamListener)
#myStream.filter(track=['python'])

web3 = Web3(Web3.IPCProvider("~/.ethereum/rinkeby/geth.ipc"))
print(web3.eth.accounts)
#ABI = json.loads(open("./contract/ABI.json").read())
#token = w3.eth.contract(address='0x0c1f74fe9782136e150403348800961c0c083afb', abi=ABI)
#token.functions.balanceOf('0xD1220A0cf47c7B9Be7A2E6BA89F429762e7b9aDb').call()
