import tweepy, math, time, json
from secret import *
from web3 import Web3
from web3.middleware import geth_poa_middleware
from threading

twitterCreationTimestamp=1104537600 # 01/01/2005 @ 12:00am (UTC)
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)
twitterUserId = 1081764112949039111

web3 = Web3(Web3.IPCProvider("~/.ethereum/rinkeby/geth.ipc"))
web3.middleware_stack.inject(geth_poa_middleware, layer=0)
web3.personal.unlockAccount(web3.personal.listAccounts[0], gethPassword, 15000)
ABI = json.loads(open("./contract/ABI.json").read())
token = web3.eth.contract(address='0xd2930f4FECE79a51DdF7618299701470CFB61790', abi=ABI) # '0x0c1f74fe9782136e150403348800961c0c083afb' without checksum

claims={}

def countVotes(tweetId): # This functiom contains horrible code that should have never went into a project that I do to get a job but, well... it is fun
    time.sleep(60)
    claimCount=[0,0] # [false, true]
    for claim in claims[tweetId]:
        claimCount[1 if claim['reply'] == 'true' else 0] += claim['balance'] # Trying to be clever... huh
    winner=["false", "true"][claimCount.index(max(claimCount))]
    winners=list(filter(lambda x: x['reply']==winner, claims[tweetId]))
    earningsPerWinner=(min(claimCount)*0.2)/len(winners)
    paid=0;
    for claim in claims[tweetId]:
        if claim['reply'] != winner:
            try:
                token.functions.transferFrom(claim['user'], "trustory",claim['balance']*0.2).transact({'from': web3.eth.accounts[0]})) # Unchecked assumption: Account retains >= 20% of the tokens that it had when it issued its vote
            except:
                pass
    for claim in winners:
        token.functions.transferFrom("trustory", claim['user'], earningsPerWinner).transact({'from': web3.eth.accounts[0]}))



def calculateTokens2Mint(creationTimestamp, followers):
    now = time.time()//1
    return int(math.exp((now-creationTimestamp)/(now-twitterCreationTimestamp))*followers)

class retweetStream(tweepy.StreamListener):
    def on_status(self, status):
        if status.author.id != twitterUserId:
            tweetId = api.update_status(status.text).id
            claims[tweetId]=[]
            threading.Thread(target=lambda : countVotes(tweetId)).start()

class replyStream(tweepy.StreamListener):
    def on_status(self, status):
        if status.in_reply_to_user_id == twitterUserId:
            reply = lowercase(status.text)
            if reply == "true" or reply == "false":
                if token.functions.checkIfGiven(status.author.screen_name).call():
                    balance=token.functions.balanceOf(status.author.screen_name).call()
                else:
                    balance =  calculateTokens2Mint(status.author.created_at.timestamp(), status.author.followers_count)
                    token.functions.mint(status.author.screen_name, balance).transact({'from': web3.eth.accounts[0]}))
                claims[status.in_reply_to_status_id].append({
                    'balance': balance,
                    'user': status.author.screen_name,
                    'reply': reply
                    })


 
tweepy.Stream(auth = api.auth, listener=retweetStream()).filter(track=['@tarkasti'])
tweepy.Stream(auth = api.auth, listener=replyStream()).filter(follow=[twitterUserId])
